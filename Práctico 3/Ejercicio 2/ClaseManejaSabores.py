from ClaseSabor import Sabor
import csv

class ManejaSabores:
    __lista = []

    def __init__(self):
        self.__lista = []

    def agregar(self, sabor):
        self.__lista.append(sabor)

    def cargasabor(self):
        archivo = open('sabores.csv')
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