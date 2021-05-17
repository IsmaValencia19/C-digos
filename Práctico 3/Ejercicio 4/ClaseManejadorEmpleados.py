from Validador import ValidaEntero, ValidaCadena
from ClaseEmpleadoContratado import Contratado
from ClaseEmpleadoExterno import Externo
from ClaseEmpleadoPlanta import Planta
from ClaseEmpleado import Empleado
from datetime import datetime
import numpy as np
import csv

class ManejaEmpleados:
    __arre = 0
    __cantidad = 0

    def __init__(self, tamaño):
        self.__arre = np.empty(tamaño, dtype = Empleado)
        self.__cantidad = 0

    #agrega al arreglo un empleado
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

    #carga el arreglo con empleados almacenados en un archivo
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

    #busca un empleado en la colección según el dni
    def buscaEmpleado(self, dni):
        empleado = None
        i = 0
        while i < len(self.__arre):
            if dni == self.__arre[i].getDni():
                empleado = self.__arre[i]
                i = len(self.__arre)
            else:
                i += 1
        return empleado

    #esta función agrega horas trabajadas a un empleado
    def item1(self):
        band = False
        empleado = None
        while not band:
            dni = ValidaEntero('Ingrese DNI de empleado contratado: ')
            empleado = self.buscaEmpleado(dni)
            if empleado != None and isinstance(empleado, Contratado):
                fecha = datetime.now()
                print('\nHoras trabajadas hasta el momento: %s\n' % (empleado.getCantHoras()))
                print('Ingrese horas trabajadas el dia de hoy {}/{}/{}: '.format(fecha.day, fecha.month, fecha.year))
                horas = ValidaEntero('')
                empleado.modificaHoras(horas)
                print('\nHoras trabajadas actualizadas: %s\n' % (empleado.getCantHoras()))
                band = True
            else:
                print('DNI incorrecto.\n')
    
    #valida si la tarea ingresada por teclado se encuentra en algún empleado
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

    #esta funcion muestra el monto a pagar por una tarea
    def item2(self):
        montoObra = 0
        fecha = datetime.now()
        band = False
        while not band:
            tarea = ValidaCadena('Ingrese tarea: ')
            if self.validaTarea(tarea.capitalize()) == True:
                i = 0
                while i < len(self.__arre):
                    if isinstance(self.__arre[i], Externo):
                        if tarea.capitalize() == self.__arre[i].getTarea():
                            unafecha = '{}/{}/{}'.format(fecha.day, fecha.month, fecha.year)
                            fechadehoy = datetime.strptime(unafecha, '%d/%m/%Y')
                            fechadefin = datetime.strptime(self.__arre[i].getFechaFin(), '%d/%m/%Y')
                            if fechadehoy > fechadefin:     #verifica si a dia de hoy la tarea no ha terminado para calcular el monto a pagar
                                montoObra += self.__arre[i].getSueldo()
                        i += 1
                    else:
                        i += 1
                band = True
            else:
                print('ERROR: La tarea ingresada no es correcta.\n')
        print('\nTarea de %s - Monto a pagar: $%s.' % (tarea.capitalize(), montoObra))
            
    #esta funcion muestra los empleados que reciben la ayuda economica<
    def item3(self):
        sueldo = 25000
        i = 0
        while i < len(self.__arre):
            if self.__arre[i].getSueldo() < sueldo:
                print('NOMBRE Y APELLIDO: %s - DIRECCIÓN: %s - DNI: %d - SUELDO: $%s\n' % (self.__arre[i].getNom(), self.__arre[i].getDir(), self.__arre[i].getDni(), self.__arre[i].getSueldo()))
            i += 1
    
    #esta funcion muestra de cada empleado el sueldo
    def item4(self):
        i = 0
        while i < len(self.__arre):
            print('NOMBRE Y APELLIDO: %s - TELÉFONO: %d - SUELDO: $%d\n' % (self.__arre[i].getNom(), self.__arre[i].getTel(), self.__arre[i].getSueldo()))
            i += 1