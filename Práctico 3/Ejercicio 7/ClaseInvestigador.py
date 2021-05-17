from ClasePersonal import Personal

class Investigador(Personal):
    __areadeinvestigacion = ''
    __tipodeinvestigacion = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera = '', cargo = '', catedra = '', areadeinvestigacion = '', tipodeinvestigacion = '', categoria = '', importeextra = 0):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__areadeinvestigacion = areadeinvestigacion
        self.__tipodeinvestigacion = tipodeinvestigacion

    def getSueldo(self):
        porcentaje = self.getAntiguedad() / 100
        return (self.getSueldobasico() + (porcentaje * self.getSueldobasico()) / 100)

    def getArea(self):
        return self.__areadeinvestigacion

    def getTipo(self):
        return self.__tipodeinvestigacion
    
    def getType(self):
        return 'Investigador'

    def toJSON(self):
        return dict(
                    __class__ = self.__class__.__name__,
                    __atributos__ = dict(
                                            cuil = self.getCuil(),
                                            apellido = self.getApellido(),
                                            nombre = self.getNombre(),
                                            sueldobasico = self.getSueldobasico(),
                                            antiguedad = self.getAntiguedad(),
                                            areadeinvestigacion = self.__areadeinvestigacion,
                                            tipodeinvestigacion = self.__tipodeinvestigacion
                                        )
                    )

    def mostrar(self):
        super().mostrarP()
        print('ÁREA DE INVESTIGACIÓN: %s | TIPO DE INVESTIGACIÓN: %s' % (self.__areadeinvestigacion, self.__tipodeinvestigacion))