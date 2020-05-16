class claseCamion:
    __id = 0
    __nomconductor = ''
    __patente = ''
    __marca = ''
    __tara = 0

    def __init__(self, id, nomc, paten, marc, tara):
        self.__id = id
        self.__nomconductor = nomc
        self.__patente = paten
        self.__marca = marc
        self.__tara = tara
    
    def getDatos(self):
        return (self.__patente, self.__nomconductor)