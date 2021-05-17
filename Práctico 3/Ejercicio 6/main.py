from ObjectEncoder import ObjectEncoder
from Validador import ValidaEntero
from ClaseLista import Lista
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    obj = ObjectEncoder()
    autos = obj.Decoder(obj.Leer())

    cad = ' MENÚ '
    cade = ''
    menu = Menu()
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(50, '='))
        print('0 - Salir.')
        print('1 - Insertar vehículo en una posición determinada.')
        print('2 - Agregar vehículo a la colección.')
        print('3 - Mostrar el tipo de auto por posición.')
        print('4 - Modificar precio base de un vehículo.')
        print('5 - Mostrar vehículo más económico.')
        print('6 - Mostrar todos los vehículos.')
        print('7 - Almacenar en el archivo los vehículos.')
        print(cade.center(50, '='))
        band = False
        while not band: 
            op = ValidaEntero('Ingrese una opción: ')
            if ( op >= 0 and op <= 7 ):
                band = True
            else:
                print('La opción ingresada es incorrecta.\n')
        menu.opcion(op, autos, obj)
        salir = op == 0