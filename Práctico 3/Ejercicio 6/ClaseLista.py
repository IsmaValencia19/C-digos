from zope.interface import implementer
from ClaseAutoNuevo import AutoNuevo
from ClaseAutoUsado import AutoUsado
from archivodeinterface import inter
from ClaseNodo import Nodo
import json
import zope

@implementer(inter)
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

    #metodos de la interface
    def agregarElemento(self, dato):
        nodo = Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarElemento(self, elemento, posicion):
        if posicion == 0:
            self.agregarElemento(elemento)
        else:
            aux = self.__comienzo
            i = 0
            elemento = Nodo(elemento)

            while i < posicion and aux != None:
                anterior = aux
                aux = aux.getSiguiente()
                i += 1

            if i > posicion:
                raise IndexError
            else:
                elemento.setSiguiente(aux)
                anterior.setSiguiente(elemento)
                self.__tope += 1

    def mostrarElemento(self, posicion):
        i = 0
        actual = self.__comienzo
        encontrado = None
        while actual != None and encontrado == None:
            if i == posicion:
                auto = actual.getDato()
                encontrado = auto
            else:
                actual = actual.getSiguiente()
                i += 1
        return type(encontrado)

    def buscavehiculo(self, pat):
        actual = self.__comienzo
        encontrado = None
        while actual != None and encontrado == None:
            auto = actual.getDato()
            if isinstance(auto, AutoUsado) and pat == auto.getPat():
                encontrado = auto
            else:
                actual = actual.getSiguiente()
        return encontrado

    def item4(self): 
        band = False
        vehiculo = None
        while not band:
            pat = input('Ingrese patente de vehículo para modificar el precio base: ')
            vehiculo = self.buscavehiculo(pat)
            if vehiculo != None:
                precio = int(input('Ingrese precio nuevo: '))
                vehiculo.modificaprecio(precio)
                print('\nPrecio de venta: %d' % (vehiculo.getImporte()))
                print()
                band = True
            else:
                print('ERROR, vehículo no encontrado.')

    def buscaminimo(self):
        min = 999999999
        actual = self.__comienzo
        while actual != None:
            auto = actual.getDato()
            if min > auto.getPrecio():
                min = auto.getPrecio()
            else:
                actual = actual.getSiguiente()
        return min

    def item5(self):
        actual = self.__comienzo
        while actual != None:
            auto = actual.getDato()
            if self.buscaminimo() == auto.getPrecio():
                print(auto)
                actual = None
            else:
                actual = actual.getSiguiente()

    def toJSON(self):
        listaautos = []
        for a in self:
            listaautos.append(a.toJSON())

        d = dict(__class__ = self.__class__.__name__, autos = listaautos)
        return d

    def mostrar(self):
        actual = self.__comienzo
        while actual != None:
            auto = actual.getDato()
            print('Modelo: %s - Cantidad de Puertas: %s - Importe de Venta: %s' % (auto.getModelo(), auto.getPuertas(), auto.getImporte()))
            actual = actual.getSiguiente()

    def __len__(self):
        return self.__tope