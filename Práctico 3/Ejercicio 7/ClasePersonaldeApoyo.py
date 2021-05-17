from ClasePersonal import Personal

class PersonaldeApoyo(Personal):
    __categoria = 0
 
    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__categoria = categoria

    def getSueldo(self):
        porcentaje = self.getAntiguedad() / 100

        porcentajecategoria = 0
        if 1 <= self.__categoria <= 10:
            porcentajecategoria = 0.10
        elif 11 <= self.__categoria <= 20:
            porcentajecategoria = 0.20
        elif self.__categoria == 21 or 22:
            porcentajecategoria = 0.30

        return (self.getSueldobasico() + (porcentaje * self.getSueldobasico()) / 100 + (porcentajecategoria * self.getSueldobasico()) / 100)

    def getType(self):
        return 'Personal de Apoyo'
    
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

    def mostrar(self):
        super().mostrarP()
        print('CATEGORÍA: %s' % (self.__categoria))