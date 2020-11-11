class TallerCapacitacion:
    __id = 0
    __nom = ''
    __vacantes =0
    __montoInscripcion = 0

    def __init__(self, id = 0, nom = '', vac = 0, monto = 0):
        self.__id = id
        self.__nom = nom
        self.__vacantes = vac
        self.__montoInscripcion = monto

    def getId(self):
        return self.__id

    def getNom(self):
        return self.__nom

    def getPago(self):
        return self.__montoInscripcion

    def verificarVacante(self):
        band = False
        if self.__vacantes > 0:
            band = True
        return band

    def modificavacante(self):
        self.__vacantes -= 1

    def __str__(self):
        return 'ID DE TALLER: %s - NOMBRE: %s - VACANTES: %s - MONTO DE INSCRIPCIÓN: $%s' % (self.__id, self.__nom, self.__vacantes, self.__montoInscripcion)