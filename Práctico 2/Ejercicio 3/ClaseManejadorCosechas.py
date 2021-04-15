from Validador import ValidaEntero
from ClaseCosecha import Cosecha
import csv

class ManejadorCosechas:
    __cosecha = None

    def __init__(self):
        self.__cosecha = Cosecha()

    def Cargar(self):
        archivo = open('cosechas.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            ID = int(fila[0])
            dia = int(fila[1])
            kg = int(fila[2])
            self.__cosecha.agregarKG(ID - 1, dia - 1, kg)
        archivo.close()

    def kilos(self, ID):
        kilos = 0
        for i in range(45):
            kilos += self.__cosecha.getValor(ID - 1, i)
        print('\nEl camión de ID: %s, tiene un total de %s Kg descargados.' % (ID, kilos))

    def getLista(self):
        return self.__cosecha

    #def Mostrar(self):
    #    for row in self.__lista:
    #        print(' '.join([str(elem) for elem in row]))