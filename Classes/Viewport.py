from Classes.Matriz_Operators import *
from Classes.GameObject import *

class Viewport:
    def __init__(self, janela, viewport):
        self.janela = janela
        self.viewport = viewport

def janela_viewport(self):
        Jxmin, Jymin, Jxmax, Jymax = self.janela
        Vxmin, Vymin, Vxmax, Vymax = self.viewport

        sx = (Vxmax - Vxmin) / (Jxmax - Jxmin)
        sy = (Vymin - Vymax) / (Jymax - Jymin)  # <-- INVERTE O Y

        m = matriz_identidade() #Inicia matriz
        
        m = multiplica_matrizes(GameObject.Transladar(-Jxmin, -Jymin), m) # Translada janela para origem

        m = multiplica_matrizes(GameObject.Escala(sx, sy), m)

        m = multiplica_matrizes(GameObject.Transladar(Vxmin, Vymax), m) # Ajusta o Y para o sistema do Pygame

        return m