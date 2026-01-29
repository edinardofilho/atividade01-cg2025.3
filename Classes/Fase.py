from Classes.Contexto import Contexto
from Classes.Poligono import Poligono
from Classes.Elipse import Elipse
from Classes.Caixa import Caixa
from Classes.Textura import Textura
import pygame
import copy

fonte_padrao = pygame.font.SysFont(pygame.font.get_default_font(), 30)
verde = (20, 128, 20)
vermelho = (128, 20, 20)
amarelo = (128, 128, 20)
escuro = (20, 20, 20)
class Fase(Contexto):
    def __init__(self, superficie):
        self._superficie = superficie

        esteira_vertices = [(0, 450), (600, 450), (600, 480), (0, 480)]
        self._esteira_ret = Poligono(self._superficie, esteira_vertices)
        self._esteira_ponta = Elipse(self._superficie, (600, 465), 10, 14)

        self._fundo = Textura(self._superficie, [(0, 0), (800, 0), (800, 600), (0, 600)], "fundo.png", [(0, 0), (1, 0), (1, 1), (0, 1)])
        self._fundos_alt = [Poligono(self._superficie, [(50, 0), (299, 0), (299, 600), (50, 600)]),
                            Poligono(self._superficie, [(300, 0), (549, 0), (549, 600), (300, 600)]),
                            Poligono(self._superficie, [(550, 0), (599, 0), (599, 600), (550, 600)]),
                            Poligono(self._superficie, [(600, 0), (800, 0), (800, 600), (600, 600)])] 

        self._game_speed = 3
        self._pontos = 0
        self._pontos_texto = fonte_padrao.render(str(self._pontos), True, (255, 255, 255))

        self._timer = 250
        self._timer_tick = 0

        self._caixas_hit = []
        self._caixas = []
        self.Add_caixa()

        self._janela = (50, 50, 150, 150)

        self._misses = 0
        self._misses_texto = fonte_padrao.render(str(), True, (255, 255, 255))

    def Update(self, eventos):
        self._timer_tick += 1
        self._timer = 250/(1 + self._game_speed/3)
        if self._timer_tick >= self._timer:
            self._timer_tick = 0
            self._game_speed += 0.1
            self.Add_caixa()

        novo_caixas = []
        for caixa in self._caixas:
            if caixa._pos[1] > 600 and caixa._pos[0] > 800:
                self._misses += 1
                continue    
            novo_caixas.append(caixa)
        self._caixas = novo_caixas

        novo_caixa_hit = []
        for caixa_hit in self._caixas_hit:
            if caixa_hit._pos[1] > 600 and caixa_hit._pos[0] > 800:
                continue
            novo_caixa_hit.append(caixa_hit)
        self._caixas_hit = novo_caixa_hit

        if self._misses >= 5:
            return None

        success = None
        if self._caixas:
            for evento in eventos:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        if self._caixas[0]._pos[0] < 50 or self._caixas[0]._pos[0] >= 600:
                            self._misses += 1
                            self._game_speed += 0.5
                        elif self._caixas[0]._pos[0] < 300:
                            self._pontos += 4
                            self._game_speed += 0.3
                            success = "Red"
                        elif self._caixas[0]._pos[0] < 550:
                            self._pontos += 8
                            self._game_speed += 0.2
                            success = "Yel"
                        elif self._caixas[0]._pos[0] < 600:
                            self._pontos += 16
                            self._game_speed += 0.1
                            success = "Gre"
                        caixa_hit = self._caixas.pop(0)
                        self._caixas_hit.append(caixa_hit)
                        self._caixas_hit[-1]._speed = [1, -3]
                        self._caixas_hit[-1]._accel[1] = 0.12

        self._superficie.fill((20, 20, 20))

        for caixa_hit in self._caixas_hit:
            caixa_hit.Rotacionar_deg(1)
            caixa_hit.Escala(0.99)
            caixa_hit.Update()
            caixa_hit.Desenhar()

        #self._fundo.Scan_fill()
        self._fundos_alt[0].Desenhar(vermelho)
        self._fundos_alt[1].Desenhar(amarelo)
        self._fundos_alt[2].Desenhar(verde)
        self._fundos_alt[3].Desenhar(escuro)
        match success:
            case "Red":
                self._fundos_alt[0].Scan_fill(vermelho)
            case "Yel":
                self._fundos_alt[1].Scan_fill(amarelo)
            case "Gre":
                self._fundos_alt[2].Scan_fill(verde)
            case _:
                pass

        self._pontos_texto = fonte_padrao.render("Pontos: " + str(self._pontos), True, (255, 255, 255))
        self._superficie.blit(self._pontos_texto, (650, 75))
        self._misses_texto = fonte_padrao.render("".join(["x" for _ in range(5)]), True, (80, 80, 80))
        self._superficie.blit(self._misses_texto, (650, 100))
        self._misses_texto = fonte_padrao.render("".join(["x" for _ in range(self._misses)]), True, (255, 20, 30))
        self._superficie.blit(self._misses_texto, (650, 100))

        self.Desenhar_esteira()
        for caixa in self._caixas:
            if caixa._pos[0] > 600:
                caixa._accel[1] = 0.12
                caixa.Rotacionar_deg(1)
            caixa.Update()
            caixa.Desenhar()

        if self._caixas:
            caixa_zoom = Caixa(self._superficie)
            caixa_zoom._world = copy.deepcopy(self._caixas[0]._world)
            caixa_zoom._pos = [ 100, 100 ]
            caixa_zoom.Escala(0.8)
            caixa_zoom._figura.Desenhar_recortado(self._janela, (255, 255, 255))

        return self

    def Desenhar_esteira(self):
        cinza = (80, 80, 80)
        self._esteira_ret.Scan_fill(cinza)
        self._esteira_ponta.Scan_fill(cinza)

    def Add_caixa(self):
        caixa = Caixa(self._superficie, "box.png")
        caixa._speed = [self._game_speed, 0]
        caixa._pos = [-10, 440]
        self._caixas.append(caixa)
