def set_pixel(superficie, x, y, cor):
    if 0 <= x < superficie.get_width() and 0 <= y < superficie.get_height():
        superficie.set_at((x, y), cor)
    else:
        #print("Coordenadas escritas fora dos limites da superfície. Ignorando...")
        return

def get_pixel(superficie, x, y):
    if 0 <= x < superficie.get_width() and 0 <= y < superficie.get_height():
        return superficie.get_at((x, y))
    else:
        print("Tentativa de ler coordenadas fora dos limites da superfície.")
