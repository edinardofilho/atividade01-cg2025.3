from Classes.Poligono import Poligono
from Classes.Pixel import set_pixel
import pygame

class Textura(Poligono):
    def __init__(self, superficie, vertices, path, uvs):
        super().__init__(superficie, vertices)
        self._textura = pygame.image.load(path).convert()
        self._uvs = uvs

    def Scan_fill(self):
        textura = self._textura
        tex_w, tex_h = self._textura.get_width(), self._textura.get_height()
        pontos = [ (p[0] + self._centro[0], p[1] + self._centro[1]) for p in self._vertices ] 
        uvs = self._uvs
        n = len(pontos)
        ys = [p[1] for p in pontos]
        y_min = int(min(ys))
        y_max = int(max(ys))
        for y in range(y_min, y_max):
            inter = []
            for i in range(n):
                x0, y0 = pontos[i]
                x1, y1 = pontos[(i + 1) % n]
                u0, v0 = uvs[i]
                u1, v1 = uvs[(i + 1) % n]
                if y0 == y1:
                    continue
                if y0 > y1:
                    x0, y0, x1, y1 = x1, y1, x0, y0
                    u0, v0, u1, v1 = u1, v1, u0, v0
                if y < y0 or y >= y1:
                    continue
                t = (y - y0) / (y1 - y0)
                x = x0 + t * (x1 - x0)
                u = u0 + t * (u1 - u0)
                v = v0 + t * (v1 - v0)
                inter.append((x, u, v))
            inter.sort(key=lambda i: i[0])
            for i in range(0, len(inter), 2):
                if i + 1 >= len(inter):
                    continue
                x_start, u_start, v_start = inter[i]
                x_end,   u_end,   v_end   = inter[i + 1]
                if x_start == x_end:
                    continue
                for x in range(int(x_start), int(x_end) + 1):
                    t = (x - x_start) / (x_end - x_start)
                    u = u_start + t * (u_end - u_start)
                    v = v_start + t * (v_end - v_start)
                    tx = int(u * (tex_w - 1))
                    ty = int(v * (tex_h - 1))
                    if 0 <= tx < tex_w and 0 <= ty < tex_h:
                        cor = textura.get_at((tx, ty))
                        set_pixel(self._superficie, x, y, cor)
