from Poligono import Poligono

class Flood_Fill:
    def __init__(self, superficie):
        self.superficie = superficie
        self.poligono = Poligono(superficie)

    def flood_fill(self, x, y, cor_preenchimento, cor_borda):
        largura = self.poligono.largura()
        altura = self.poligono.altura()

        pilha = [(x, y)]

        while pilha:
            x, y = pilha.pop()

            if not (0 <= x < largura and 0 <= y < altura):
                continue

            cor_atual = superficie.get_at((x, y))[:3]

            if cor_atual == cor_borda or cor_atual == cor_preenchimento:
                continue

            self.poligono.set_pixel(x, y, cor_preenchimento)

            pilha.append((x + 1, y))
            pilha.append((x - 1, y))
            pilha.append((x, y + 1))
            pilha.append((x, y - 1))