class Inscripcion:
    __fechainscrip = ''
    __pago = None
    __taller = None
    __persona = None

    def __init__(self, fecha = '', pago = None, taller = None):
        self.__fechainscrip = fecha
        self.__pago = pago
        self.__taller = taller
        self.__persona = None

    def agregar(self, persona):
        self.__persona = persona

    def __str__(self):
        s = ''
        if self.__pago == True:
            s = 'Si'
        else:
            s = 'No'
        return '\nFECHA DE INSCRIPCIÓN: %s - PAGÓ: %s - TALLER: %s - INSCRIPTO: %s' % (self.__fechainscrip, s, self.__taller, self.__persona)