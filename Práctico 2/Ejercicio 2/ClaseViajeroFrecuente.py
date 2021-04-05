class ViajeroFrecuente:
    __id = 0
    __dni = 0
    __nom = ''
    __ape = ''
    __mill_acum = 0

    def __init__(self, nid, dni, nomb, apell, millas_acum):
        self.__id = nid
        self.__dni = dni
        self.__nom = nomb
        self.__ape = apell
        self.__mill_acum = millas_acum

    def setId(self, id):
        self.__id = id

    def getId(self):
        return self.__id

    def setDni(self, dni):
        self.__dni = dni

    def getDni(self):
        return self.__dni

    def setNom(self, nom):
        self.__nom = nom

    def getNom(self):
        return self.__nom

    def setApe(self, ape):
        self.__ape = ape

    def getApe(self):
        return self.__ape

    def setMilla(self, millas):
        self.__mill_acum = millas
        
    def getMilla(self):
        return self.__mill_acum
        
    def cantTotalMillas(self):
        return self.__mill_acum

    def acumMillas(self, millas):
        self.__mill_acum += millas

    def canjearMillas(self, millasAcanjear):
        self.__mill_acum -= millasAcanjear

    def __str__(self):
        return '%s - %s - %s - %s - %s' % (self.__id, self.__dni, self.__nom, self.__ape, self.__mill_acum)