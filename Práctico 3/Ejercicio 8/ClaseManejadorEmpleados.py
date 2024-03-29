from ClaseEmpleadoContratado import Contratado
from ClaseEmpleadoExterno import Externo
from Validador import ValidaEntero
from interfaceTesorero import ITesorero
from ClaseEmpleadoPlanta import Planta
from zope.interface import implementer
from interfaceGerente import IGerente
from ClaseEmpleado import Empleado
from datetime import datetime
import numpy as np
import csv
import os

@implementer(ITesorero)
@implementer(IGerente)
class ManejaEmpleados:
    __arre = 0
    __cantidad = 0

    def __init__(self, tamaño):
        self.__arre = np.empty(tamaño, dtype = Empleado)
        self.__cantidad = 0

    def agregar(self, unEmpleado):
        if type(unEmpleado) == Planta:
            self.__arre.astype(Planta)
            self.__arre[self.__cantidad] = unEmpleado
            self.__cantidad += 1
        elif type(unEmpleado) == Contratado:
            self.__arre.astype(Contratado)
            self.__arre[self.__cantidad] = unEmpleado
            self.__cantidad += 1
        elif type(unEmpleado) == Externo:
            self.__arre.astype(Externo)
            self.__arre[self.__cantidad] = unEmpleado
            self.__cantidad += 1

    def cargaArre(self):
        archivoplanta = open('planta.csv')
        reader1 = csv.reader(archivoplanta, delimiter = ',')
        for fila in reader1:
            unEmpleadoPlanta = Planta(int(fila[0]), fila[1], fila[2], int(fila[3]), int(fila[4]), int(fila[5]))
            self.agregar(unEmpleadoPlanta)
        archivoplanta.close()

        archivocontratados = open('contratados.csv')
        reader2 = csv.reader(archivocontratados, delimiter = ',')
        for fila in reader2:
            unEmpleadoContratado = Contratado(int(fila[0]), fila[1], fila[2], int(fila[3]), fila[4], fila[5], int(fila[6]))
            self.agregar(unEmpleadoContratado)
        archivocontratados.close()

        archivoexterno = open('externos.csv')
        reader3 = csv.reader(archivoexterno, delimiter = ',')
        for fila in reader3:
            unEmpleadoExterno = Externo(int(fila[0]), fila[1], fila[2], int(fila[3]), fila[4], fila[5], fila[6], int(fila[7]), int(fila[8]), int(fila[9]))
            self.agregar(unEmpleadoExterno)
        archivoexterno.close()

    def buscaEmpleado(self, dni):
        empleado = None
        i = 0
        while i < len(self.__arre) and empleado == None:
            if dni == self.__arre[i].getDni():
                empleado = self.__arre[i]
            else:
                i += 1
        return empleado

    #método de la interfaceTesorero
    def gastosSueldoPorEmpleado(self, dni):
        band = False
        empleado = None
        está = False
        while not band:
            empleado = self.buscaEmpleado(dni)
            if empleado != None:
                print('\nEl sueldo del empleado %s - DNI: %s es de $%s.\n' % (empleado.getNom(), dni, empleado.getSueldo()))
                band = True
                está = True
            else:
                band = True
        return está

    #métodos de la interfaceGerente
    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        band = False
        empleado = None
        retorno = False
        while not band:
            empleado = self.buscaEmpleado(dni)
            if empleado != None and isinstance(empleado, Planta):
                print('\n=== Sueldo básico antes de moficiar ===')
                print(empleado)
                empleado.setSueldoBasico(nuevoBasico)
                print('=== Sueldo básico modificado ===')
                print(empleado)
                retorno = True
                band = True
            else:
                band = True
        return retorno

    def modificarViaticoEExterno(self, dni, nuevoViatico):
        band = False
        empleado = None
        retorno = False
        while not band:
            empleado = self.buscaEmpleado(dni)
            if empleado != None and isinstance(empleado, Externo):
                print('\n=== Monto Viático antes de modificar ===')
                print(empleado)
                print('=== Monto Viático modificado ===')
                empleado.setViatico(nuevoViatico)
                print(empleado)
                retorno = True
                band = True
            else:
                band = True
        return retorno

    def modificarValorEPorHora(self, dni, nuevoValorHora):
        band = False
        empleado = None
        retorno = False
        while not band:
            empleado = self.buscaEmpleado(dni)
            if empleado != None and isinstance(empleado, Contratado):
                print('\n=== Valor por hora antes de modificar ===')
                print('     $%s' % (empleado.getValorHora()))
                print('\n=== Valor por hora modificado ===')
                empleado.setValorHora(nuevoValorHora)
                print('     $%s\n' % (empleado.getValorHora()))
                retorno = True
                band = True
            else:
                band = True
        return retorno