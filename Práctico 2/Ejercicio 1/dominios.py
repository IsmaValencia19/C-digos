from Clases import claseEmail
import csv
class contador:
    __lista = []
    
    def __init__(self):
        self.__lista = []

    def agregar(self, correo):
        self.__lista.append(correo)

    def dominios():
        archivo = open('correosparacontardominio.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            id = fila[0]
            dom = fila[1]
            tipdom = fila[2]
            contra = fila[3]
            uncorreo = claseEmail(id, dom, tipdom, contra)
            self.agregar(uncorreo)

    def buscardominio(self, domi):
        i = 0
        cont = 0
        while i < len(lista):
            if(self.__lista[i].getDominio == dominio):
                cont += 1
            i += 1
        return cont