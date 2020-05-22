from ClasePersona import Persona

class Inscripcion:
    __fechainscrip = ''
    __pago = None
    __taller = None
    __persona = []

    def __init__(self, fecha = '', pago = None, taller = None):
        self.__fechainscrip = fecha
        self.__pago = pago
        self.__taller = taller
        self.__persona = []

    def agregar(self, persona):
        self.__persona.append(persona)

    def __str__(self):
        s = '\nFecha de Inscripción: ' + self.__fechainscrip + '\n'
        if self.__pago == True:
            s += 'Pagó: Si' + '\n'
        else:
            s += 'Pagó: No' + '\n'
        s += 'Taller: ' + self.__taller + '\n'
        for persona in self.__persona:
            s += str(persona) + '\n'
        return s