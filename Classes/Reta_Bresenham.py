from SetPixel import SetPixel
class Reta_Bresenham:
    def __init__(self, superficie):
        self.superficie = superficie

def reta_bresenham(x0, y0, x1, y1, cor):
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
            self.set_pixel.set_pixel(y, x, cor)
        else:
            self.set_pixel.set_pixel(x, y, cor)

        if d <= 0:
            d += incE
        else:
            d += incNE
            y += ystep

        x += 1

def set_pixel(self, x, y, cor):
    SetPixel(self.superficie).set_pixel(x, y, cor)

def get_pixel(self, x, y):
    return SetPixel(self.superficie).get_pixel(x, y)

def largura(self):
    return SetPixel(self.superficie).largura()

def altura(self):
    return SetPixel(self.superficie).altura()