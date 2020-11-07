from claseFechaHora import claseFechaHora
from Validador import ValidaEntero
from claseHora import claseHora
import os

if __name__ == '__main__':
    os.system("cls")
    
    d = 5#ValidaEntero('Ingrese dia: ')
    mes = 5#ValidaEntero('Ingrese mes: ')
    a = 2020#ValidaEntero('Ingrese año: ')
    h = 8#ValidaEntero('Ingrese hora: ')
    m = 30#ValidaEntero('Ingrese minutos: ')
    s = 30#ValidaEntero('Ingrese segundos: ')

    f = claseFechaHora(d, mes, a, h, m, s)
    f.Mostrar()
    print()

    h1 = 20#ValidaEntero('Ingrese hora: ')
    m1 = 30#ValidaEntero('Ingrese minutos: ')
    s1 = 30#ValidaEntero('Ingrese segundos: ')

    r = claseHora(h1, m1, s1)
    r.Mostrar()
    print()

    f2 = claseFechaHora()
    f2 = f + r
    f2.Mostrar()
    print()

    f3 = r + f
    f3.Mostrar()
    print()

    f4 = f3 - 1
    f4.Mostrar()