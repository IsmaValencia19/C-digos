from ClaseManejaLibros import ManejaLibro
from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    os.system("cls")
    ml = ManejaLibro()
    ml.cargar()

    menu = Menu()
    cad = ' MENÚ '
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(58, '='))
        print('0 - Salir.')
        print('1 - Ingresar ID para mostrar detalles de un libro.')
        print('2 - Ingresar una palabra para ver en que parte se encuentra.')
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( op >= 0 and op <= 2 ):
                band = True
            else:
                print('\nLa opción ingresada es incorrecta.\n')
        menu.opcion(op, ml)
        salir = op == 0