from Classes.GameObject import GameObject
from Classes.Poligono import Poligono
from Classes.Textura import Textura
from Classes.Matriz_Operators import *

class Caixa(GameObject):
    def __init__(self, superficie, path=None):
        super().__init__()
        self._superficie = superficie
        self._vertices = [ (-20, -20), (-20, 20), (20, 20), (20, -20) ]
        self._figura = Poligono(self._superficie, self._vertices)
        if path != None:
            self._textura = Textura(self._superficie, self._vertices, path, [(0, 0), (0, 1), (1, 1), (1, 0)])
        else:
            self._textura = None

    def Update(self):
        super().Update()
        if self._textura == None:
            self._figura._centro = self._pos
        else:
            self._textura._centro = self._pos

    def Desenhar(self):
        if self._textura == None:
            self._figura.Scan_fill((255, 0, 0))
        else:
            self._textura.Scan_fill()

    def Escala(self, escala: float):
        super().Escala(escala)
        if self._textura == None:
            self._figura._vertices = [ multiplica_vetor_2(self._world, v) for v in self._figura._vertices ]
        else:
            self._textura._vertices = [ multiplica_vetor_2(self._world, v) for v in self._textura._vertices ]

    def Rotacionar_deg(self, angulo: float):
        super().Rotacionar_deg(angulo)
        if self._textura == None:
            self._figura._vertices = [ multiplica_vetor_2(self._world, v) for v in self._vertices ]
        else:
            self._textura._vertices = [ multiplica_vetor_2(self._world, v) for v in self._vertices ]
