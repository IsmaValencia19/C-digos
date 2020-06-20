from ClaseNodo import Nodo
import json

class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, dato):
        nodo = Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def getDolar(self):
        actual = self.__comienzo
        precio = None
        while actual != None and precio == None:
            casa = actual.getDato()
            if 'Oficial' == casa.getNombre():
                precio = casa.getVenta()
            else:
                actual = actual.getSiguiente()
        return precio

    def toJSON(self):
        listacasas = []
        for a in self:
            listacasas.append(a.toJSON())

        d = dict(__class__ = self.__class__.__name__, casas = listacasas)
        return d

    def mostrar(self):
        actual = self.__comienzo
        while actual != None:
            casa = actual.getDato()
            print('Nombre: %s - Compra: %s - Venta: %s - Agencia: %s - Observaciones: %s - Geolocalización: %s - Telefono: %s - Dirección: %s - Decimales: %s' % (casa.getNombre(), casa.getCompra(), casa.getVenta(), casa.getAgencia(), casa.getObservaciones(), casa.getGeolocalizacion(), casa.getTelefono(), casa.getDireccion(), casa.getDecimales()))
            actual = actual.getSiguiente()

    def __len__(self):
        return self.__tope