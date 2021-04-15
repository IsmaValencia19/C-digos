from claseFechaHora import FechaHora
from Validador import ValidaEntero
from claseHora import Hora
import os

if __name__ == '__main__':
    os.system("cls")

    d = 12#ValidaEntero('Ingrese dia: ')
    mes = 4#ValidaEntero('Ingrese mes: ')
    a = 2021#ValidaEntero('Ingrese año: ')
    h = 16#ValidaEntero('Ingrese hora: ')
    m = 25#ValidaEntero('Ingrese minutos: ')
    s = 55#ValidaEntero('Ingrese segundos: ')

    f = FechaHora(d, mes, a, h, m, s)
    print(f)
    print()

    h1 = 16#ValidaEntero('Ingrese hora: ')
    m1 = 26#ValidaEntero('Ingrese minutos: ')
    s1 = 30#ValidaEntero('Ingrese segundos: ')

    r = Hora(h1, m1, s1)
    print(r)
    print()
    os.system('pause')

    print()
    f2 = f + r
    print(f2)
    print()
    os.system('pause')

    print()
    f3 = r + f
    print(f3)
    print()
    os.system('pause')

    print()
    f4 = f3 - 1
    print(f4)
    print()
    os.system('pause')

    print()
    f4 = 1 + f2
    print(f4)
    print()
    os.system('pause')