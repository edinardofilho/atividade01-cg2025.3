class Figura:
    def __init__(self, superficie):
        self._superficie = superficie

    def Altura(self):
        return self._superficie.get_height()

    def Largura(self):
        return self._superficie.get_width()
