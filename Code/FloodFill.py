from Poligono import Poligono

class FloodFill:
    def __init__(self, width, height, color=None):
        self.poligono = Poligono(width, height, color)

    def flood_fill(self, x, y, target_color, replacement_color):
        if target_color == replacement_color:
            return

        pixel_color = self.get_pixel_color(x, y)
        if pixel_color != target_color:
            return

        self.set_pixel_color(x, y, replacement_color)

        self.flood_fill(x + 1, y, target_color, replacement_color)  # Right
        self.flood_fill(x - 1, y, target_color, replacement_color)  # Left
        self.flood_fill(x, y + 1, target_color, replacement_color)  # Down
        self.flood_fill(x, y - 1, target_color, replacement_color)  # Up

    def get_pixel_color(self, x, y):
        # Placeholder for getting the color of the pixel at (x, y)
        pass

    def set_pixel_color(self, x, y, color):
        # Placeholder for setting the color of the pixel at (x, y)
        pass