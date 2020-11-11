from ClaseManejaSabores import ManejaSabores
from ClaseManejaHelados import ManejaHelados
from Validador import ValidaEntero
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    os.system("cls")
    ms = ManejaSabores()
    ms.cargaSabor()
    mh = ManejaHelados()
    menu = Menu()
    cad = ' MENÚ '
    salir = False
    while not salir:
        os.system("cls")
        print(cad.center(76, '='))
        print('0 - Salir.')
        print('1 - Registrar venta de helado.')
        print('2 - Ver 5 sabores más vendidos.')
        print('3 - Ingresar ID de un sabor para ver el total de gramos vendidos.')
        print('4 - Ingresar Tipo de Helado para ver los sabores más vendidos en dicho tipo.')
        op = ValidaEntero('Ingrese una opción: ')
        menu.opcion(op, ms, mh)
        salir = op == 0