from ClaseIntegrante import Integrante
from ClaseProyecto import Proyecto
import csv

class ManejadorProyecto:
    __proyectos = []

    def __init__(self):
        self.__proyectos = []

    def agregar(self, proyecto):
        self.__proyectos.append(proyecto)

    def getLista(self):
        return self.__proyectos

    def carga(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                'saltear cabecera'
                bandera = not bandera
            else:
                ID = fila[0]
                titulo = fila[1]
                palabras = fila[2]
                proyecto = Proyecto(ID, titulo, palabras)
                self.agregar(proyecto)
        archivo.close()

    def asignarpuntaje(self, integrantes):
        cont = 0  # contador de integrantes
        director = False # se usa para saber si tiene director o no
        codirector = False  # se usa para saber si tiene codirector o no

        for i in range(len(self.__proyectos)):
            for j in range(len(integrantes)):
                if integrantes[j].getId() == self.__proyectos[i].getId():
                    cont += 1
                    if integrantes[j].getRol() == 'director':
                        director = True
                        if integrantes[j].getCategoria() == "I":
                            self.__proyectos[i].ModificaPuntaje(10)
                        elif integrantes[j].getCategoria() == "II":
                            self.__proyectos[i].ModificaPuntaje(10)
                        else:
                            self.__proyectos[i].ModificaPuntaje(-5)
                            print('El director del Proyecto "%s", debe tener categoría I o II.' % (self.__proyectos[i].getTitulo()))
                    elif integrantes[j].getRol() == 'codirector':
                        codirector = True
                        if integrantes[j].getCategoria() == 'I':
                            self.__proyectos[i].ModificaPuntaje(10)
                        elif integrantes[j].getCategoria() == 'II':
                            self.__proyectos[i].ModificaPuntaje(10)
                        elif integrantes[j].getCategoria() == 'III':
                            self.__proyectos[i].ModificaPuntaje(10)
                        else:
                            self.__proyectos[i].ModificaPuntaje(-5)
                            print('El codirector del Proyecto "%s", debe tener categoría I, II o III.' % (self.__proyectos[i].getTitulo()))
            if cont >= 3:
                self.__proyectos[i].ModificaPuntaje(10)
                cont = 0
            else:
                self.__proyectos[i].ModificaPuntaje(-20)
                print('El Proyecto "%s", debe tener como mínimo 3 integrantes' % (self.__proyectos[i].getTitulo()))
                
            if not director:
                self.__proyectos[i].ModificaPuntaje(-10)
                print('El proyecto "%s" debe tener un director.' % (self.__proyectos[i].getTitulo()))
            elif not codirector:
                if director:
                    self.__proyectos[i].ModificaPuntaje(-10)
                    print('El proyecto "%s" debe tener un codirector.' % (self.__proyectos[i].getTitulo()))

    def ordenar(self):
        proyectos = sorted(self.__proyectos)
        for pro in proyectos:
            print(pro)

    def __str__(self):
        s = ''
        for proye in self.__proyectos:
            s += str(proye) + '\n'
        return s