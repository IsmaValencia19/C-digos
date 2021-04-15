class Camion:
    __id = 0
    __nomConductor = ''
    __patente = ''
    __marcaCamion = ''
    __tara = 0

    def __init__(self, id, nom, pat, marca, tara):
        self.__id = id
        self.__nomConductor = nom
        self.__patente = pat
        self.__marcaCamion = marca
        self.__tara = tara

    def getId(self):
        return self.__id

    def getPat(self):
        return self.__patente

    def getCond(self):
        return self.__nomConductor

    def getTara(self):
        return self.__tara

    def __str__(self):
        return 'ID del camión: %s - Nombre del Conductor: %s - Patente del Camión: %s - Marca del Camión: %s - Peso del Camión: %s' % (self.__id, self.__nomConductor, self.__patente, self.__marcaCamion, self.__tara)