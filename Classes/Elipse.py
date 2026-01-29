from Classes.Figura import Figura
from Classes.Pixel import set_pixel

class Elipse(Figura):
    def __init__(self, superficie, centro, semi_eixo_x, semi_eixo_y):
        super().__init__(superficie, centro)
        self._semi_eixo_x = semi_eixo_x
        self._semi_eixo_y = semi_eixo_y

    def Desenhar(self, cor):
        xc, yc = self._centro
        rx, ry = self._semi_eixo_x, self._semi_eixo_y
        x = 0
        y = ry
        rx2 = rx * rx
        ry2 = ry * ry
        dx_val = 2 * ry2 * x
        dy_val = 2 * rx2 * y
        p1 = ry2 - (rx2 * ry) + (0.25 * rx2)
        while dx_val < dy_val:
            self.Desenhar_simetrico(xc, yc, x, y, cor)
            x += 1
            dx_val += 2 * ry2
            if p1 < 0:
                p1 += ry2 + dx_val # dx_val já foi incrementado
            else:
                y -= 1
                dy_val -= 2 * rx2
                p1 += ry2 + dx_val - dy_val
        p2 = (ry2 * (x + 0.5)**2) + (rx2 * (y - 1)**2) - (rx2 * ry2)
        while y >= 0:
            self.Desenhar_simetrico(xc, yc, x, y, cor)
            y -= 1
            dy_val -= 2 * rx2
            if p2 > 0:
                p2 += rx2 - dy_val # Note o sinal: estamos descendo
            else:
                x += 1
                dx_val += 2 * ry2
                p2 += rx2 - dy_val + dx_val

    def Desenhar_simetrico(self, xc, yc, x, y, cor):
        pontos = [
            (xc + x, yc + y), 
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y)
        ]

        for px, py in pontos:
            set_pixel(self._superficie, px, py, cor)
