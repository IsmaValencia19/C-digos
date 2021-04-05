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
                id = int(fila[0])
                dni = int(fila[1])
                nom = fila[2]
                ape = fila[3]
                millas = int(fila[4])
                unViajero = ViajeroFrecuente(id, dni, nom, ape, millas)
                self.agregarViajero(unViajero)
        archivo.close()
    
    def buscarViajero(self, id):
        i = 0
        indice = None
        while i < len(self.__listaViajero):
            if self.__listaViajero[i].getId() == id:
                indice = self.__listaViajero[i].getId() - 1
                i = len(self.__listaViajero)
            else:
                i += 1
        return indice
 
    def getId(self, indice):
        return self.__listaViajero[indice]
    
    def __str__(self):
        s = ''
        for viajero in self.__listaViajero:
            s += str(viajero) + '\n'
        return s