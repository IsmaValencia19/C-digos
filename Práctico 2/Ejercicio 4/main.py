from claseFechaHora import FechaHora
from Validador import ValidaEntero
import os

if __name__ == '__main__':
    os.system("cls")
    
    d = ValidaEntero('Ingrese dia: ')
    mes = ValidaEntero('Ingrese mes: ')
    a = ValidaEntero('Ingrese año: ')
    h = ValidaEntero('Ingrese hora: ')
    m = ValidaEntero('Ingrese minutos: ')
    s = ValidaEntero('Ingrese segundos: ')

    print()
    r = FechaHora()
    r1 = FechaHora(d, mes, a)
    r2 = FechaHora(d, mes, a, h, m, s)
    print(r)
    print(r1)
    print(r2)  
    os.system('pause')

    print()
    r.PonerEnHora(5)
    print(r)
    os.system('pause')
    
    print()
    r2.PonerEnHora(13, 30)
    print(r2)
    os.system('pause')

    print()
    r.PonerEnHora(14, 30, 25)
    print(r)
    os.system('pause')
    
    print()              
    r.AdelantarHora(3)
    print(r)
    os.system('pause')

    print()
    r1.AdelantarHora(1, 15)
    print(r1)
    print()