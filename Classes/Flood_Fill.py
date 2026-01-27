from Classes.Figura import Figura
from Classes.Pixel import set_pixel

def flood_fill(figura: Figura, x, y, cor_preenchimento, cor_borda):
    largura = figura.Largura()
    altura = figura.Altura()

    pilha = [(x, y)]

    while pilha:
        x, y = pilha.pop()

        if not (0 <= x < largura and 0 <= y < altura):
            continue

        cor_atual = figura._superficie.get_at((x, y))[:3]

        if cor_atual == cor_borda or cor_atual == cor_preenchimento:
            continue

        set_pixel(figura._superficie, x, y, cor_preenchimento)

        pilha.append((x + 1, y))
        pilha.append((x - 1, y))
        pilha.append((x, y + 1))
        pilha.append((x, y - 1))
