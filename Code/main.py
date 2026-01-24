
import sys
from TelaAbertura import TelaAbertura
from SetPixel import SetPixel

def main():
    width, height = 800, 600
    SetPixel(width, height, (0, 0, 0))  # Inicializa a tela com fundo preto
    tela_abertura = TelaAbertura(width, height)
    tela_abertura.run()

sys.exit()