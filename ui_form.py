# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)
import rc_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(663, 803)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelYourApiKey = QLabel(self.centralwidget)
        self.labelYourApiKey.setObjectName(u"labelYourApiKey")
        self.labelYourApiKey.setGeometry(QRect(480, 660, 51, 18))
        self.labelApiKey = QLabel(self.centralwidget)
        self.labelApiKey.setObjectName(u"labelApiKey")
        self.labelApiKey.setGeometry(QRect(540, 660, 111, 18))
        self.labelTextToSend = QLabel(self.centralwidget)
        self.labelTextToSend.setObjectName(u"labelTextToSend")
        self.labelTextToSend.setGeometry(QRect(190, 660, 101, 18))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 660, 171, 131))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBoxStyle = QComboBox(self.gridLayoutWidget)
        self.comboBoxStyle.setObjectName(u"comboBoxStyle")

        self.gridLayout.addWidget(self.comboBoxStyle, 3, 1, 1, 1)

        self.comboBoxModel = QComboBox(self.gridLayoutWidget)
        self.comboBoxModel.setObjectName(u"comboBoxModel")

        self.gridLayout.addWidget(self.comboBoxModel, 0, 1, 1, 1)

        self.labelSize = QLabel(self.gridLayoutWidget)
        self.labelSize.setObjectName(u"labelSize")

        self.gridLayout.addWidget(self.labelSize, 1, 0, 1, 1)

        self.labelModel = QLabel(self.gridLayoutWidget)
        self.labelModel.setObjectName(u"labelModel")

        self.gridLayout.addWidget(self.labelModel, 0, 0, 1, 1)

        self.comboBoxSize = QComboBox(self.gridLayoutWidget)
        self.comboBoxSize.setObjectName(u"comboBoxSize")

        self.gridLayout.addWidget(self.comboBoxSize, 1, 1, 1, 1)

        self.comboBoxQuality = QComboBox(self.gridLayoutWidget)
        self.comboBoxQuality.setObjectName(u"comboBoxQuality")

        self.gridLayout.addWidget(self.comboBoxQuality, 2, 1, 1, 1)

        self.labelQuality = QLabel(self.gridLayoutWidget)
        self.labelQuality.setObjectName(u"labelQuality")

        self.gridLayout.addWidget(self.labelQuality, 2, 0, 1, 1)

        self.labelStyle = QLabel(self.gridLayoutWidget)
        self.labelStyle.setObjectName(u"labelStyle")

        self.gridLayout.addWidget(self.labelStyle, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(190, 690, 331, 91))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(540, 690, 111, 98))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButtonSaveAs = QPushButton(self.verticalLayoutWidget)
        self.pushButtonSaveAs.setObjectName(u"pushButtonSaveAs")

        self.verticalLayout.addWidget(self.pushButtonSaveAs)

        self.pushButtonSendText = QPushButton(self.verticalLayoutWidget)
        self.pushButtonSendText.setObjectName(u"pushButtonSendText")

        self.verticalLayout.addWidget(self.pushButtonSendText)

        self.pushButtonApiKey = QPushButton(self.verticalLayoutWidget)
        self.pushButtonApiKey.setObjectName(u"pushButtonApiKey")

        self.verticalLayout.addWidget(self.pushButtonApiKey)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 642, 642))
        self.horizontalLayoutImage = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutImage.setObjectName(u"horizontalLayoutImage")
        self.horizontalLayoutImage.setContentsMargins(0, 0, 0, 0)
        self.labelImage = QLabel(self.horizontalLayoutWidget)
        self.labelImage.setObjectName(u"labelImage")
        self.labelImage.setMaximumSize(QSize(640, 640))
        self.labelImage.setPixmap(QPixmap(u":/assets/default-screen.png"))
        self.labelImage.setAlignment(Qt.AlignCenter)

        self.horizontalLayoutImage.addWidget(self.labelImage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 663, 23))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelYourApiKey.setText(QCoreApplication.translate("MainWindow", u"API Key:", None))
        self.labelApiKey.setText("")
        self.labelTextToSend.setText(QCoreApplication.translate("MainWindow", u"Text to send:", None))
        self.labelSize.setText(QCoreApplication.translate("MainWindow", u"Size:", None))
        self.labelModel.setText(QCoreApplication.translate("MainWindow", u"Model:", None))
        self.labelQuality.setText(QCoreApplication.translate("MainWindow", u"Quality:", None))
        self.labelStyle.setText(QCoreApplication.translate("MainWindow", u"Style:", None))
        self.pushButtonSaveAs.setText(QCoreApplication.translate("MainWindow", u"Save &as..", None))
        self.pushButtonSendText.setText(QCoreApplication.translate("MainWindow", u"&Send", None))
        self.pushButtonApiKey.setText(QCoreApplication.translate("MainWindow", u"Change API &Key", None))
        self.labelImage.setText("")
    # retranslateUi

