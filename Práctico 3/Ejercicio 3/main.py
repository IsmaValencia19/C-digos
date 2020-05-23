from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
from ClaseTallerCapacitacion import TallerCapacitacion
from ClaseManejadorTaller import ManejaTaller
from ClaseManejadorPersona import ManejaPersona
from ClaseManejadorInscripcion import ManejaInscripcion
from ClaseMenu import Menu
import os

if __name__ == '__main__':
    os.system("cls")
    mt = ManejaTaller()
    mt.carga()
    mp = ManejaPersona()
    mi = ManejaInscripcion()
    mp.testing(mt, mi)
    menu = Menu()
    salir = False
    while not salir:
        os.system("cls")
        cad = ' MENÚ '
        print(cad.center(40, '='))
        print('0 - Salir.')
        print('1 - Inscribir una persona en un taller.')
        print('2 - Consulta inscripción.')
        print('3 - Consultar Inscriptos.')
        print('4 - Registrar pago.')
        print('5 - Guardar inscripciones.')
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op, mt, mp, mi)
        salir = op == 0 