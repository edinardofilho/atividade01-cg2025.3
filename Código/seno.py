import pygame
import sys
import math
from SetPixel import SetPixel

tela = SetPixel(800, 600, (0, 0, 0))  # Fundo preto 

def desenha_seno(superficie, cor):
    amplitude = superficie.getHeight() // 4
    centro = superficie.getHeight() // 2
    frequencia = 2*math.pi / superficie.getWidth()

    for x in range(superficie.getWidth()):
        y = centro - int(amplitude * math.sin(frequencia * x))

        SetPixel.setPixel(superficie, x, y, cor)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    vermelho = (255, 0, 0)
    desenha_seno(tela, vermelho)

    pygame.display.flip()

pygame.quit()
sys.exit()

