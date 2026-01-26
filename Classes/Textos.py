from Classes.Poligono import Poligono
from Classes.Flood_Fill import Flood_Fill

class Textos:
    def __init__(self, superficie):
        self.superficie = superficie
        self.poligono = Poligono(superficie)

    def desenhar_z(self, cor_preenchimento, cor_borda):
        x0, x1 = 150, 350
        y0, y1 = 200, 400
        vertices_z = [(x0, y0), (x0, y1), ((x0 + 50),y1), ((x1 - 50), (y0 + 50)), 
                      ((x1 - 50), y1), (x1, y1), (x1, y0), ((x1 - 50), y0), 
                      ((x0 + 50), (y1 - 50)), ((x0 + 50), y0)]
        self.poligono.desenhar_poligono(vertices_z, cor_borda)
        self.poligono.flood_fill(250, 250, cor_preenchimento, cor_borda)  # Atualiza o polígono atual
        return self.poligono

    def desenhar_poligono(self, vertices, cor):
        self.poligono.desenhar_poligono(vertices, cor)

    def largura(self):
        return self.poligono.largura()

    def altura(self):
        return self.poligono.altura()