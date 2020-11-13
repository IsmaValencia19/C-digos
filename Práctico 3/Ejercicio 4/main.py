from ClaseManejadorEmpleados import ManejaEmpleados 
from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
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
        op = ValidaEntero('Ingrese una opción: ')
        menu.opcion(op, me)
        salir = op == 0