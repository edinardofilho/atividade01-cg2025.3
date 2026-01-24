import pygame
import sys

class SetPixel:
    def __init__(self, width, height, color):
        pygame.init()
        if (width <= 800) or (height <= 600):
            width, height = 800, 600  # Tamanho mínimo da janela
        if color is None:
            color = (0, 0, 0)  # Cor padrão preta se não fornecida
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill(color)
        pygame.display.set_caption("Armazém Maluco")
        self.running = True

    def setPixel(self, x, y, color):
        if 0 <= x < self.screen.get_width() and 0 <= y < self.screen.get_height():
            self.screen.set_at((x, y), color)

    def getWidth(self):
        return self.screen.get_width()
    
    def getHeight(self):
        return self.screen.get_height()