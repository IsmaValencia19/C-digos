import csv

class Cosecha:
    __lista = []

    def __init__(self):
        self.__lista = [0] * 20
        for i in range(20):
            self.__lista[i] = [0] * 45

    def agregarKG(self, ID = 0, d = 0, kg = 0):
        if (d >= 0 and d < 45):
            self.__lista[ID][d] += kg

    def getValor(self, ID = 0, DIA = 0):
        return self.__lista[ID][DIA]