from manejadorViajeros import clasemanejadorViajero
from ClaseViajeroFrecuente import ViajeroFrecuente
from Validador import ValidaEntero
from ClaseMenu import Menu
import csv
import os
 
if __name__ == '__main__':
    os.system("cls")
    mv = clasemanejadorViajero()
    mv.testViajeros()
    print('>>>>>>>>>>>>>LISTA DE VIAJEROS<<<<<<<<<<<<<\n')
    print(mv)
    bandera = False
    while not bandera:
        ID = ValidaEntero('Ingrese número de viajero frecuente: ')
        viajero = mv.buscarViajero(ID)
        if viajero == None:
            print('El número de viajero {} no corresponde a un viajero.'.format(viajero.getId()))
        else:
            menu = Menu()
            cad = ' MENÚ '
            salir = False
            while not salir:
                os.system("cls")
                print(cad.center(58, '='))
                print('Has introducido el ID: {}'.format(viajero.getId()))
                print("0 - Salir")
                print("1 - Consultar cantidad de millas.")
                print("2 - Acumular millas.")
                print("3 - Canjear millas.")
                band = False
                while not band: 
                    op = ValidaEntero('Ingrese una opción: ')
                    if ( 0 <= op <= 3 ):
                        band = True
                    else:
                        print('\nLa opción ingresada es incorrecta.\n')
                menu.opcion(op, mv, viajero)
                salir = op == 0
            bandera = True