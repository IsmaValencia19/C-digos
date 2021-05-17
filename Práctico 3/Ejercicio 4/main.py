from ClaseManejadorEmpleados import ManejaEmpleados 
from Testing import ActivaTesting
from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    #ActivaTesting()
    me = ManejaEmpleados(8)
    me.cargaArre()
    menu = Menu()
    cad = ' MENÚ '
    cade = ''
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(25, '='))
        print('0 - Salir.')
        print('1 - Registrar horas.')
        print('2 - Total de tarea.')
        print('3 - Ayuda para empleados.')
        print('4 - Calcular sueldo.')
        print(cade.center(25, '='))
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( op >= 0 and op <= 4 ):
                band = True
            else:
                print('La opción ingresada es incorrecta.\n')
        menu.opcion(op, me)
        salir = op == 0