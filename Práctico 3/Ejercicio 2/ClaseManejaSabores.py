from ClaseSabor import Sabor
import csv

class ManejaSabores:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregar(self, sabor):
        self.__lista.append(sabor)

    def validaSabor(self, sabor):
        band = False
        i = 0
        while i < len(self.__lista):
            if sabor == self.__lista[i].getNom():
                band = True
                i = len(self.__lista)
            else:
                i += 1
        return band

    def cargaSabor(self):
        archivo = open('sabor.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            unSabor = Sabor(int(fila[0]), fila[1], fila[2])
            self.agregar(unSabor)
        archivo.close()

    def __str__(self):
        s = ''
        for sabor in self.__lista:
            s += str(sabor) + '\n'
        return s