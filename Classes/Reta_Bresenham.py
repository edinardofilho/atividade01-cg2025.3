from Classes.Pixel import set_pixel

class Reta_Bresenham:
    def __init__(self, superficie, x0, y0, x1, y1):
        self._superficie = superficie
        self._x0 = x0
        self._y0 = y0
        self._x1 = x1
        self._y1 = y1

    def Desenhar_reta(self, cor):
        x0, x1, y0, y1 = self._x0, self._x1, self._y0, self._y1
        steep = abs(y1 - y0) > abs(x1 - x0)
        if steep:
            x0, y0 = y0, x0
            x1, y1 = y1, x1
        if x0 > x1:
            x0, x1 = x1, x0
            y0, y1 = y1, y0
        dx = x1 - x0
        dy = y1 - y0
        ystep = 1
        if dy < 0:
            ystep = -1
            dy = -dy
        d = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)
        x = x0
        y = y0
        while x <= x1:
            if steep:
                set_pixel(self._superficie, y, x, cor)
            else:
                set_pixel(self._superficie, x, y, cor)
            if d <= 0:
                d += incE
            else:
                d += incNE
                y += ystep
            x += 1
