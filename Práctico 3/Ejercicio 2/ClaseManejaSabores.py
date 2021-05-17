from Validador import ValidaEntero
from ClaseSabor import Sabor
import numpy as np
import csv

class ManejaSabores:
    __arre = 0
   
    def __init__(self):
        self.__arre = np.array([])

    def agregar(self, sabor):
        self.__arre = np.append(self.__arre, sabor)

    def carga(self):
        archivo = open('sabor.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            unSabor = Sabor(int(fila[0]), fila[1], fila[2])
            self.agregar(unSabor)
        archivo.close()

    def getCantidadSabores(self):
        return len(self.__arre)

    def buscarSabor(self, idsabor):
        i = 0
        sabor = None
        while i < len(self.__arre):
            if idsabor == self.__arre[i].getId():
                sabor = self.__arre[i]
                i = len(self.__arre)
            else:
                i += 1
        return sabor

    def cincoSabores(self, cont):
        listapedido = []
        i = 0
        print('Sabores más vendidos: \n')
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
            print('Sabor %s fue vendido %s vez/veces.' % (listapedido[i][0], listapedido[i][1]))

    def gramosabor(self, acum):
        band = False
        while not band:
            sabor = self.buscarSabor(ValidaEntero('Ingrese ID de sabor: '))
            if sabor != None:
                i = 0
                while i < len(acum):
                    if self.__arre[i].getId() == sabor.getId():
                        print('\nSabor: %s - Vendido: %s gs.' % (self.__arre[i].getNom(), acum[i]))
                        i = len(acum)
                    else:
                        i += 1
                band = True
            else:
                print('\nID de sabor incorrecto.\n')

    def __str__(self):
        s = ''
        for sabor in self.__arre:
            s += str(sabor) + '\n'
        return s