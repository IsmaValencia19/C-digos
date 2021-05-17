from ObjectEncoder import ObjectEncoder
from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    obj = ObjectEncoder()
    personal = obj.Decoder(obj.Leer())
    menu = Menu()
    cad = ' MENÚ '
    cade = ''
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(85, '='))
        print('0 - Salir.')
        print('1 - Insertar a agentes en la colección.')
        print('2 - Agregar agentes a la colección.')
        print('3 - Mostrar por posición el tipo de agente.')
        print('4 - Ver el/los docente/s investigador/es de una carrera.')
        print('5 - Cantidad de Docentes Investigadores e Investigadores de un área de investigación.')
        print('6 - Mostrar agentes.')
        print('7 - Mostrar docentes investigadores de una categoria.')
        print('8 - Guardar en el archivo.')
        print(cade.center(85, '='))
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( op >= 0 and op <= 8 ):
                band = True
            else:
                print('ERROR: La opción ingresada es incorrecta.\n')
        menu.opcion(op, personal, obj)
        salir = op == 0