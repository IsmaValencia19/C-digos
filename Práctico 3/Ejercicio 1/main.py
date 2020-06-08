from ClaseManejaLibros import ManejaLibro
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    os.system("cls")
    ml = ManejaLibro()
    ml.cargarLista()
    menu = Menu()
    cad = ' MENÚ '
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(58, '='))
        print('0 - Salir.')
        print('1 - Ingresar ID para mostrar detalles de un libro.')
        print('2 - Ingresar una palabra para ver en que parte se encuentra.')
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, ml)
        salir = op == 0