from Classes.Matriz_Operators import *
import math

class GameObject:
    def __init__(self):
        self._world = matriz_identidade_2()
        self._pos = [0, 0]
        self._speed = [0, 0]
        self._accel = [0, 0]

    def Update(self):
        self._speed[0] += self._accel[0]
        self._speed[1] += self._accel[1]
        self._pos[0] += self._speed[0]
        self._pos[1] += self._speed[1]

    def Escala(self, escala: float):
        m_escala = [[escala, 0],
                    [0, escala]]
        self._world = multiplica_matrizes_2(m_escala, self._world)

    def Transladar(self, x: float, y: float):
        self._pos[0] += x
        self._pos[1] += y

    def Rotacionar_deg(self, angulo: float):
        rad = math.radians(angulo)
        c = math.cos(rad)
        s = math.sin(rad)
        m_rotacao = [[c, -s],
                     [s, c]]
        self._world = multiplica_matrizes_2(m_rotacao, self._world)
