from archivodeinterface import inter
from ClaseNodo import Nodo
import zope

@zope.interface.implementer(inter)
class Lista:
    __comienzo = None
    __actual = None
    __tope = 0
    __indice = 0

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

    def validacategoria(self, categoria):
        categorias = ['I', 'II', 'III', 'IV', 'V']
        encontrada = None
        i = 0
        while i < len(categorias) and encontrada == None:
            if categorias[i] == categoria:
                encontrada = categorias[i]
                i = len(categorias)
            else:
                i += 1
        return encontrada 

    def item4(self):
        actual = self.__comienzo
        while actual != None:
            personal = actual.getDato()
            
            actual = actual.getSiguiente()

    def toJSON(self):
        listapersonal = []
        for a in self:
            listapersonal.append(a.toJSON())

        d = dict(__class__ = self.__class__.__name__, personal = listapersonal)
        return d

    def mostrar(self):
        for personal in self:
            print(personal)

    def __len__(self):
        return self.__tope