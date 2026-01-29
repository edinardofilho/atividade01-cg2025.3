from Classes.Contexto import Contexto
from Classes.Circulo import Circulo
from Classes.Elipse import Elipse
from Classes.Poligono import Poligono
from Classes.Botao import Botao
from Classes.Fase import Fase
from Classes.Boundary_Fill import boundary_fill
import math

vertices_caixa_z = [(100, 100), (400, 100), (400, 500), (100, 500)]
vertices_caixa_log = [(400, 100), (700, 100), (700, 500), (400, 500)]

circulo_centro = (700, 100)
circulo_raio = 50

botao_pos = (550, 500)
botao_lar = 150
botao_alt = 50

cinza_escuro = (47, 79, 79)    
turquesa = (72, 209, 204)
branco_azulado = (240, 248, 255) 
branco = (255, 255, 255)
azul_teal = (0, 128, 128)
azul_claro = (100, 149, 237)
branco_trigo = (245, 222, 179)
blanque = (255, 250, 240)
amarelo = (224, 172, 27)
laranja = (254, 132, 27)
preto = (0, 0, 0)

class Tela_Abertura(Contexto):
    def __init__(self, superficie):
        self._superficie = superficie
        self._start = Botao(self._superficie, botao_pos, botao_alt, botao_lar, "Começar", Fase(self._superficie))

    def Update(self, eventos):
        for evento in eventos:
            botao_status = self._start.Checar_mouse(evento)
            if botao_status == None:
                continue
            else:
                self._start = Botao(self._superficie, botao_pos, botao_alt, botao_lar, "Recomeçar", Fase(self._superficie))
                return botao_status

        self._superficie.fill(azul_claro)
        self.Desenhar_circulo(Circulo(self._superficie, circulo_centro, circulo_raio), amarelo, branco)
        self.Desenhar_caixa(Poligono(self._superficie, vertices_caixa_z), cinza_escuro, turquesa)
        self.Desenhar_z(branco_azulado, blanque)
        self.Desenhar_caixa(Poligono(self._superficie, vertices_caixa_log), azul_teal, turquesa)
        self.Desenhar_log(branco_trigo, branco)
        self.Desenhar_ltda(branco_trigo, branco)
        self._start.Desenhar(laranja, preto)

        return self

    def Desenhar_circulo(self, circulo, cor_preenchimento, cor_borda):
        circulo.Desenhar(cor_borda)
        boundary_fill(self._superficie, circulo._centro[0], circulo._centro[1], cor_preenchimento, cor_borda)

    def Desenhar_elipse(self, elipse, cor_preenchimento, cor_borda):
        elipse.Desenhar(cor_borda)
        boundary_fill(self._superficie, elipse._centro[0], elipse._centro[1], cor_preenchimento, cor_borda)

    def Desenhar_caixa(self, poligono, cor_preenchimento, cor_borda):
        poligono.Desenhar(cor_borda)
        boundary_fill(self._superficie, poligono._centro[0], poligono._centro[1], cor_preenchimento, cor_borda)

    def Desenhar_z(self, cor_preenchimento, cor_borda):
        x0, x1 = 200, 400
        y0, y1 = 200, 400
        vertices_z = [(x0, y0), (x1, y0), (x1, y0 + 50), (x0 + 50, y1 - 50),
                      (x1, y1 - 50), (x1, y1), (x0, y1), (x0, y1 - 50),
                      (x1 - 50, y0 + 50), (x0, y0 + 50)]
        z = Poligono(self._superficie, vertices_z)
        z.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
    
    def Desenhar_log(self, cor_preenchimento, cor_borda):
        x0, x1 = 400, 450
        y0, y1 = 200, 250
        vertices_l = [(x0, y0), (x0, y1), (x1, y1), (x1, y1 - 10),
                      (x0 + 10, y1 - 10), (x0 + 10, y0)]
        l = Poligono(self._superficie, vertices_l)
        l.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
        
        x0, x1 = x0 + 70, x1 + 70
        o_centro = (math.floor((x0+x1)/2), math.floor((y0+y1)/2))
        o_ext = Circulo(self._superficie, o_centro, math.floor((x1 - x0)/2))
        o_ext.Desenhar(cor_borda)
        boundary_fill(self._superficie, o_ext._centro[0], o_ext._centro[1], cor_preenchimento, cor_borda)

        o_int = Circulo(self._superficie, o_centro, math.floor((x1 - x0 - 20)/2))
        o_int.Desenhar(cor_borda)
        boundary_fill(self._superficie, o_int._centro[0], o_int._centro[1], azul_teal, cor_borda)

        x0, x1 = x0 + 70, x1 + 70
        vertices_g = [(x0, y0), (x1, y0), (x1, y0 + 10), (x0 + 10, y0 + 10),
                      (x0 + 10, y1 - 10), (x1 - 10, y1 - 10), (x1 - 10, y1 - 20),
                      (x1 - 20, y1 - 20), (x1 - 20, y1 - 30), (x1, y1 - 30),
                      (x1, y1), (x0, y1)]
        g = Poligono(self._superficie, vertices_g)
        g.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
    
    def Desenhar_ltda(self, cor_preenchimento, cor_borda):
        x0, x1 = 400, 450
        y0, y1 = 350, 400
        vertices_l = [(x0, y0), (x0, y1), (x1, y1), (x1, y1 - 10),
                      (x0 + 10, y1 - 10), (x0 + 10, y0)]
        
        l = Poligono(self._superficie, vertices_l)
        l.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
        
        x0, x1 = x0 + 70, x1 + 70
        vertices_t = [(x0, y0), (x1, y0), (x1, y0 + 10), (x1 - 20, y0 + 10),
                      (x1 - 20, y1), (x1 - 30, y1), (x1 - 30, y0 + 10),
                      (x0, y0 + 10)]
        
        t = Poligono(self._superficie, vertices_t)
        t.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
        
        x0, x1 = x0 + 70, x1 + 70
        vertices_d_ext = [(x0, y0), (x1 - 20, y0), (x1, y0 + 15), 
                          (x1, y1 - 15), (x1 - 20, y1), (x0, y1)]
        vertices_d_int = [(x0 + 10, y0 + 10), (x1 - 25, y0 + 10),
                          (x1 - 10, y0 + 20), (x1 - 10, y1 - 20), (x1 - 25, y1 - 10),
                          (x0 + 10, y1 - 10)]

        d_ext = Poligono(self._superficie, vertices_d_ext)
        d_ext.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 5, y0 + 5, cor_preenchimento, cor_borda)

        d_int = Poligono(self._superficie, vertices_d_int)
        d_int.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 15, y0 + 15, azul_teal, cor_borda)

        x0, x1 = x0 + 70, x1 + 70
        vertices_a_ext = [(x1, y1), (x1 - 20, y0), (x0 + 20, y0),
                            (x0, y1), (x0 + 10, y1),(x0 + 20, y1 - 20),
                            (x1 - 20, y1 - 20), (x1 - 10, y1)]
        vertices_a_int = [(x0 + 25, y0 + 10), (x0 + 20, y0 + 20), (x1 - 20, y0 + 20),]
        
        a_ext = Poligono(self._superficie, vertices_a_ext)
        a_ext.Desenhar(cor_borda)
        boundary_fill(self._superficie, x1 - 25, y0 + 5, cor_preenchimento, cor_borda)

        a_int = Poligono(self._superficie, vertices_a_int)
        a_int.Desenhar(cor_borda)
        boundary_fill(self._superficie, x0 + 25, y0 + 15, azul_teal, cor_borda)
