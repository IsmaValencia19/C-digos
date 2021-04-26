class Inscripcion:
    __fechainscrip = ""
    __pago = None
    __taller = None
    __persona = None

    def __init__(self, fecha = "", pago = None, taller = None, persona = None):
        self.__fechainscrip = fecha
        self.__pago = pago
        self.__taller = taller
        self.__persona = persona

    def getFecha(self):
        return self.__fechainscrip 

    def getPago(self):
        return self.__pago

    def getTaller(self):
        return self.__taller

    def getPersona(self):
        return self.__persona

    #se modifica el pago de las inscripciones que adeudan
    def modificapago(self):
        self.__pago = True

    def __str__(self):
        p = ''
        if self.__pago == True:
            p = 'Si'
        else:
            p = 'No'
        return '\nFECHA DE INSCRIPCIÓN: {}/{}/{} - PAGÓ: {} - TALLER: {} - INSCRIPTO: {}'.format(self.__fechainscrip.day, self.__fechainscrip.month, self.__fechainscrip.year, p, self.__taller.getNom(), self.__persona)