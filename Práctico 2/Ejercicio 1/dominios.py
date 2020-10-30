from ClaseEmail import Email
import csv
import re

class contador:
    __lista = []
    
    def __init__(self):
        self.__lista = []

    def agregar(self, correo):
        self.__lista.append(correo)

    def testing(self):
        archivo = open('10correos.csv')
        reader = csv.reader(archivo, delimiter = ',')
        i = 0
        for fila in reader:
            while i < len(fila):
                fila[i].find('@')
                nuevo_email = fila[i].split('@')
                usuario = nuevo_email[0]
                resto = nuevo_email[1]
                continuacion = resto.split('.')
                dominio = continuacion[0]
                tipodominio = continuacion[1]
                uncorreo = Email(usuario, dominio, tipodominio)
                self.agregar(uncorreo)
                i += 1
        archivo.close()

    def buscardominio(self, domi):
        cont = 0
        for elemento in self.__lista:
            dominio = elemento.getDominio()
            if domi == dominio:
                cont += 1
        return cont

    def __str__(self):
        s = ''
        for correos in self.__lista:
            s += str(correos) + '\n'
        return s