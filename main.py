import pygame
import sys
from Classes.Flood_Fill import Flood_Fill
from Classes.Textos import Textos
sys.setrecursionlimit(10**7)

pygame.init()
largura, altura = 800, 600
cor_fundo = (100, 149, 237)  # Azul claro
cor_preenchimento = (47, 79, 79)  #Cinza escuro
cor_borda = (72, 209, 204)  # Turquesa
poligono_caixa = [(100, 100), (400, 100), (400, 300), (100, 300)]

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("ZLog Ltda")

tela_abertura = Flood_Fill(tela)
palavra_z = Textos(tela)

rodando = True

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        
    tela.fill(cor_fundo) # Preenche a tela com azul claro

    tela_abertura.desenhar_poligono(poligono_caixa, cor_borda) # Desenha o retângulo da caixa
    tela_abertura.flood_fill(250, 200, cor_preenchimento, cor_borda) # Preenche o retângulo com cinza escuro

    palavra_z.desenhar_z(cor_preenchimento, cor_borda)  # Desenha o "Z" no centro da tela

    pygame.display.flip()

pygame.quit()
sys.exit()