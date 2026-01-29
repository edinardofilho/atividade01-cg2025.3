def m_identidade():
    return [[1, 0], 
            [0, 1]]

def m_add(m1, m2):
    return [ [ m1[i][j] + m2[i][j] for j in range(2) ] for i in range(2) ]

def e_mul(m, e):
    return [ [ e * m[i][j] for j in range(2) ] for i in range(2) ]

def v_mul(m, v):
    return [ sum(m[i][k] * v[k] for k in range(2)) for i in range(2) ]

def m_mul(m1, m2):
    return [ [ sum(m1[i][k] * m2[k][j] for k in range(2)) for j in range(2) ] for i in range(2) ]
