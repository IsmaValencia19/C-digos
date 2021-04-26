from ClaseInscripcion import Inscripcion
from Validador import ValidaEntero
from ClasePersona import Persona
from datetime import datetime

class ManejaPersona:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregar(self, persona):
        self.__lista.append(persona)

    #valida si existe la persona
    def validapersona(self, dni):
        persona = None
        i = 0
        while i < len(self.__lista) and persona == None:
            if dni == self.__lista[i].getDni():
                persona = self.__lista[i]
            else:
                i += 1
        return persona

    #busca una persona por dni
    def buscarpersona(self):
        persona = None
        band = False
        while not band:
            dni = ValidaEntero('Ingrese DNI: ')
            persona = self.validapersona(dni)
            if persona != None:
                band = True
            else:
                print('ERROR: El DNI es incorrecto. Persona no inscripta.\n')
        return persona

    #se registra el pago si el inscripto debe o no
    def registrapago(self, mi):
        persona = self.buscarpersona()
        print()
        mi.buscaparapagar(persona)

    def testing(self, mt, mi):
        persona1 = Persona('Martin Gomez', 'Av. Cordoba 5403', 35034523)
        persona2 = Persona('Julieta Martinez', 'Juan Jofre 304', 40129321)
        persona3 = Persona('Martina Lopez', 'Urquiza 123', 42932094)

        talleres = mt.getArre()  #retorné la lista de talleres para poder hacer el testing
        fecha = datetime.now()
        insc1 = Inscripcion(fecha, False, talleres[0], persona1)
        talleres[0].restarvacante()
        insc2 = Inscripcion(fecha, False, talleres[2], persona2)
        talleres[2].restarvacante()
        insc3 = Inscripcion(fecha, True, talleres[3], persona3)
        talleres[3].restarvacante()

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