from ClaseManejadorInscripcion import ManejaInscripcion
from ClaseTallerCapacitacion import TallerCapacitacion
from Validador import ValidaEntero, ValidaCadena
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

    #inscribir una persona en un taller
    def opcion1(self, mt, mp, mi):
        os.system("cls")
        cad = ' FORMULARIO DE REGISTRO '
        print(cad.center(81, '='))
        print()
        band = False
        print(mt)
        while not band:
            taller = mt.buscataller()
            if taller.verificarVacante() != False:
                band = True
            else:
                print('Por este año el taller de %s no dispone de vacantes.\n')
        fecha = datetime.now()
        os.system("cls")
        print('Se esta inscribiendo el dia {}/{}/{} al taller de {}.'.format(fecha.day, fecha.month, fecha.year, taller.getNom()))
        nom = ValidaCadena('Ingrese nombre y apellido: ')
        dir = ValidaCadena('Ingrese domicilio: ')
        dni = ValidaEntero('Ingrese DNI: ')
        unapersona = Persona(nom, dir, dni)

        pago = False
        unainscripcion = Inscripcion(fecha, pago, taller, unapersona)

        unapersona.agregar(unainscripcion)
        mp.agregar(unapersona)
        taller.restarvacante()

        mi.agregaInscripcion(unainscripcion)

        print('\nInscripto exitosamente.\n')
        os.system("pause")
    
    #consulta inscripción
    def opcion2(self, mt, mp, mi):
        os.system("cls")
        persona = mp.buscarpersona()
        print()
        mi.verificaDeuda(persona)
        print()
        os.system("pause")
    
    #consulta inscriptos
    def opcion3(self, mt, mp, mi):
        os.system("cls")
        print(mt)
        taller = mt.buscataller()
        mi.mostrarInscriptos(taller)
        print()
        os.system("pause")
    
    #registra un pago
    def opcion4(self, mt, mp, mi):
        os.system("cls")
        persona = mp.buscarpersona()
        mi.buscaparapagar(persona)
        os.system("pause")
    
    #guarda las inscripciones
    def opcion5(self, mt, mp, mi):
        os.system("cls")
        mi.guardarArchivo(mp, mt)
        print()
        os.system("pause")

    #opcion 6 la añadí para verificar
    def opcion6(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE TALLERES<<<<<')
        print()
        print(mt)
        os.system("pause")

    #opcion 7 la añadí para verificar
    def opcion7(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE PERSONAS<<<<<')
        print()
        print(mp)
        os.system("pause")

    #opcion 8 la añadí para verificar
    def opcion8(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE INSCRIPCIONES<<<<<')
        print(mi)
        print()
        os.system("pause")