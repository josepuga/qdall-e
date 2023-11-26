import random
import json
import urllib.request
import os

import openai
from openai import OpenAI

from PySide6.QtWidgets import QApplication, QMainWindow, QInputDialog
from PySide6.QtWidgets import QLineEdit, QMessageBox, QFileDialog
from PySide6.QtCore import QStandardPaths
from PySide6.QtGui import QPixmap

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from ui_form import Ui_MainWindow
from classes import Dalle2Model, Dalle3Model

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('qdall-e')

        # Para que cada vez que  se graba una imagen, el diálogo aparezca en el
        # último directorio usado. Por defecta el Directorio "Images" del sistema
        self.save_directory = QStandardPaths.writableLocation(QStandardPaths.PicturesLocation)
        # Diccionario con los diferentes objetos DalleModel
        self.dm = {Dalle3Model.model: Dalle3Model(), Dalle2Model.model: Dalle2Model()}
        self.ui.comboBoxModel.addItems([Dalle3Model.model, Dalle2Model.model])
        self.model = self.ui.comboBoxModel.currentText()
        self.updateControls()
        self.setEvents()
        # Se coge el API Key de la variable de entorno. Si no estuviera, el botón
        # send se deshabilita
        self.api_key = os.environ.get('OPENAI_API_KEY', "")
        if self.api_key == "":
            self.ui.pushButtonSendText.setEnabled(False)
        else:
            self.ui.labelApiKey.setText(self.ofuscateApiKey())
        # Sólo se permite grabar si hay una imagen válida
        self.ui.pushButtonSaveAs.setEnabled(False)
        # Pixmap original (la imagen se escala en el GUI y esta se guarda para grabar)
        self.pixmap_original = None


    # Definición de los eventos, al pulsar los botones y al cambiar de modelo
    def setEvents(self):
        self.ui.comboBoxModel.currentIndexChanged.connect(self.updateControls)
        self.ui.pushButtonSaveAs.clicked.connect(self.saveAs)
        self.ui.pushButtonSendText.clicked.connect(self.sendText)
        self.ui.pushButtonApiKey.clicked.connect(self.apiKey)

    # Devuelve un nombre de fichero de imagen acorde con el prompt que
    # introdujo el usuario. El fichero es el texto tecleado sustituyendo
    # los espacios por subrayados limitado a 100 caracteres + '-' + un número
    # aleatorio de 4 cifras
    #FIXME: Si el usuario cambia el texto despues de una petición, se usará
    #       el texto actual.
    def getImageFileName(self):
        result = self.dm[self.model].prompt
        result = result.replace(' ', '_')
        result = result[:100]
        result += '-' + str(random.randint(0,9999)).zfill(5) + ".png"
        return result

    def saveAs(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setNameFilter("Images (*.png)")
        dialog.selectFile(self.getImageFileName())
        dialog.setViewMode(QFileDialog.List)
        dialog.setDirectory(self.save_directory)
        if dialog.exec():
            filename = dialog.selectedFiles()[0]
            self.save_directory = os.path.dirname(filename)
            self.pixmap_original.save(filename, "png")


    def showError(self, message, title):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(message)
        msg_box.setWindowTitle(title)
        msg_box.exec()

    def setDefaultImage(self):
        self.ui.labelImage.setPixmap(QPixmap(':/assets/default-screen.png'))

    def loadImageFromUrl(self, url):
        self.ui.pushButtonSaveAs.setEnabled(False)
        pixmap = QPixmap()
        try:
            data = urllib.request.urlopen(url).read()
        except Exception as e:
            self.showError(f"Unable to load the image.\n{url}\nError: {e}", "Error")
            self.setDefaultImage()
            return

        if not pixmap.loadFromData(data):
            self.showError(f"Bad image format.\n{url}", "Error")
            self.setDefaultImage()
            return

        self.pixmap_original = pixmap
        height = self.ui.labelImage.height()
        width = self.ui.labelImage.width()
        if pixmap.height() > pixmap.width():
            pixmap = pixmap.scaledToHeight(height)
        else:
            pixmap = pixmap.scaledToWidth(width)
        self.ui.labelImage.setPixmap(pixmap)
        self.ui.pushButtonSaveAs.setEnabled(True)


    def sendText(self):
        self.ui.pushButtonSendText.setEnabled(False)
        # Se fuerza a actualizar los datos del modelo actual con los widgets
        self.updateDalleModel(self.ui.comboBoxModel.currentText())
        self.dm[self.model].prompt = self.ui.textEdit.toPlainText()
        client = OpenAI( api_key=self.api_key)
        message = ""
        try:
            response = None
            while response is None:
                response = client.images.generate(**self.dm[self.model].get_params())
        #Posibles errores.
        except openai.APIConnectionError as e:
            message = "Server connection error:\n {e.__cause__}"
        except openai.RateLimitError as e:
            message = f"OpenAI RATE LIMIT error {e.status_code}:\n {e.response}"
        except openai.APIStatusError as e:
            message = f"OpenAI STATUS error {e.status_code}:\n {e.response}"
        except openai.BadRequestError as e:
            message = f"OpenAI BAD REQUEST error {e.status_code}:\n {e.response}"
        except Exception as e:
            message = f"An unexpected error occurred:\n {e}"

        if message != "":
            self.showError(message, "Error")

        if response is not None:
            url = response.data[0].url
            self.loadImageFromUrl(url)
        self.ui.pushButtonSendText.setEnabled(True)

    def apiKeyIsValid(self, api_key):
        #{'error': {'message': 'Incorrect API key provided:',
        #'type': 'invalid_request_error', 'param': None, 'code': 'invalid_api_key'}}
        client = OpenAI(api_key=api_key)
        try:
            client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": "Say this is a test",
                    }
                ], model="gpt-3.5-turbo",
            )
        except openai.APIStatusError as e:
            try:
                error_info = e.response.json()
                message = error_info.get('error', {}).get('message', '<Unknow>')
                code_id = error_info.get('error', {}).get('code', '0')
            except json.JSONDecodeError:
                message = "<Unknow>"
                code_id = "0"

            message = message.replace(". ", ".\n").replace("http", "\nhttp")
            title = "Error " + code_id
            self.showError(message, title)
            return False
        else:
            return True

    def ofuscateApiKey(self):
        if len(self.api_key) < 12:
            return "*****"
        else:
            return self.api_key[:3] + "*****" + self.api_key[-4:]


    def apiKey(self):
        key, ok = QInputDialog().getText(self, "OpenAI API Key",
            u"API Key: (No se guardará en ningún sitio. Sólo durante esta sesión).",
            QLineEdit.Password)
        if ok and key:
            # Independientemente de que la clave sea válida o no, se permite la
            # opción "Send" mientras la clave no sea nula "". Esto es así porque puede
            # ser que la clave necesite créditos y el usuario haya recargado al ver
            # el error.
            self.api_key = key
            self.ui.pushButtonSendText.setEnabled(True)
            self.ui.labelApiKey.setText(self.ofuscateApiKey())
            #  No hace falta comprobar su valor. Es para enviar un diálogo de error
            self.apiKeyIsValid(key)


    # Actualiza los controles según los atributos de clase del objeto modelo activo.
    # comboBoxModel, tiene la cadena de texto que es el modelo, que a su vez sirve de
    # índice al diccionario dm.
    def updateDalleModel(self, model):
        self.dm[model].quality = self.ui.comboBoxQuality.currentText()
        self.dm[model].size = self.ui.comboBoxSize.currentText()
        self.dm[model].style = self.ui.comboBoxStyle.currentText()


    def updateControls(self):
        old_model = self.model
        # Se actualiza el modelo actual, con los valores de los widgets
        self.updateDalleModel(old_model)
        self.model = self.ui.comboBoxModel.currentText()
        model = self.model  # Evito tanto self. en el codigo

        # Calidad
        self.ui.comboBoxQuality.clear()
        self.ui.comboBoxQuality.addItems(self.dm[model].qualities)
        self.ui.comboBoxQuality.setCurrentText(self.dm[model].quality)

        # Tamaño
        self.ui.comboBoxSize.clear()
        self.ui.comboBoxSize.addItems(self.dm[model].sizes)
        self.ui.comboBoxSize.setCurrentText(self.dm[model].size)

        # Estilo
        self.ui.comboBoxStyle.clear()
        self.ui.comboBoxStyle.addItems(self.dm[model].styles)
        self.ui.comboBoxStyle.setCurrentText(self.dm[model].style)

        # Labels deshabilitadas si una opción no está disponible en la clase
        self.ui.labelQuality.setEnabled(self.dm[model].qualities != [])
        self.ui.labelStyle.setEnabled(self.dm[model].styles != [])
