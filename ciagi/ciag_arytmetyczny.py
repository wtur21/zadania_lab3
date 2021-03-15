def n_wyraz(a_1, r, n):
    a_n = a_1 + (n - 1) * r
    return a_n

def suma_an(a_1, a_n, n):
    S_n = ((a_1 + a_n)/2) * n
    return S_n

def suma_r(a_1, r, n):
    S_n = ((2 * a_1 + (n - 1) * r)/2) * n
    return S_n

def a_2(a_1, a_3):
    a_2 = (a_1 + a_3)/2
    return a_2