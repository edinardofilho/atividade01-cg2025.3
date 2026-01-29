from Classes.Reta_Bresenham import Reta_Bresenham
from Classes.Figura import Figura
from Classes.Pixel import set_pixel

class Circulo(Figura):
    def __init__(self, superficie, centro, raio):
        super().__init__(superficie, centro)
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

    def Scan_fill(self, cor):
        x = 0
        y = self._raio
        d = 1 - self._raio
        xc, yc = self._centro
        while x < y:
            self.Scan_fill_simetrico(xc, yc, x, y, cor)
            x += 1
            if d < 0:
                d = d + 2 * x + 3
            else:
                y -= 1
                d = d + 2 * (x - y) + 5

    def Scan_fill_simetrico(self, xc, yc, x, y, cor):
        pontos = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        Reta_Bresenham(self._superficie, pontos[0][0], pontos[0][1], pontos[1][0], pontos[1][1]).Desenhar_reta(cor)
        Reta_Bresenham(self._superficie, pontos[2][0], pontos[2][1], pontos[3][0], pontos[3][1]).Desenhar_reta(cor)
        Reta_Bresenham(self._superficie, pontos[4][0], pontos[4][1], pontos[5][0], pontos[5][1]).Desenhar_reta(cor)
        Reta_Bresenham(self._superficie, pontos[6][0], pontos[6][1], pontos[7][0], pontos[7][1]).Desenhar_reta(cor)
