class claseCosecha:
    __listacosechas = []

    def __init__(self):
        self.__listacosechas = [0] * 45
        for i in range(4):
            self.__listacosechas[i] = [0] * 20

    def agregar(self, d = 0, i = 0, kg = 0):
        if(0 <= d <= 45):
            self.__listacosechas[d][i] = kg

    def getValor(self, i = 0, j = 0):
        return self.__listacosechas[i][j]