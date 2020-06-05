from ClasePersonal import Personal
import abc

class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def getSueldo(self):
        porcentaje = self.getAntiguedad() / 100

        porcentajecargo = 0
        if self.__cargo == 'Simple':
            porcentajecargo = 0.10
        elif self.__cargo == 'Semi-Exclusivo':
            porcentajecargo = 0.20
        elif self.__cargo == 'Exclusivo':
            porcentajecargo = 0.50
        
        return (self.getSueldobasico() + (porcentaje * self.getSueldobasico()) / 100 + (porcentajecargo * self.getSueldobasico()) / 100)

    def getCarrera(self):
        return self.__carrera

    @abc.abstractmethod
    def getArea(self):
        pass

    def toJSON(self):
        return dict(
                    __class__ = self.__class__.__name__,
                    __atributos__ = dict(
                                            cuil = self.getCuil(),
                                            apellido = self.getApellido(),
                                            nombre = self.getNombre(),
                                            sueldobasico = self.getSueldobasico(),
                                            antiguedad = self.getAntiguedad(),
                                            carrera = self.__carrera,
                                            cargo = self.__cargo,
                                            catedra = self.__catedra
                                        )
                    )

    def __str__(self):
        super().mostrar()
        return 'CARRERA EN LA QUE DICTA CLASES: %s | CARGO: %s | CÁTEDRA: %s\n' % (self.__carrera, self.__cargo, self.__catedra)