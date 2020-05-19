from ClaseSabor import Sabor
import csv
import numpy as np

class ManejaSabores:
    __arre = 0
   
    def __init__(self):
        self.__arre = np.array([])

    def agregar(self, sabor):
        self.__arre = np.append(self.__arre, sabor)

    def cargaSabor(self):
        archivo = open('sabor.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            unSabor = Sabor(int(fila[0]), fila[1], fila[2])
            self.agregar(unSabor)
        archivo.close()

    def validaSabor(self, iDsabor):
        band = False
        i = 0
        while i < len(self.__arre):
            if iDsabor == self.__arre[i].getId():
                band = True
                i = len(self.__arre)
            else:
                i += 1
        return band

    def getSabor(self, idsabor):
        i = 0
        while i < len(self.__arre):
            if idsabor == self.__arre[i].getId():
                sabor = self.__arre[i].getNom()
                i = len(self.__arre)
            else:
                i += 1
        return sabor

    def b5sabores(self, cont):
        listapedido = []
        i = 0
        while i < len(cont):
            if self.__arre[i].getId() == i + 1:
                #print('Sabor: %s fue pedido %s vez/veces.' % (self.__arre[i].getNom(), cont[i]))
                sabor = self.__arre[i].getNom()
                pedido = cont[i]
                lista = [sabor, pedido]
                listapedido.append(lista)
            i += 1
        
        listapedido.sort(key = lambda x:x[1], reverse = True)
        for i in range(5):
            print(listapedido[i])

    def gramosabor(self, acum):
        band = False
        while not band:
            idSabor = int(input('Ingrese ID de sabor: '))
            if self.validaSabor(idSabor) == True:
                #print('ID de sabor correcto.')
                band = True
            else:
                print('ID de sabor incorrecto.')
                idSabor = int(input('Ingrese ID de sabor: '))

        i = 0
        while i < len(acum):
            if self.__arre[i].getId() == idSabor:
                print('Sabor: %s - Vendido: %s gs.' % (self.__arre[i].getNom(), acum[i]))
                i = len(acum)
            else:
                i += 1

    def __str__(self):
        s = ''
        for sabor in self.__arre:
            s += str(sabor) + '\n'
        return s