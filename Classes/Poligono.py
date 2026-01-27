from Classes.Reta_Bresenham import Reta_Bresenham
from Classes.Figura import Figura

class Poligono(Figura):
    def __init__(self, superficie, vertices):
        super().__init__(superficie)
        self._vertices = vertices

    def Desenhar(self, cor):
        num_vertices = len(self._vertices)
        for i in range(num_vertices):
            x0, y0 = self._vertices[i]
            x1, y1 = self._vertices[(i + 1) % num_vertices]
            Reta_Bresenham(self._superficie, x0, y0, x1, y1).Desenhar_reta(cor)
