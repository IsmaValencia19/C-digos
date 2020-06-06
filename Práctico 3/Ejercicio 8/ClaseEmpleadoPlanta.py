from ClaseEmpleado import Empleado
import abc

class Planta(Empleado):
    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self, dni, nom, dir, tel, sueldobasico, anti):
        Empleado.__init__(self, dni, nom, dir, tel)
        self.__sueldoBasico = sueldobasico
        self.__antiguedad = anti

    @abc.abstractmethod
    def getTarea(self):
        pass

    def getSueldoBasico(self):
        return self.__sueldoBasico

    def setSueldoBasico(self, nuevovalor):
        self.__sueldoBasico = nuevovalor

    def getAntig(self):
        return self.__antiguedad

    def getSueldo(self):
        sueldo = self.__sueldoBasico + ((self.__sueldoBasico/100) * self.__antiguedad)
        return sueldo 

    def __lt__(self, sueld):
        return self.getSueldo() < sueld

    def __str__(self):
        super().mostrar()
        return 'SUELDO BÁSICO: $%d - ANTIGÜEDAD: %d - SUELDO: %d\n' % (self.__sueldoBasico, self.__antiguedad, self.getSueldo())