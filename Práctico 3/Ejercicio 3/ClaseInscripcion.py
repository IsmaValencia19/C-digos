class Inscripcion:
    __fechainscrip = ''
    __pago = None
    __taller = None
    __persona = None

    def __init__(self, fecha = '', pago = None, taller = None, persona = None):
        self.__fechainscrip = fecha
        self.__pago = pago
        self.__taller = taller
        self.__persona = persona

    def getPersona(self):
        return self.__persona

    def getTaller(self):
        return self.__taller

    def getPago(self):
        return self.__pago

    def modificapago(self):
        self.__pago = True

    def getFecha(self):
        return self.__fechainscrip

    def __str__(self):
        s = ''
        if self.__pago == True:
            s = 'Si'
        else:
            s = 'No'
        return '\nFECHA DE INSCRIPCIÓN: {}/{}/{} - PAGÓ: {} - TALLER: {} - INSCRIPTO: {}'.format(self.__fechainscrip.day, self.__fechainscrip.month, self.__fechainscrip.year, s, self.__taller.getNom(), self.__persona)