import pygame
import sys
from Classes.Tela_Abertura import Tela_Abertura
from Classes.Fase import Fase
from Classes.Context_Window import Context_Window
sys.setrecursionlimit(10**7)

pygame.init()
largura, altura = 800, 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("ZLog Ltda")
clock = pygame.time.Clock()
FPS = 60

contexto = Context_Window(Tela_Abertura(tela))
rodando = True

while rodando:
    #for evento in pygame.event.get():
    #    if evento.type == pygame.QUIT:
    #        rodando = False
        
    #tela.fill(azul_claro) # Preenche a tela com azul claro

    contexto.Update(pygame.event.get())
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
