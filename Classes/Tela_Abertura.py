from Classes.Flood_Fill import Flood_Fill

poligono_caixa_z = [(100, 100), (400, 100), (400, 500), (100, 500)]
poligono_caixa_log = [(400, 100), (700, 100), (700, 500), (400, 500)]

cinza_escuro = (47, 79, 79)    
turquesa = (72, 209, 204)
branco_azulado = (240, 248, 255) 
branco = (255, 255, 255)
azul_teal = (0, 128, 128)
branco_trigo = (245, 222, 179)
blanque = (255, 250, 240)

class Tela_Abertura:
    def __init__(self, superficie):
        self.superficie = superficie
        self.flood_fill = Flood_Fill(superficie)

    def tela_abertura(self):
        self.desenhar_caixa(poligono_caixa_z, cinza_escuro, turquesa)
        self.desenhar_z(branco_azulado, blanque)
        self.desenhar_caixa(poligono_caixa_log, azul_teal, turquesa)
        self.desenhar_log(branco_trigo, branco)
        self.desenhar_ltda(branco_trigo, branco)

    def desenhar_caixa(self, vertices, cor_preenchimento, cor_borda):
        self.flood_fill.desenhar_poligono(vertices, cor_borda)
        self.flood_fill.flood_fill(vertices[0][0] + 5, vertices[0][1] + 5,
                                   cor_preenchimento, cor_borda)
        return self.flood_fill

    def desenhar_z(self, cor_preenchimento, cor_borda):
        x0, x1 = 200, 400
        y0, y1 = 200, 400
        vertices_z = [(x0, y0), (x1, y0), (x1, y0 + 50), (x0 + 50, y1 - 50),
                      (x1, y1 - 50), (x1, y1), (x0, y1), (x0, y1 - 50),
                      (x1 - 50, y0 + 50), (x0, y0 + 50)]
        
        self.flood_fill.desenhar_poligono(vertices_z, cor_borda)
        self.flood_fill.flood_fill(x0 + 5, y0 + 5, cor_preenchimento, cor_borda) 
        return self.flood_fill
    
    def desenhar_log(self, cor_preenchimento, cor_borda):
        x0, x1 = 400, 450
        y0, y1 = 200, 250
        vertices_l = [(x0, y0), (x0, y1), (x1, y1), (x1, y1 - 10),
                      (x0 + 10, y1 - 10), (x0 + 10, y0)]
        
        self.flood_fill.desenhar_poligono(vertices_l, cor_borda)
        self.flood_fill.flood_fill(x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
        
        x0, x1 = x0 + 70, x1 + 70
        vertices_o_ext = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        vertices_o_int = [(x0 + 10, y0 + 10), (x1 - 10, y0 + 10),
                          (x1 - 10, y1 - 10), (x0 + 10, y1 - 10)]

        self.flood_fill.desenhar_poligono(vertices_o_ext, cor_borda)
        self.flood_fill.flood_fill(x0 + 5, y0 + 5, cor_preenchimento, cor_borda)

        self.flood_fill.desenhar_poligono(vertices_o_int, cor_borda)
        self.flood_fill.flood_fill(x0 + 15, y0 + 15, azul_teal, cor_borda)

        x0, x1 = x0 + 70, x1 + 70
        vertices_g = [(x0, y0), (x1, y0), (x1, y0 + 10), (x0 + 10, y0 + 10),
                      (x0 + 10, y1 - 10), (x1 - 10, y1 - 10), (x1 - 10, y1 - 20),
                      (x1 - 20, y1 - 20), (x1 - 20, y1 - 30), (x1, y1 - 30),
                      (x1, y1), (x0, y1)]
        
        self.flood_fill.desenhar_poligono(vertices_g, cor_borda)
        self.flood_fill.flood_fill(x0 + 5, y0 + 5, cor_preenchimento, cor_borda)

        return self.flood_fill
    
    def desenhar_ltda(self, cor_preenchimento, cor_borda):
        x0, x1 = 400, 450
        y0, y1 = 350, 400
        vertices_l = [(x0, y0), (x0, y1), (x1, y1), (x1, y1 - 10),
                      (x0 + 10, y1 - 10), (x0 + 10, y0)]
        
        self.flood_fill.desenhar_poligono(vertices_l, cor_borda)
        self.flood_fill.flood_fill(x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
        
        x0, x1 = x0 + 70, x1 + 70
        
        vertices_t = [(x0, y0), (x1, y0), (x1, y0 + 10), (x1 - 20, y0 + 10),
                      (x1 - 20, y1), (x1 - 30, y1), (x1 - 30, y0 + 10),
                      (x0, y0 + 10)]
        
        self.flood_fill.desenhar_poligono(vertices_t, cor_borda)
        self.flood_fill.flood_fill(x0 + 5, y0 + 5, cor_preenchimento, cor_borda)
        
        x0, x1 = x0 + 70, x1 + 70

        vertices_d_ext = [(x0, y0), (x1 - 20, y0), (x1, y0 + 15), 
                          (x1, y1 - 15), (x1 - 20, y1), (x0, y1)]
        vertices_d_int = [(x0 + 10, y0 + 10), (x1 - 25, y0 + 10),
                          (x1 - 10, y0 + 20), (x1 - 10, y1 - 20), (x1 - 25, y1 - 10),
                          (x0 + 10, y1 - 10)]

        self.flood_fill.desenhar_poligono(vertices_d_ext, cor_borda)
        self.flood_fill.flood_fill(x0 + 5, y0 + 5, cor_preenchimento, cor_borda)

        self.flood_fill.desenhar_poligono(vertices_d_int, cor_borda)
        self.flood_fill.flood_fill(x0 + 15, y0 + 15, azul_teal, cor_borda)

        x0, x1 = x0 + 70, x1 + 70
        vertices_a_ext = [(x1, y1), (x1 - 20, y0), (x0 + 20, y0),
                            (x0, y1), (x0 + 10, y1),(x0 + 20, y1 - 20),
                            (x1 - 20, y1 - 20), (x1 - 10, y1)]
        vertices_a_int = [(x0 + 25, y0 + 10), (x0 + 20, y0 + 20), (x1 - 20, y0 + 20),]
        
        self.flood_fill.desenhar_poligono(vertices_a_ext, cor_borda)
        self.flood_fill.flood_fill(x1 - 25, y0 + 5, cor_preenchimento, cor_borda)

        self.flood_fill.desenhar_poligono(vertices_a_int, cor_borda)
        self.flood_fill.flood_fill(x0 + 25, y0 + 15, azul_teal, cor_borda)

        return self.flood_fill

    def desenhar_poligono(self, vertices, cor):
        self.flood_fill.desenhar_poligono(vertices, cor)

    def set_pixel(self, x, y, cor):
        Flood_Fill(self.superficie).set_pixel(x, y, cor)

    def get_pixel(self, x, y):
        return Flood_Fill(self.superficie).get_pixel(x, y)

    def largura(self):
        return Flood_Fill(self.superficie).largura()

    def altura(self):
        return Flood_Fill(self.superficie).altura()    