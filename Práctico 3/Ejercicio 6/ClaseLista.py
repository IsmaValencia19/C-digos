from Validador import ValidaEntero, ValidaCadena, ValidaCadenaAlfabetica
from zope.interface import implementer
from ClaseAutoNuevo import AutoNuevo
from ClaseAutoUsado import AutoUsado
from archivodeinterface import inter
from ClaseNodo import Nodo
import json
import zope
import os

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

    def RegistroAutoNuevo(self):
        os.system('cls')
        print('\n>>>>>>>>>>REGISTRANDO VEHÍCULO NUEVO<<<<<<<<<<')
        modelo = ValidaCadena('Ingrese el modelo(ej. Palio, Punto, etc): ')
        puertas = ValidaEntero('Ingrese la cantidad de puertas: ')
        color = ValidaCadenaAlfabetica('Ingrese color: ')
        precio = ValidaEntero('Ingrese precio: ')
        band = False
        while not band:
            version = ValidaCadenaAlfabetica('Ingrese versión(Full o Base): ')
            if (version.capitalize() == 'Full') or (version.capitalize() == 'Base'):
                band = True
            else:
                print('ERROR, versión incorrecta.\n')
        unAutoNuevo = AutoNuevo(modelo.capitalize(), puertas, color.capitalize(), precio, version.capitalize())
        return unAutoNuevo

    def RegistroAutoUsado(self):
        print('\n>>>>>>>>>>REGISTRANDO VEHÍCULO USADO<<<<<<<<<<')
        modelo = ValidaCadena('Ingrese el modelo(ej. Palio, Focus, etc): ')
        puertas = ValidaEntero('Ingrese la cantidad de puertas: ')
        color = ValidaCadenaAlfabetica('Ingrese color: ')
        precio = ValidaEntero('Ingrese precio: ')
        marca = ValidaCadena('Ingrese marca: ')
        patente = ValidaCadena('Ingrese patente: ')
        año = ValidaEntero('Ingrese año de fabrica: ')
        kilometraje = ValidaEntero('Ingrese kilometraje: ')
        unAutoUsado = AutoUsado(modelo.capitalize(), puertas, color.capitalize(), precio, marca.capitalize(), patente, año, kilometraje)
        return unAutoUsado

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
        auto = None
        while actual != None and auto == None:
            if i == (posicion - 1):
                auto = actual.getDato()
            else:
                actual = actual.getSiguiente()
                i += 1
        if isinstance(auto, AutoNuevo):
            print('\nEl objeto de la posición %s es un Auto Nuevo.\n' % (posicion))
        else:
            print('\nEl objeto de la posición %s es un Auto Usado.\n' % (posicion))

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
            pat = ValidaCadena('Ingrese patente de vehículo para modificiar el precio base: ')
            vehiculo = self.buscavehiculo(pat)
            if vehiculo != None:
                print('\nPrecio de venta: $%s\n' % (vehiculo.getImporte()))
                precio = ValidaEntero('Ingrese precio nuevo: ')
                vehiculo.modificaprecio(precio)
                print('\nPrecio de venta actualizado: $%d\n' % (vehiculo.getImporte()))
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
            print('Marca: %s - Modelo: %s - Cantidad de Puertas: %s - Importe de Venta: $%s' % (auto.getMarca(), auto.getModelo(), auto.getPuertas(), auto.getImporte()))
            actual = actual.getSiguiente()

    def __len__(self):
        return self.__tope