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

    #valida si existe el taller
    def validataller(self, id):
        band = False
        i = 0
        while i < len(self.__arre):
            if id == self.__arre[i].getId():
                band = True
                i = len(self.__arre)
            else:
                i += 1
        return band

    #devuelve el nombre del taller según su id
    def getTaller(self, id):
        taller = ''
        i = 0
        while i < len(self.__arre):
            if id == self.__arre[i].getId():
                taller = self.__arre[i].getNom()
                i = len(self.__arre)
            else:
                i += 1
        return taller

    #envia el precio de cada taller
    def getPago(self, taller):
        i = 0
        while i < len(self.__arre):
            if taller == self.__arre[i].getNom():
                pago = self.__arre[i].getPago()
                i = len(self.__arre)
            else:
                i += 1
        return pago

    #se modifica la vacante de cada taller al inscribirse una persona, osea se va restando a medida que ingresa gente
    def modificavacante(self, id):
        i = 0
        while i < len(self.__arre):
            if id == self.__arre[i].getId():
                self.__arre[i].modificavacante()
                i = len(self.__arre)
            else:
                i += 1

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