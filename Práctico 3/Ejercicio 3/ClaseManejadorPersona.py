from ClasePersona import Persona
from ClaseInscripcion import Inscripcion
from ClaseManejadorTaller import ManejaTaller
from ClaseManejadorInscripcion import ManejaInscripcion

class ManejaPersona:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregar(self, persona):
        self.__lista.append(persona)

    def registrar(self, mt, mi):
        cad = ' FORMULARIO DE REGISTRO '
        print(cad.center(40, '='))
        print()
        band = False
        print(mt)
        while not band:
            id = int(input('Ingrese ID de taller para inscribirse: '))
            if mt.validataller(id) == True:
                band = True
            else:
                print('ID de taller incorrecto.')
                id = int(input('Ingrese ID de taller para inscribirse: '))
        nom = input('Ingrese nombre y apellido: ')
        dir = input('Ingrese domicilio: ')
        dni = input('Ingrese DNI: ')
        unapersona = Persona(nom, dir, dni)

        fecha = input('Ingrese fecha de inscripción: ')
        pago = False
        taller = mt.getTaller(id)
        unainscripcion = Inscripcion(fecha, pago, taller)
        unainscripcion.agregar(unapersona)
        mt.modificavacante(id)

        self.agregar(unapersona)

        mi.agregaInscripcion(unainscripcion)
        print()
        print('Inscripto exitosamente.')

    def busca(self, dni):
        band = False
        i = 0
        while i < len(self.__lista):
            if dni == self.__lista[i].getDni():
                band = True
                i = len(self.__lista)
            else:
                i += 1
        return band

    def consultaInscripcion(self, mt):
        band = False
        while not band:
            dni = input('Ingresa DNI: ')
            if self.busca(dni) == True:
                band = True
            else:
                print('Persona no inscripta.')
                dni = input('Ingresa DNI: ')
        
        i = 0
        while i < len(self.__lista):
            if dni == self.__lista[i].getDni(): 
                print('Inscripcion: %s' % (self.__lista[i].getInscripcion()))
                i = len(self.__lista)
            else:
                i += 1

    def testing(self, mt, mi):
        persona1 = Persona('Martin Gomez', 'Av. Cordoba 5403', '35034523')
        persona2 = Persona('Julieta Martinez', 'Juan Jofre 304', '40129321')
        persona3 = Persona('Martina Lopez', 'Urquiza 123', '42932094')

        insc1 = Inscripcion('21/05/2020', False, 'Python')
        insc1.agregar(persona1)
        mt.modificavacante(1)
        insc2 = Inscripcion('21/05/2020', False, 'HTML5')
        insc2.agregar(persona2)
        mt.modificavacante(3)
        insc3 = Inscripcion('22/05/2020', True, 'CSS3')
        insc3.agregar(persona3)
        mt.modificavacante(4)

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