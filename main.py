import pygame
import sys
from import FloodFill
sys.setrecursionlimit(10**7)

pygame.init()
largura, altura = 500, 400
preto, branco, azul, vermelho, verde = (0, 0, 0), (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Algoritmo Flood Fill")

tela_abertura = FloodFill(tela)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
    tela.fill(branco) # Preenche a tela com branco

    tela_abertura.desenhar_poligono([(100, 100), (400, 100), (400, 300), (100, 300)], preto) # Desenha um retângulo preto

    tela_abertura.flood_fill(250, 200, azul, preto) # Preenche o retângulo com azul

    pygame.display.flip()

pygame.quit()
sys.exit()