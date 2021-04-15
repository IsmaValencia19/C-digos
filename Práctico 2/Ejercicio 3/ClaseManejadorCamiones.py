from ClaseCamion import Camion
import csv

class ManejadorCamiones:
    __camiones = []

    def __init__(self):
        self.__camiones = []

    def agregar(self, camion):
        self.__camiones.append(camion)

    def Cargar(self):
        archivo = open('camiones.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            ID = int(fila[0])
            nom = fila[1]
            pat = fila[2]
            marca = fila[3]
            tara = fila[4]
            unCamion = Camion(ID, nom, pat, marca, tara)
            self.agregar(unCamion)
        archivo.close()

    def buscaCamion(self, ID):
        camion = None
        i = 0
        while i < len(self.__camiones):
            if self.__camiones[i].getId() == ID:
                camion = self.__camiones[i]
                i = len(self.__camiones)
            else:
                i += 1
        return camion

    def __str__(self):
        s = ''
        for cam in self.__camiones:
            s += str(cam) + '\n'
        return s