from ClasePersonal import Personal

class DocenteInvestigador(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''
    __areadeinvestigacion = ''
    __tipodeinvestigacion = ''
    __categoria = ''
    __importeextra = 0

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, areadeinvestigacion, tipodeinvestigacion, categoria, importeextra):
        super().__init__(cuil, apellido, nombre, sueldobasico, antiguedad)
        self.__carrera = carrera 
        self.__cargo = cargo
        self.__catedra = catedra
        self.__areadeinvestigacion = areadeinvestigacion
        self.__tipodeinvestigacion = tipodeinvestigacion
        self.__categoria = categoria
        self.__importeextra = importeextra

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
                                            catedra = self.__catedra,
                                            areadeinvestigacion = self.__areadeinvestigacion,
                                            tipodeinvestigacion = self.__tipodeinvestigacion,
                                            categoria = self.__categoria,
                                            importeextra = self.__importeextra
                                        )
                    )

    def __str__(self):
        super().mostrar()
        return 'CARRERA EN LA QUE DICTA CLASES: %s | CARGO: %s | CÁTEDRA: %s | ÁREA DE INVESTIGACIÓN: %s | TIPO DE INVESTIGACIÓN: %s | CATEGORÍA EN EL PROGRAMA DE INCENTIVOS DE INVESTIGACIÓN: %s | IMPORTE EXTRA POR DOCENCIA E INVESTIGACIÓN: %s\n' % (self.__carrera, self.__cargo, self.__catedra, self.__areadeinvestigacion, self.__tipodeinvestigacion, self.__categoria, self.__importeextra)