from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
from ClaseManejadorTaller import ManejaTaller
from Validador import ValidaEntero
from ClaseManejadorInscripcion import ManejaInscripcion
from datetime import datetime

class ManejaPersona:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregar(self, persona):
        self.__lista.append(persona)

    #busca una persona por dni
    def buscapersona(self, dni):
        persona = None
        i = 0
        while i < len(self.__lista) and persona == None:
            if dni == self.__lista[i].getDni():
                persona = self.__lista[i]
                i = len(self.__lista)
            else:
                i += 1
        return persona

    #se registra el pago si el inscripto debe o no
    def registrapago(self, mi, mt):
        band = False
        while not band:
            dni = ValidaEntero('Ingrese DNI: ')
            if self.buscapersona(dni) == True:
                band = True
            else:
                print('DNI incorrecto.')

        print()
        mi.buscaparapagar(dni, mt)

    def testing(self, mt, mi):
        persona1 = Persona('Martin Gomez', 'Av. Cordoba 5403', '35034523')
        persona2 = Persona('Julieta Martinez', 'Juan Jofre 304', '40129321')
        persona3 = Persona('Martina Lopez', 'Urquiza 123', '42932094')

        arre = mt.getArre()     #retorne la lista para poder hacer el testing
        fecha = datetime.now()
        insc1 = Inscripcion(fecha, False, arre[0], persona1)
        arre[0].modificavacante()
        insc2 = Inscripcion(fecha, False, arre[2], persona2)
        arre[2].modificavacante()
        insc3 = Inscripcion(fecha, True, arre[3], persona3)
        arre[3].modificavacante()

        persona1.agregar(insc1)
        persona2.agregar(insc2)
        persona3.agregar(insc3)

        self.agregar(persona1)
        self.agregar(persona2)
        self.agregar(persona3)

        mi.agregaInscripcion(insc1)
        mi.agregaInscripcion(insc2)
        mi.agregaInscripcion(insc3)

    def __str__(self):
        s = ''
        for persona in self.__lista:
            s += str(persona) + '\n'
        return s