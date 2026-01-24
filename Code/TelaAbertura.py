from FloodFill import FloodFill

class TelaAbertura:
    def __init__(self, width, height):
        self.flood_fill = FloodFill(width, height)

    def draw_opening_screen(self):
        # Exemplo de uso das classes para desenhar na tela de abertura
        self.screen.fill((0, 0, 0))  # Preenche a tela com preto

        # Desenha um polígono
        vertices = [(100, 100), (200, 50), (300, 100), (250, 200), (150, 200)]
        self.poligono.draw_polygon(vertices, (255, 0, 0))  # Desenha um polígono vermelho

        # Preenche o polígono usando Flood Fill
        self.flood_fill.flood_fill(200, 100, (0, 0, 0), (0, 255, 0))  # Preenche com verde

        pygame.display.flip()  # Atualiza a tela

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_opening_screen()
        pygame.quit()