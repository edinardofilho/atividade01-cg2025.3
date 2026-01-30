import pygame
import sys

class Context_Window:
    def __init__(self, contexto_inicial):
        self._pilha_contexto = [ contexto_inicial ]

    def Update(self, eventos):
        contexto = self._pilha_contexto[-1]
        novo_contexto = contexto.Update(eventos)
        if novo_contexto == None:
            self._pilha_contexto.pop()
        elif novo_contexto == contexto:
            pass
        else:
            self._pilha_contexto.append(novo_contexto)
        if not self._pilha_contexto:
            pygame.quit()
            sys.exit()
        return self