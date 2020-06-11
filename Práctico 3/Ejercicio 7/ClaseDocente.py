from ClasePersonal import Personal

class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, areadeinvestigacion = '', tipodeinvestigacion = '', categoria = '', importeextra = 0):
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

    def getCargo(self):
        return self.__cargo

    def getCatedra(self):
        return self.__catedra

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

    def mostrar(self):
        super().mostrarP()
        print('CARRERA EN LA QUE DICTA CLASES: %s | CARGO: %s | CÁTEDRA: %s' % (self.__carrera, self.__cargo, self.__catedra))
    
    #este mostrar lo hice para que en la clase DocenteInvestigador solo muestre los atributos de docente, porque con el mostrar de arriba trae el mostrar de personal, junto con
    #el método de mostrar de la clase Investigador me sale dos veces el mismo nombre, por eso cree este "mostra"
    def mostra(self):
        print('CARRERA EN LA QUE DICTA CLASES: %s | CARGO: %s | CÁTEDRA: %s' % (self.__carrera, self.__cargo, self.__catedra))