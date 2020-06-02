from ClaseAutoNuevo import AutoNuevo
from ClaseAutoUsado import AutoUsado
from archivodeinterface import inter
from ClaseNodo import Nodo
import json
import zope

@zope.interface.implementer(inter)
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
                encontrado = actual
            else:
                actual = actual.getSiguiente()
                i += 1
        return type(encontrado)

    def toJSON(self):
        autos = []
        for a in self:
            autos.append(a.toJSON())

        d = dict(__class__ = self.__class__.__name__, datos = autos)
        return d

    def mostrar(self):
        for a in self:
            print(a)
            print()

    def __len__(self):
        return self.__tope