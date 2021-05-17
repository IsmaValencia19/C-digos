import abc

class Personal:
    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldobasico = 0
    __antiguedad = 0
 
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldobasico = sueldobasico
        self.__antiguedad = antiguedad

    def getCuil(self):
        return self.__cuil

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getSueldobasico(self):
        return self.__sueldobasico

    def getAntiguedad(self):
        return self.__antiguedad

    @abc.abstractmethod
    def getType(self):
        pass

    def __gt__(self, personal):
        return self.__apellido > personal.getApellido()

    def mostrarP(self):
        print('CUIL: %s | APELLIDO: %s | NOMBRE: %s | SUELDO BÁSICO: %s | ANTIGÜEDAD: %s' % (self.__cuil, self.__apellido, self.__nombre, self.__sueldobasico, self.__antiguedad))