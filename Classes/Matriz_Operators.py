import math

def matriz_identidade_2():
    return [[1, 0], 
            [0, 1]]

def matriz_soma_2(m1, m2):
    return [ [ m1[i][j] + m2[i][j] for j in range(2) ] for i in range(2) ]

def multiplica_escalar_2(m, e):
    return [ [ e * m[i][j] for j in range(2) ] for i in range(2) ]

def multiplica_vetor_2(m, v):
    return [ sum(m[i][k] * v[k] for k in range(2)) for i in range(2) ]

def multiplica_matrizes_2(m1, m2):
    return [ [ sum(m1[i][k] * m2[k][j] for k in range(2)) for j in range(2) ]
             for i in range(2) ]

def identidade():
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]

def translacao(tx, ty):
    return [
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ]

def escala(sx, sy):
    return [
        [sx, 0, 0],
        [0, sy, 0],
        [0, 0, 1]
    ]

def rotacao(theta):
    c = math.cos(theta)
    s = math.sin(theta)
    return [
        [ c, -s, 0],
        [ s,  c, 0],
        [ 0,  0, 1]
    ]

def multiplica_matrizes_3(a, b):
    r = [[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                r[i][j] += a[i][k] * b[k][j]
    return r
