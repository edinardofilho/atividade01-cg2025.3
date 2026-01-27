from Classes.Figura import Figura
from Classes.Pixel import set_pixel

class Circulo(Figura):
    def __init__(self, superficie, centro, raio):
        super().__init__(superficie)
        self._centro = centro
        self._raio = raio

    def Desenhar(self, cor):
        x = 0
        y = self._raio
        d = 1 - self._raio
        xc, yc = self._centro
        self.Desenhar_simetrico(xc, yc, x, y, cor)
        while x < y:
            x += 1
            if d < 0:
                d = d + 2 * x + 3
            else:
                y -= 1
                d = d + 2 * (x - y) + 5
            self.Desenhar_simetrico(xc, yc, x, y, cor)

    def Desenhar_simetrico(self, xc, yc, x, y, cor):
        pontos = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]

        for px, py in pontos:
            set_pixel(self._superficie, px, py, cor)
