import pygame
import sys
from RetaBresenham import RetaBresenham

largura, altura = 800, 600

def desenha_linha(x1, y1, x2, y2, cor):
    reta = RetaBresenham(largura, altura)
    reta.draw_line(x1, y1, x2, y2, cor)

vermelho = (255, 0, 0)
desenha_linha(100, 100, 200, 200, vermelho)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
pygame.quit()
sys.exit()

