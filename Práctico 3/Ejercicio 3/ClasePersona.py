class Persona:
    __nom = ''
    __dir = ''
    __dni = ''
    __insc = None

    def __init__(self, nom, dir, dni):
        self.__nom = nom
        self.__dir = dir
        self.__dni = dni
        self.__insc = None

    #agrega una inscripción por persona
    def agregar(self, inscrip):
        self.__insc = inscrip

    def getInscripcion(self):
        return self.__insc

    def getNom(self):
        return self.__nom

    def getDni(self):
        return self.__dni

    def __str__(self):
        return 'NOMBRE Y APELLIDO: %s - DNI: %s - DIRECCIÓN: %s' % (self.__nom, self.__dni, self.__dir)