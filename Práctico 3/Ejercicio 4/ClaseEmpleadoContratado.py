from ClaseEmpleado import Empleado

class Contratado(Empleado):
    __fechaInicio = ''
    __fechaFinalizacion = ''
    __cantHorasTrabajadas = 0
    valorHora = 200

    def __init__(self, dni, nom, dir, tel, fechaI, fechaF, cantHoras):
        Empleado.__init__(self, dni, nom, dir, tel)
        self.__fechaInicio = fechaI
        self.__fechaFinalizacion = fechaF
        self.__cantHorasTrabajadas = cantHoras

    @classmethod
    def getValorHora(cls):
        return cls.valorHora

    def getCantHoras(self):
        return self.__cantHorasTrabajadas

    def modificaHoras(self, horas):
        self.__cantHorasTrabajadas += horas

    def getSueldo(self, ):
        sueldo = self.__cantHorasTrabajadas * Contratado.getValorHora()
        return sueldo

    #def __lt__(self, sueld):
    #    return self.getSueldo() < sueld

    def __str__(self):
        super().mostrar()
        return 'CONTRATO: %s a %s - CANTIDAD DE HORAS TRABAJADAS: %d - SUELDO: %d\n' % (self.__fechaInicio, self.__fechaFinalizacion, self.__cantHorasTrabajadas, self.getSueldo())