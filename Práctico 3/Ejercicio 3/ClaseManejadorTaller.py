from ClaseTallerCapacitacion import TallerCapacitacion
import numpy as np
import csv

class ManejaTaller:
    __arre = 0

    def __init__(self):
        self.__arre = np.array([])

    #carga en el arreglo la información del archivo sobre los talleres
    def carga(self):
        archivo = open('Talleres.csv')
        reader = csv.reader(archivo, delimiter = ',')
        band = True
        for fila in reader:
            if band:
                'saltear cabecera'
                band = not band
            else:
                unTaller = TallerCapacitacion(int(fila[0]), fila[1], int(fila[2]), int(fila[3]))
                self.__arre = np.append(self.__arre, unTaller)
        archivo.close()

    def getArre(self):
        return self.__arre

    #valida si existe el taller
    def validataller(self, id):
        taller = None
        i = 0
        while i < len(self.__arre) and taller == None:
            if id == self.__arre[i].getId():
                taller = self.__arre[i]
            else:
                i += 1
        return taller

    #retorna el id de un taller según su nombre
    def getId(self, taller):
        i = 0
        while i < len(self.__arre):
            if taller == self.__arre[i].getNom():
                id = self.__arre[i].getId()
                i = len(self.__arre)
            else:
                i += 1
        return id

    def __str__(self):
        s = ''
        for taller in self.__arre:
            s += str(taller) + '\n'
        return s