from ClaseManejadorInscripcion import ManejaInscripcion
from ClaseManejadorPersona import ManejaPersona
from ClaseManejadorTaller import ManejaTaller
from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    os.system("cls")
    mt = ManejaTaller()
    mt.carga()
    mi = ManejaInscripcion()
    mp = ManejaPersona()
    mp.testing(mt, mi)
    menu = Menu()
    salir = False
    while not salir:
        os.system("cls")
        cad = ' MENÚ '
        print(cad.center(40, '='))
        print('0 - Salir.')
        print('1 - Inscribir una persona en un taller.')
        print('2 - Consultar inscripción.')
        print('3 - Consultar Inscriptos.')
        print('4 - Registrar pago.')
        print('5 - Guardar inscripciones.')
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( op >= 0 and op <= 8 ):
                band = True
            else:
                print('La opción ingresada es incorrecta.\n')
        menu.opcion(op, mt, mp, mi)
        salir = op == 0 