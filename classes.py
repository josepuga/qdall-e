from abc import ABC, abstractmethod
class DalleModel(ABC):
    """
    Clase base, de la cual herendan los modelos dalle2 y dalle3. Los atributos
    de clase son comunes a ambos.TODO: EXPLICAR MEJOR

    NOTA: Todas las propiedades de clase deberían ser readonly. Pero si uso @property
    no me devuelve una cadena al acceder a la propiedad, sí una ref. de objeto.
    No se cómo tratar esto en python, pero supone más código. Algo que tampoco
    tiene sentido si se sigue la pauta de no modifcar esas propiedades de clase.
    """

    model = ""
    models = ["dall-e-2", "dall-e-3"]
    qualities = []
    styles = []
    sizes = []
    n_min = 0
    n_max = 0

    def __init__(self):
        self._prompt = ""
        self._quality = ""
        self._style = ""
        self._size = ""
        self._n = 0

    @abstractmethod
    def get_params(self):
        """Crea un mapa, con los valores necesarios para llamar a OpenAI con el
        método generate
        """


    @property
    def prompt(self):
        return self._prompt

    @prompt.setter
    def prompt(self, value):
        self._prompt = value

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        self._quality = value

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, value):
        self._style = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, value):
        self._n = value


class Dalle2Model(DalleModel):
    model = "dall-e-2"
    qualities = []
    styles = []
    sizes = ["1024x1024", "512x512", "256x256"]
    n_min = 1
    n_max = 10

    def __init__(self):
        DalleModel.__init__(self)
        self._size = Dalle2Model.sizes[0]
        self._n = Dalle2Model.n_min

    def get_params(self):
        """Crea un mapa, con los valores necesarios para llamar a OpenAI con el
        método generate
        """
        return {
            "prompt": self.prompt,
            "model": self.model,
            "size": self._size,
            "n": self._n,
        }


class Dalle3Model(DalleModel):
    model = "dall-e-3"
    qualities = ["standard", "hd"]
    styles = ["natural", "vivid"]
    sizes = ["1024x1024", "1024x1792", "1792x1024"]
    n_min = 1
    n_max = 1

    def __init__(self):
        DalleModel.__init__(self)
        self._quality = Dalle3Model.qualities[0]
        self._style = Dalle3Model.styles[0]
        self._size = Dalle3Model.sizes[0]
        self._n = Dalle3Model.n_min

    def get_params(self):
        """Crea un mapa, con los valores necesarios para llamar a OpenAI con el
        método generate
        """
        return {
            "prompt": self.prompt,
            "model": self.model,
            "quality": self._quality,
            "style": self._style,
            "size": self._size,
        }
