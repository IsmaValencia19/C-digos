from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    menu = Menu()
    cad = ' MENÚ '
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(58, '='))
        print('0 - Salir.')
        print('1 - Union de dos conjuntos.')
        print('2 - Diferencia de dos conjuntos.')
        print('3 - Verifica si dos conjuntos son iguales.')
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( op >= 0 and op <= 3 ):
                band = True
            else:
                print('\nLa opción ingresada es incorrecta.\n')
        menu.opcion(op)
        salir = op == 0   