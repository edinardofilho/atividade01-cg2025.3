from Classes.Contexto import Contexto
from Classes.Poligono import Poligono
from Classes.Circulo import Circulo
from Classes.GameObject import GameObject

class Fase(Contexto):
    def __init__(self, superficie):
        self._superficie = superficie

        esteira_vertices = [(0, 550), (700, 550), (700, 580), (0, 580)]
        self._esteira_ret = Poligono(self._superficie, esteira_vertices)
        self._esteira_ponta = Circulo(self._superficie, (700, 565), 14)

    def Update(self, eventos):
        self.Desenhar_esteira()
        return self

    def Desenhar_esteira(self):
        self._esteira_ret.Scan_fill((10, 10, 10))
        self._esteira_ponta.Scan_fill((10, 10, 10))
