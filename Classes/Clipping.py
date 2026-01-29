from Classes.Reta_Bresenham import Reta_Bresenham

class Clipping:
    def __init__(self):
        pass

def clipping_linha(self, x0, y0, x1, y1, xmin, ymin, xmax, ymax): #Algoritmo de Cohen-Sutherland
        c0 = self.codigo_regiao(x0, y0, xmin, ymin, xmax, ymax)
        c1 = self.codigo_regiao(x1, y1, xmin, ymin, xmax, ymax)

        while True:
            if not (c0 | c1):
                return True, x0, y0, x1, y1  # Totalmente interno

            if c0 & c1:
                return False, None, None, None, None  # Totalmente externo

            c_out = c0 if c0 else c1

            if c_out & 8:
                x = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                y = ymin
            elif c_out & 4:
                x = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                y = ymax
            elif c_out & 2:
                y = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                x = xmax
            elif c_out & 1:
                y = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                x = xmin

            if c_out == c0:
                x0, y0 = x, y
                c0 = self.codigo_regiao(x0, y0, xmin, ymin, xmax, ymax)
            else:
                x1, y1 = x, y
                c1 = self.codigo_regiao(x1, y1, xmin, ymin, xmax, ymax)

def clipping_poligono(superficie, pontos, janela, cor): #Algoritmo de Sutherland-Hodgman
    xmin, ymin, xmax, ymax = janela
    n = len(pontos)

    for i in range(n):
        x0, y0 = pontos[i]
        x1, y1 = pontos[(i + 1) % n]

        visivel, rx0, ry0, rx1, ry1 = clipping_linha(
            x0, y0, x1, y1, xmin, ymin, xmax, ymax
        )

        if visivel:
            reta = Reta_Bresenham(superficie, int(rx0), int(ry0), int(rx1), int(ry1))
            reta.Desenhar_reta(cor)

def codigo_regiao(x, y, xmin, ymin, xmax, ymax):
    codigo = 0 #Interior
    if x < xmin:
        codigo |= 1 #Esquerda
    elif x > xmax:
        codigo |= 2 #Direita
    if y < ymin:
        codigo |= 4 #Acima
    elif y > ymax:
        codigo |= 8 #Abaixo
    return codigo