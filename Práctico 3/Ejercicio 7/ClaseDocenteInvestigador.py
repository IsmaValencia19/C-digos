from ClaseInvestigador import Investigador
from ClaseDocente import Docente

class DocenteInvestigador(Docente, Investigador):
    __categoria = ''
    __importeextra = 0

    def __init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, areadeinvestigacion, tipodeinvestigacion, categoria, importeextra):
        Docente.__init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, areadeinvestigacion, tipodeinvestigacion, categoria, importeextra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, areadeinvestigacion, tipodeinvestigacion, categoria, importeextra)
        self.__categoria = categoria
        self.__importeextra = importeextra

    def getSueldo(self):
        return (Docente.getSueldo(self) + self.__importeextra)

    def getCategoria(self):
        return self.__categoria

    def getImporteextra(self):
        return self.__importeextra

    def __gt__(self, personal):
        return self.getNombre() > personal.getNombre()

    def toJSON(self):
        return dict(
                    __class__ = self.__class__.__name__,
                    __atributos__ = dict(
                                            cuil = self.getCuil(),
                                            apellido = self.getApellido(),
                                            nombre = self.getNombre(),
                                            sueldobasico = self.getSueldobasico(),
                                            antiguedad = self.getAntiguedad(),
                                            carrera = self.getCarrera(),
                                            cargo = self.getCargo(),
                                            catedra = self.getCatedra(),
                                            areadeinvestigacion = self.getArea(),
                                            tipodeinvestigacion = self.getTipo(),
                                            categoria = self.__categoria,
                                            importeextra = self.__importeextra
                                        )
                    )

    def mostrar(self):
        Investigador.mostrar(self)
        Docente.mostra(self)
        print('CATEGORÍA EN EL PROGRAMA DE INCENTIVOS DE INVESTIGACIÓN: %s | IMPORTE EXTRA POR DOCENCIA E INVESTIGACIÓN: %s | SUELDO: %s' % (self.__categoria, self.__importeextra, self.getSueldo()))