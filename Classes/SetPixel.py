class SetPixel:
    def __init__(self, superficie):
        self.superficie = superficie

    def set_pixel(self, x, y, cor):
        if 0 <= x < self.superficie.get_width() and 0 <= y < self.superficie.get_height():
            self.superficie.set_at((x, y), cor)
        else:
            raise ValueError("Coordenadas fora dos limites da superfície.")
        
    def get_pixel(self, x, y):
        if 0 <= x < self.superficie.get_width() and 0 <= y < self.superficie.get_height():
            return self.superficie.get_at((x, y))
        else:
            raise ValueError("Coordenadas fora dos limites da superfície.")
        
    def largura(self):
        return self.superficie.get_width()

    def altura(self):
        return self.superficie.get_height()