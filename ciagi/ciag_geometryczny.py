import math as m

def n_wyraz(a_1, q, n):
    a_n = a_1 * q ** (n - 1)
    return a_n

def suma(a_1, q, n):
    if q == 1:
        S_n = a_1 * n
    else:
        s_n = a_1 * ((1 - q ** n)/(1 - q))
    return S_n

def a_2(a_1, a_3):
    a_2 = m.sqrt(a_1 * a_3)
    return a_2