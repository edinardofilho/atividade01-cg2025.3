from Reta_Bresenham import Reta_Bresenham
class Poligono:
    def __init__(self, superficie):
        self.superficie = superficie
        self.reta_bresenham = Reta_Bresenham(superficie)

    def desenhar_poligono(self, vertices, cor):
        num_vertices = len(vertices)
        
        for i in range(num_vertices):
            x0, y0 = vertices[i]
            x1, y1 = vertices[(i + 1) % num_vertices]
            
            self.reta_bresenham.reta_bresenham(x0, y0, x1, y1, cor)

    def vertices(self):
        return self.vertices
    
    def set_pixel(self, x, y, cor):
        Reta_Bresenham(self.superficie).set_pixel(x, y, cor)

    def get_pixel(self, x, y):
        return Reta_Bresenham(self.superficie).get_pixel(x, y)

    def largura(self):
        return Reta_Bresenham(self.superficie).largura()

    def altura(self):
        return Reta_Bresenham(self.superficie).altura()    