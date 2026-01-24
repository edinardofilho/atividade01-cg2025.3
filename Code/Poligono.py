from RetaBresenham import RetaBresenham

class Poligono:
    def __init__(self, width, height, color=None):
        self.reta_bresenham = RetaBresenham(width, height, color)

    def draw_polygon(self, vertices, color):
        num_vertices = len(vertices)
        for i in range(num_vertices):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % num_vertices]  # Conecta-se ao próximo vértice, fechando o polígono
            self.reta_bresenham.draw_line(x1, y1, x2, y2, color)