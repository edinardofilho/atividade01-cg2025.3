class Figura:
    def __init__(self, superficie, centro):
        self._superficie = superficie
        self._centro = centro

    def Altura(self):
        return self._superficie.get_height()

    def Largura(self):
        return self._superficie.get_width()
