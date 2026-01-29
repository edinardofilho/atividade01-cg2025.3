from Classes.Matriz_Operators import *
import math

class GameObject:
    def __init__(self):
        self._pos = [0, 0]
        self._world = m_identidade()

    def Update(self):
        pass

    def Escala(escala: float):
        m_escala = [[escala, 0],
                    [0, escala]]
        self._world = m_mul(m_escala, self._world)

    def Transladar(x: float, y: float):
        self._pos[0] += x
        self._pos[1] += y

    def Rotacionar_deg(self, angulo: float):
        rad = math.radians(angulo)
        c = math.cos(rad)
        s = math.sin(rad)
        m_rotacao = [[c, -s],
                     [s, c]]
        self._world = m_mul(m_rotacao, self._world)

    def Get_pos():
        return (round(pos[0]), round(pos[1]))
