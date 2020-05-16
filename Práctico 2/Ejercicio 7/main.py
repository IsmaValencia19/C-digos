from claseFechaHora import claseFechaHora
from claseHora import claseHora
import os
os.system("cls")

if __name__ == '__main__':
    d = 5#int(input('Ingrese dia: '))
    mes = 5#int(input('Ingrese mes: '))
    a = 2020#int(input('Ingrese año: '))
    h = 8#int(input('Ingrese hora: '))
    m = 30#int(input('Ingrese minutos: '))
    s = 30#int(input('Ingrese segundos: '))

    f = claseFechaHora(d, mes, a, h, m, s)
    f.Mostrar()
    print()

    h1 = 20#int(input('Ingrese hora: '))
    m1 = 30#int(input('Ingrese minutos: '))
    s1 = 30#nt(input('Ingrese segundos: '))

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