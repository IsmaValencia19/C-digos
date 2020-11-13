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

    def validaempleado(self, dni):
        empleado = None
        i = 0
        while i < len(self.__arre):
            if dni == self.__arre[i].getDni():
                empleado = self.__arre[i]
                i = len(self.__arre)
            else:
                i += 1
        return empleado

    #método de la interfaceTesorero
    def gastosSueldoPorEmpleado(self, documento):
        band = False
        empleado = None
        retorno = 1 #variable usada por si es incorrecto el dni
        while not band and retorno == 1:
            dni = documento
            empleado = self.validaempleado(dni)
            if empleado != None:
                print('\nEl sueldo del empleado %s - DNI: %s es de $%s.\n' % (empleado.getNom(), dni, empleado.getSueldo()))
                band = True
            else:
                retorno = -1
        return retorno

    #métodos de la interfaceGerente
    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        band = False
        empleado = None
        retorno = 1 #variable usada por si es incorrecto el dni
        while not band and retorno == 1:
            empleado = self.validaempleado(dni)
            if empleado != None and isinstance(empleado, Planta):
                print('\n=== Sueldo básico antes de moficiar ===')
                print(empleado)
                empleado.setSueldoBasico(nuevoBasico)
                print('=== Sueldo básico modificado ===')
                print(empleado)
                band = True
            else:
                retorno = -1
        return retorno

    def modificarViaticoEExterno(self, dni, nuevoViatico):
        band = False
        empleado = None
        retorno = 1 #variable usada por si es incorrecto el dni
        while not band and retorno == 1:
            empleado = self.validaempleado(dni)
            if empleado != None and isinstance(empleado, Externo):
                print('\n=== Monto Viático antes de modificar ===')
                print(empleado)
                print('=== Monto Viático modificado ===')
                empleado.setViatico(nuevoViatico)
                print(empleado)
                band = True
            else:
                retorno = -1
        return retorno

    def modificarValorEPorHora(self, dni, nuevoValorHora):
        band = False
        empleado = None
        retorno = 1 #variable usada por si es incorrecto el dni
        while not band and retorno == 1:
            empleado = self.validaempleado(dni)
            if empleado != None and isinstance(empleado, Contratado):
                print('\n=== Valor por hora antes de modificar ===')
                print('     $%s' % (empleado.getValorHora()))
                print('\n=== Valor por hora modificado ===')
                empleado.setValorHora(nuevoValorHora)
                print('     $%s\n' % (empleado.getValorHora()))
                band = True
            else:
                retorno = -1
        return retorno

def tesorero(manejarTesorero):
    os.system("cls")
    tesorero = ' CUENTA DE TESORERO '
    print(tesorero.center(50, '='))
    band = False
    while not band:
        dni = ValidaEntero('Ingrese DNI de un empleado para verificar el sueldo: ')
        if manejarTesorero.gastosSueldoPorEmpleado(dni) != -1:
            band = True
        else:
            print('ERROR, DNI incorrecto.')

def gerente(manejarGerente):
    os.system("cls")
    gerente = ' CUENTA DE GERENTE '
    print(gerente.center(55, '='))
    cad = ' MENÚ '
    cade = ''
    print(cad.center(55, '='))
    print('1 - Modificar sueldo básico de un Empleado Planta.')
    print('2 - Mofidicar valor por hora de un Empleado Contratado.')
    print('3 - Modificar monto del viático de un Empleado Externo.')
    print(cade.center(55, '='))
    op = ValidaEntero('Ingrese una opción: ')
    print()
    if op == 1:
        band = False
        while not band:
            dni = ValidaEntero('Ingrese DNI de un Empleado Planta: ')
            sueldo = ValidaEntero('Ingrese nuevo sueldo básico: ')
            if manejarGerente.modificarBasicoEPlanta(dni, sueldo) != -1:
                band = True
            else:
                print('ERROR, el DNI no pertenece a un Empleado Planta.\n')
    elif op == 2:
        band = False
        while not band:
            dni = ValidaEntero('Ingrese DNI de un Empleado Contratado: ')
            nuevovalor = ValidaEntero('Ingrese nuevo valor por hora: ')
            if manejarGerente.modificarValorEPorHora(dni, nuevovalor) != -1:
                band = True
            else:
                print('ERROR, el DNI no pertenece a un Empleado Contratado.\n')
    elif op == 3:
        band = False
        while not band:
            dni = ValidaEntero('Ingrese DNI de un Empleado Externo: ')
            nuevovalor = ValidaEntero('Ingrese nuevo valor de viático: ')
            if manejarGerente.modificarViaticoEExterno(dni, nuevovalor) != -1:
                band = True
            else:
                print('ERROR, el DNI no pertenece a un Empleado Externo.\n')
    else:
        print('=== OPCIÓN INCORRECTA ===')