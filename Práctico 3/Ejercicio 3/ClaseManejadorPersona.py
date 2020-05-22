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

    def carga(self, mt, mi):
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