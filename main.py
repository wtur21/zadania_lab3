# zad. 1

A = [1 - x for x in range(1, 11)]

B = [4**x for x in range(8)]

C = [x for x in B if x % 2 == 0]

# zad. 2

import random as r

lista1 = [r.randint(-1000, 1000) for x in range(10)]

lista2 = [x for x in lista1 if x % 2 == 0]

# zad. 3

slo = {"chleb": "szt", "ziemniaki": "kg", "mleko": "szt", "banany": "kg", "bułki": "szt", "jabłka": "kg", "woda": "szt"}
lista = [x for x in slo if slo[x] == "szt"]

# zad. 4

def trk():
    a = input("Podaj długość najdłuższego boku tego trójkąta: ")

    print("Podaj długości pozostałych boków tego trójkąta: ")
    b = input()
    c = input()

    a = int(a)
    b = int(b)
    c = int(c)

    if a**2 == b**2 + c**2:
        wynik = "jest"
    else:
        wynik = "nie jest"

    print(f"Trójkąt {wynik} prostokątny")

# zad. 5

def trapez(a = 1, b = 1, h = 1):
    P = ((a + b) * h)/2
    return P

# zad. 6

def i_ciag(a = 1, b = 4, ile = 10):
    i = 0
    ilocz = 1
    while i < ile:
        ilocz = ilocz * a
        a = a * b
        i = i + 1
    return ilocz

# zad. 7

def i_ciag(*ciag):
    ile = input("Podaj ilość elementów: ")
    ile = int(ile)
    i = 0
    ilocz = 1
    while i < ile:
        ilocz = ilocz * ciag[i]
        i = i + 1
    return ilocz

# zad. 8

def zakupy(**lista):
    print(lista)
    wartosc = 0
    for x in lista:
        wartosc = wartosc + lista[x]

    return wartosc

# zad.9

# test

import ciagi.ciag_geometryczny as geo

import ciagi.ciag_arytmetyczny as aryt

print(geo.n_wyraz(2,4,5))
print(aryt.n_wyraz(1,5,10))

# zad. 10

liczby = [x for x in range(0, 101) if x % 4 == 0]
print(liczby)
f = open("liczby.txt", "w")
f.write(str(liczby))
f.close()

# zad. 11

f = open("liczby.txt", "r")
for linia in f:
    print(linia, end = "")
f.close()