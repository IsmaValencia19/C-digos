from ClaseViajeroFrecuente import ViajeroFrecuente
import csv

class clasemanejadorViajero:
    __listaViajero = []
    
    def __init__(self):
        self.__listaViajero = []
    
    def agregarViajero(self, viajero):
        self.__listaViajero.append(viajero)

    def testViajeros(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter = ',')
        bandera = True
        for fila in reader:
            if bandera:
                'saltear cabecera'
                bandera = not bandera
            else:
                ID = int(fila[0])
                dni = int(fila[1])
                nom = fila[2]
                ape = fila[3]
                millas = int(fila[4])
                unViajero = ViajeroFrecuente(ID, dni, nom, ape, millas)
                self.agregarViajero(unViajero)
        archivo.close()
    
    def buscarViajero(self, ID):
        i = 0
        viajero = None
        while i < len(self.__listaViajero):
            if self.__listaViajero[i].getId() == ID:
                viajero = self.__listaViajero[i]
                i = len(self.__listaViajero)
            else:
                i += 1
        return viajero
    
    def __str__(self):
        s = ''
        for viajero in self.__listaViajero:
            s += str(viajero) + '\n'
        return s