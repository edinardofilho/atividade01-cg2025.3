from Classes.Poligono import Poligono
import pygame
import math

pygame.font.init()
fonte_padrao = pygame.font.SysFont(pygame.font.get_default_font(), 30)
class Botao:
    def __init__(self, superficie, pos, altura, largura, texto, contexto_resultado):
        vertices = [(pos[0] - math.floor(largura/2), pos[1] - math.floor(altura/2)),
                    (pos[0] - math.floor(largura/2), pos[1] + math.floor(altura/2)),
                    (pos[0] + math.floor(largura/2), pos[1] + math.floor(altura/2)),
                    (pos[0] + math.floor(largura/2), pos[1] - math.floor(altura/2))]
        self._superficie = superficie
        self._rect = Poligono(self._superficie, vertices)
        self._pos = pos
        self._largura = largura
        self._altura = altura
        self._res = contexto_resultado
        self._texto = fonte_padrao.render(texto, True, (255, 255, 255))

    def Desenhar(self, cor_preenchimento, cor_borda):
        self._rect.Scan_fill(cor_preenchimento)
        self._rect.Desenhar(cor_borda)
        self._superficie.blit(self._texto, (self._rect._centro[0] - math.floor(self._texto.get_width()/2), self._rect._centro[1] - math.floor(self._texto.get_height()/2)))

    def Checar_mouse(self, evento):
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if self._pos[0] - math.floor(self._largura/2) <= mouse_pos[0] <= self._pos[0] + math.floor(self._largura/2) and self._pos[1] - math.floor(self._altura/2) <= mouse_pos[1] <= self._pos[1] + math.floor(self._altura/2):
                    if self._res == None:
                        self._res = True
                    return self._res
        return None
