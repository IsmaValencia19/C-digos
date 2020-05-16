from claseCAMION import claseCamion
import csv

class manejadorCamiones:
    __listaCamion = []
    
    def __init__(self):
        self.__listaCamion = []
    
    def agregarCamion(self, camion):
        self.__listaCamion.append(camion)
    
    def buscarcamion(self, id):
        for indice, camion in enumerate(self.__listaCamion):
            if camion.getId() == id:
                return indice
    
    def __str__(self):
        s = ''
        for camion in self.__listaCamion:
            s += str(camion) + '\n'
        return s

    def testCamiones(self):
        archivo = open('camiones.csv')
        reader = csv.reader(archivo, delimiter = ',')
        bandera = True
        for fila in reader:
            if bandera:
                'saltear cabecera'
                bandera = not bandera
            else:
                id = int(fila[0])
                nom = fila[1]
                patente = fila[2]
                marca = fila[3]
                tara = float(fila[4])
                unCamion = claseCamion(id, nom, patente, marca, tara)
                self.agregarCamion(unCamion)
        archivo.close()
