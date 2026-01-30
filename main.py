import pygame
import sys
from Classes.Tela_Abertura import Tela_Abertura
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
    contexto.Update(pygame.event.get())
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
