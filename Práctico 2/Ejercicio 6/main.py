from claseFechaHora import claseFechaHora
from Validador import ValidaEntero
import os

def opcion1():
    hora = claseFechaHora()
    hora.Mostrar()
    print()
    print('Se suman 5hs.')
    print()
    suma = hora + 5
    hora.Mostrar()
    os.system("pause")

def opcion2():
    print()
    hora = claseFechaHora()
    hora.AdelantarHora(7)
    hora.Mostrar()
    print()
    print('Se restan 9hs.')
    print()
    resta = hora - 9
    hora.Mostrar()
    print()
    os.system("pause")

def opcion3():
    print()
    hora = claseFechaHora()
    hora.AdelantarHora(17, 20, 14)
    hora.Mostrar()
    print()
    hora2 = claseFechaHora()
    hora2.AdelantarHora(17, 20, 16)
    hora2.Mostrar()
    print()
    if(hora > hora2):
        print('La primera hora es mayor que la segunda.')
    else:
        print("la segunda hora es mayor que la primera.")
    os.system("pause")

def salir():
    print()
    print('>>>Salio del programa<<<.')
    print()

def menu():
    op = 0
    while op != 4:
        os.system("cls")
        print('1 - Sumar hora.')
        print('2 - Restar hora.')
        print('3 - Distinguir entre dos horas cuál es la mayor.')
        print('4 - Salir.')
        op = ValidaEntero('Ingrese opción: ')
        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
        elif op == 4:
            salir()

if __name__ == '__main__':
    os.system("cls")
    menu()