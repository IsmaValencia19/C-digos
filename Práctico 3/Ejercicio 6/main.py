from ObjectEncoder import ObjectEncoder
from ClaseLista import Lista
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    obj = ObjectEncoder()
    autos = obj.Decoder(obj.Leer('vehiculos.json'))

    cad = ' MENÚ '
    menu = Menu()
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(50, '='))
        print('0 - Salir.')
        print('1 - Insertar vehículo en una posición determinada.')
        print('2 - Agregar vehículo a la colección.')
        print('3 - Mostrar por posición.')
        print('4 - Modificar precio base de un vehículo.')
        print('5 - Mostrar vehículo más económico.')
        print('6 - Mostrar todos los vehículos.')
        print('7 - Almacenar en el archivo los vehículos.')
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, autos)
        salir = op == 0