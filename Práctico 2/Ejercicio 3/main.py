from ClaseManejadorCamiones import ManejadorCamiones
from ClaseManejadorCosechas import ManejadorCosechas
from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    Camiones = ManejadorCamiones()
    Camiones.Cargar()

    Cosechas = ManejadorCosechas()
    Cosechas.Cargar()

    menu = Menu()
    cad = ' MENÚ '
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(58, '='))
        print('0 - Salir.')
        print('1 - Ingresar ID de un camión y muestra la cantidad total de kilos descargados.')
        print('2 - Ingrese un dia y muestra un listado de datos.')
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( 0 <= op <= 2 ):
                band = True
            else:
                print('\nLa opción ingresada es incorrecta.\n')
        menu.opcion(op, Camiones, Cosechas)
        salir = op == 0