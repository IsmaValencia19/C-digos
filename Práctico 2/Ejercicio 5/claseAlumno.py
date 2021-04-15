class Alumno:
    #variables de clase
    cant_max_inasis = 21
    cant_totalClases = 100
    
    #variables de instancia
    __nom = ''
    __año = 0
    __div = 0
    __cant_inasistencia = 0
    
    def __init__(self, nom = '', año = 0, div = 0, cant_inasis = 0):
        self.__nom = nom
        self.__año = año
        self.__div = div
        self.__cant_inasistencia = cant_inasis

    def getAño(self):
        return self.__año

    def getDiv(self):
        return self.__div

    def getNom(self):
        return self.__nom

    def getInasis(self):
        return self.__cant_inasistencia

    def  porcen_inasis(self):
        return (self.__cant_inasistencia * 100 ) / Alumno.getCantClases()

    def __str__(self):
        return 'Nombre: %s - Año: %s - División: %s - Inasistencias: %s' % (self.__nom, self.__año, self.__div, self.__cant_inasistencia)

    #metodos de clase
    @classmethod
    def actualizarMaxInas(cls, cantInasis):
        cls.cant_max_inasis = cantInasis
    
    @classmethod
    def getMaxInas(cls):
        return cls.cant_max_inasis
    
    @classmethod
    def getCantClases(cls):
        return cls.cant_totalClases

    @classmethod
    def verAsistencias(cls):
        print('La cantidad máxima de inasistencias exigida son: '+str(cls.getMaxInas()))
        print('Cantidad de clases en el año: ' +str(cls.getCantClases()))        