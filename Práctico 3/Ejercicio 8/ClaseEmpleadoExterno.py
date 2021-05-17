from ClaseEmpleado import Empleado

class Externo(Empleado):
    __tarea = ''
    __fechaInicio = ''
    __fechaFinalizacion = ''
    __montoViatico = 0
    __costoObra = 0
    __montoSeguroVida = 0

    def __init__(self, dni, nom, dir, tel, tarea, fechaIni, fechafin, montoV, obra, montoSV):
        Empleado.__init__(self, dni, nom, dir, tel)
        self.__tarea = tarea
        self.__fechaInicio = fechaIni
        self.__fechaFinalizacion = fechafin
        self.__montoViatico = montoV
        self.__costoObra = obra
        self.__montoSeguroVida = montoSV

    def setViatico(self, nuevovalor):
        self.__montoViatico = nuevovalor

    def getTarea(self):
        return self.__tarea

    def getObra(self):
        return self.__costoObra

    def getSueldo(self):
        sueldo = self.__costoObra - self.__montoViatico - self.__montoSeguroVida
        return sueldo

    def __str__(self):
        super().mostrar()
        return 'TAREA: %s - CONTRATO: %s a %s - MONTO DEL VIÁTICO: $%d - COSTO DE LA OBRA: $%d - MONTO DEL SEGURO DE VIDA: $%d - SUELDO: $%d\n' % (self.__tarea, self.__fechaInicio, self.__fechaFinalizacion, self.__montoViatico, self.__costoObra, self.__montoSeguroVida, self.getSueldo())       