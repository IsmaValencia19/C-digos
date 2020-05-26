from ClaseEmpleado import Empleado
from ClaseEmpleadoPlanta import Planta
from ClaseEmpleadoContratado import Contratado
from ClaseEmpleadoExterno import Externo
from datetime import datetime
import numpy as np
import csv

class ManejaEmpleados:
    __arre = 0

    def __init__(self, tamaño):
        self.__arre = np.array([])

    def agregar(self, unEmpleado):
        self.__arre = np.append(self.__arre, unEmpleado)

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

    def validaEmpleado(self, dni):
        band = False
        i = 0
        while i < len(self.__arre):
            if dni == self.__arre[i].getDni():
                band = True
                i = len(self.__arre)
            else:
                i += 1
        return band

    def item1(self):
        band = False
        while not band:
            dni = int(input('Ingrese DNI de empleado contratado: '))
            if self.validaEmpleado(dni) == True:
                band = True
            else:
                print('El DNI no pertenece a ningún empleado.')
                dni = int(input('Ingrese DNI de empleado contratado: '))

        fecha = datetime.now()
        print('Ingrese horas trabajadas el dia de hoy {}/{}/{}: '.format(fecha.day, fecha.month, fecha.year))
        horas = int(input())
        i = 0
        while i < len(self.__arre):
            if dni == self.__arre[i].getDni():
                self.__arre[i].modificaHoras(horas)
                i = len(self.__arre)
            else:
                i += 1
    
    def validaTarea(self, tarea):
        band = False
        i = 0
        while i < len(self.__arre):
            if tarea == self.__arre[i].getTarea():
                band = True
                i = len(self.__arre)
            else:
                i += 1
        return band

    def item2(self):
        band = False
        while not band:
            tarea = input('Ingrese tarea: ')
            if self.validaTarea(tarea) == True:
                band = True
            else:
                print('ERROR: Tarea no encontrada.')
        
        i = 0
        while i < len(self.__arre):
            if tarea == self.__arre[i].getTarea():
                print('\nTarea de %s - Monto a pagar: $%s.' % (self.__arre[i].getTarea(), self.__arre[i].getObra()))
            i += 1

    def item3(self):
        sueldo = 25000
        i = 0
        while i < len(self.__arre):
            if self.__arre[i].getSueldo() < sueldo:
                print('NOMBRE Y APELLIDO: %s - DIRECCIÓN: %s - DNI: %d\n' % (self.__arre[i].getNom(), self.__arre[i].getDir(), self.__arre[i].getDni()))
            i += 1
    
    def item4(self):
        i = 0
        while i < len(self.__arre):
            print('NOMBRE Y APELLIDO: %s - TELÉFONO: %d - SUELDO: %d\n' % (self.__arre[i].getNom(), self.__arre[i].getTel(), self.__arre[i].getSueldo()))
            i += 1
    
    def mostrar(self):
        for empleado in self.__arre:
            print(empleado)