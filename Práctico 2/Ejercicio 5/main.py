from manejadorAlumnos import manejadorAlumno
from Validador import ValidaEntero
from ClaseAlumno import Alumno
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    ma = manejadorAlumno()
    ma.testAlumnos()

    menu = Menu()
    cad = ' MENÚ '
    salir = False
    while not salir:
        os.system("cls")
        print(ma)
        print(cad.center(58, '='))
        print('0 - Salir.')
        print('1 - Ingrese año y división para listar alumnos en malas condiciones.')
        print('2 - Modificar la cantidad máxima de inasistencias permitidas.')
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( 0 <= op <= 2 ):
                band = True
            else:
                print('\nLa opción ingresada es incorrecta.\n')
        menu.opcion(op, ma)
        salir = op == 0   