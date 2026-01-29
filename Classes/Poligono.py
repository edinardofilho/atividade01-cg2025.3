from Classes.Reta_Bresenham import Reta_Bresenham
from Classes.Figura import Figura
from Classes.Clipping import clipping_linha
from Classes.Pixel import set_pixel
import math

class Poligono(Figura):
    def __init__(self, superficie, vertices):
        len_vert = len(vertices)
        centro = (math.floor(sum(v[0] for v in vertices)/len_vert), math.floor(sum(v[1] for v in vertices)/len_vert))
        super().__init__(superficie, centro)
        self._vertices = [ (v[0] - centro[0], v[1] - centro[1]) for v in vertices ]

    def Desenhar(self, cor):
        num_vertices = len(self._vertices)
        for i in range(num_vertices):
            x0, y0 = (self._vertices[i][0] + self._centro[0], self._vertices[i][1] + self._centro[1])
            x1, y1 = (self._vertices[(i + 1) % num_vertices][0] + self._centro[0], self._vertices[(i + 1) % num_vertices][1] + self._centro[1])
            Reta_Bresenham(self._superficie, math.floor(x0), math.floor(y0), math.floor(x1), math.floor(y1)).Desenhar_reta(cor)

    def Scan_fill(self, cor):
        n = len(self._vertices)
        pontos = [ (math.floor(v[0] + self._centro[0]), math.floor(v[1] + self._centro[1])) for v in self._vertices ]
        ys = [p[1] for p in pontos]
        y_min = min(ys)
        y_max = max(ys)
        for y in range(y_min, y_max):
            intersecoes_x = []
            for i in range(n):
                x0, y0 = pontos[i]
                x1, y1 = pontos[(i + 1) % n]
                if y0 == y1:
                    continue
                if y0 > y1:
                    x0, y0, x1, y1 = x1, y1, x0, y0
                if y < y0 or y >= y1:
                    continue
                x = x0 + (y - y0) * (x1 - x0) / (y1 - y0)
                intersecoes_x.append(x)
            intersecoes_x.sort()
            for i in range(0, len(intersecoes_x), 2):
                if i + 1 < len(intersecoes_x):
                    x_inicio = int(round(intersecoes_x[i]))
                    x_fim = int(round(intersecoes_x[i + 1]))
                    for x in range(x_inicio, x_fim + 1):
                        set_pixel(self._superficie, x, y, cor)

    def Desenhar_recortado(self, janela, cor):
        pontos = [ (math.floor(v[0] + self._centro[0]), math.floor(v[1] + self._centro[1])) for v in self._vertices ]
        xmin, ymin, xmax, ymax = janela
        n = len(pontos)

        for i in range(n):
            x0, y0 = pontos[i]
            x1, y1 = pontos[(i + 1) % n]

            visivel, rx0, ry0, rx1, ry1 = clipping_linha(
                self._superficie, x0, y0, x1, y1, xmin, ymin, xmax, ymax
            )

            if visivel:
                Reta_Bresenham(self._superficie, int(rx0), int(ry0), int(rx1), int(ry1)).Desenhar_reta(cor)
