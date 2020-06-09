from ClaseManejadorInscripcion import ManejaInscripcion
from ClaseTallerCapacitacion import TallerCapacitacion
from ClaseManejadorPersona import ManejaPersona
from ClaseManejadorTaller import ManejaTaller
from ClaseInscripcion import Inscripcion
from ClasePersona import Persona
from datetime import datetime
import os

class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.opcion8
                          }
    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, mt, mp, mi):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mt, mp, mi)

    def salir(self, mt, mp, mi):
        os.system("cls")
        print()
        cad = ' SALIÓ DEL PROGRAMA '
        print(cad.center(50, '='))
        print()

    def opcion1(self, mt, mp, mi):
        os.system("cls")
        cad = ' FORMULARIO DE REGISTRO '
        print(cad.center(81, '='))
        print()
        band = False
        taller = None
        print(mt)
        while not band:
            id = int(input('Ingrese ID de taller para inscribirse: '))
            taller = mt.validataller(id)
            if taller != None:
                if taller.verificarVacante() == False:
                    print('Taller sin vacantes.\n')
                    band = False
                else:
                    band = True
            else:
                print('ID de taller incorrecto.\n')
        fecha = datetime.now()
        os.system("cls")
        print('Se esta inscribiendo el dia {}/{}/{} al taller de {}.'.format(fecha.day, fecha.month, fecha.year, taller.getNom()))
        nom = input('Ingrese nombre y apellido: ')
        dir = input('Ingrese domicilio: ')
        dni = input('Ingrese DNI: ')
        unapersona = Persona(nom, dir, dni)

        pago = False
        unainscripcion = Inscripcion(fecha, pago, taller, unapersona)

        unapersona.agregar(unainscripcion)
        mp.agregar(unapersona)
        taller.modificavacante()

        mi.agregaInscripcion(unainscripcion)

        print('\nInscripto exitosamente.\n')
        os.system("pause")
    
    def opcion2(self, mt, mp, mi):
        os.system("cls")
        persona = None
        band = False
        while not band:
            dni = input('Ingrese DNI: ')
            persona = mp.buscapersona(dni)
            if persona != None:
                band = True
            else:
                print('Persona no inscripta.')
        print()
        mi.buscapersona(persona, mt)
        print()
        os.system("pause")
    
    def opcion3(self, mt, mp, mi):
        os.system("cls")
        print(mt)
        taller = None
        band = False
        while not band:
            id = int(input('Ingrese ID de taller para listar inscriptos: '))
            taller = mt.validataller(id)
            if  taller != None:
                band = True
            else:
                print('ERROR, ID incorrecto.')
        mi.consultaInscriptos(taller)
        print()
        os.system("pause")
    
    def opcion4(self, mt, mp, mi):
        os.system("cls")
        persona = None
        band = False
        while not band:
            dni = input('Ingrese DNI: ')
            persona = mp.buscapersona(dni)
            if persona != None:
                band = True
            else:
                print('DNI incorrecto.')
        mi.buscaparapagar(persona)
        os.system("pause")
    
    def opcion5(self, mt, mp, mi):
        os.system("cls")
        mi.guardarArchivo(mp, mt)
        print()
        os.system("pause")

    #opcion 6 la añadi yo
    def opcion6(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE TALLERES<<<<<')
        print()
        print(mt)
        os.system("pause")

    #opcion 7 la añadi yo
    def opcion7(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE PERSONAS<<<<<')
        print()
        print(mp)
        os.system("pause")

    #opcion 8 la añadi yo
    def opcion8(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE INSCRIPCIONES<<<<<')
        print(mi)
        print()
        os.system("pause")