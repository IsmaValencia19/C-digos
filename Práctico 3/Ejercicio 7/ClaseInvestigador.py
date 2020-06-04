from ClasePersonal import Personal

class Investigador(Personal):
    __areadeinvestigacion = ''
    __tipodeinvestigacion = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, areadeinvestigacion, tipodeinvestigacion):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__areadeinvestigacion = areadeinvestigacion
        self.__tipodeinvestigacion = tipodeinvestigacion

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

    def __str__(self):
        super().mostrar()
        return 'ÁREA DE INVESTIGACIÓN: %s | TIPO DE INVESTIGACIÓN: %s\n' % (self.__areadeinvestigacion, self.__tipodeinvestigacion)