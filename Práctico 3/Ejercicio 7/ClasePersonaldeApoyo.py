from ClasePersonal import Personal

class PersonaldeApoyo(Personal):
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categoria = categoria

    def toJSON(self):
        return dict(
                    __class__ = self.__class__.__name__,
                    __atributos__ = dict(
                                            cuil = self.getCuil(),
                                            apellido = self.getApellido(),
                                            nombre = self.getNombre(),
                                            sueldobasico = self.getSueldobasico(),
                                            antiguedad = self.getAntiguedad(),
                                            categoria = self.__categoria
                                        )
                    )

    def __str__(self):
        super().mostrar()
        return 'CATEGORÍA: %s\n' % (self.__categoria)