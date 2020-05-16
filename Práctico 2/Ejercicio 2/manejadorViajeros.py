from Clases import claseViajero
import csv

class clasemanejadorViajero:
    __listaViajero = []
    
    def __init__(self):
        self.__listaViajero = []
    
    def agregarViajero(self, viajero):
        self.__listaViajero.append(viajero)
    
    def buscarViajero(self, id):
        i = 0
        while i < len(self.__listaViajero):
            if self.__listaViajero[i].getId() == id:
                indice = self.__listaViajero[i].getId() - 1
            i += 1
        return indice

        #for indice, viajero in enumerate(self.__listaViajero):
        #    if viajero.getId() == id:
        #        return indice
    
    def __str__(self):
        s = ''
        for viajero in self.__listaViajero:
            s += str(viajero) + '\n'
        return s

    def testViajeros(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo, delimiter = ',')
        bandera = True
        for fila in reader:
            if bandera:
                'saltear cabecera'
                bandera = not bandera
            else:
                id = int(fila[0])
                dni = int(fila[1])
                nom = fila[2]
                ape = fila[3]
                millas = int(fila[4])
                unViajero = claseViajero(id, dni, nom, ape, millas)
                self.agregarViajero(unViajero)
        archivo.close()

    def getId(self, indice):
        return self.__listaViajero[indice]