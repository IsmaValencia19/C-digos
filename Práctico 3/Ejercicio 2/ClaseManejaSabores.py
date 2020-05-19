from ClaseSabor import Sabor
import csv

class ManejaSabores:
    __lista = []
    __contSabor = 0     #esta variable la uso para saber la cantidad de sabores registrados

    def __init__(self):
        self.__lista = []
        self.__contSabor = 0

    def agregar(self, sabor):
        self.__lista.append(sabor)

    def cargaSabor(self):
        archivo = open('sabor.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            unSabor = Sabor(int(fila[0]), fila[1], fila[2])
            self.__contSabor += 1
            self.agregar(unSabor)
        archivo.close()

    def validaSabor(self, iDsabor):
        band = False
        i = 0
        while i < len(self.__lista):
            if iDsabor == self.__lista[i].getId():
                band = True
                i = len(self.__lista)
            else:
                i += 1
        return band

    def getSabor(self, idsabor):
        i = 0
        while i < len(self.__lista):
            if idsabor == self.__lista[i].getId():
                sabor = self.__lista[i].getNom()
                i = len(self.__lista)
            else:
                i += 1
        return sabor

    def cantSabores(self):      
        return self.__contSabor

    def b5sabores(self, cont):
        listapedido = []
        i = 0
        while i < len(cont):
            if self.__lista[i].getId() == i + 1:
                #print('Sabor: %s fue pedido %s vez/veces.' % (self.__lista[i].getNom(), cont[i]))
                sabor = self.__lista[i].getNom()
                pedido = cont[i]
                lista = [sabor, pedido]
                listapedido.append(lista)
            i += 1
        
        listapedido.sort(key = lambda x:x[1], reverse = True)
        for fila in listapedido:
            print(fila)

    def __str__(self):
        s = ''
        for sabor in self.__lista:
            s += str(sabor) + '\n'
        return s