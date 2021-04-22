from ClaseIntegrante import Integrante
import csv

class ManejadorIntegrante:
    __integrantes = []

    def __init__(self):
        self.__integrantes = []

    def agregar(self, integrante):
        self.__integrantes.append(integrante)

    def carga(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                'saltear cabecera'
                bandera = not bandera
            else:
                ID = fila[0]
                apenom = fila[1]
                dni = fila[2]
                categ = str(fila[3])
                rol = str(fila[4])
                integrante = Integrante(ID, apenom, dni, categ, rol)
                self.agregar(integrante)
        archivo.close()

    def getLista(self):
        return self.__integrantes

    def __str__(self):
        s = ''
        for integ in self.__integrantes:
            s += str(integ) + '\n'
        return s 