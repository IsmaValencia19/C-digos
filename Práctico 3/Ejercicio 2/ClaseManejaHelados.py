from ClaseHelado import Helado
from ClaseManejaSabores import ManejaSabores
from Validador import ValidaEntero
import numpy as np
import os

class ManejaHelados:
    __lista = []
    __contSabores = 0   #variable usada para contar las veces que se pide un sabor
    __acumgramos = 0
    __tipoHelado = []
    __listsab = []

    def __init__(self):
        self.__lista = []
        self.__contSabores = np.full(6, 0)
        self.__acumgramos = np.full(6, 0)
        self.__tipoHelado = [100, 150, 250, 500, 1000]
        self.__listsab = [[], [], [], [], []]

    def agregar(self, helado):
        self.__lista.append(helado)

    #esta función agrega los sabores a un tipo de helado
    def agregarlista(self, sabores, num):
        i = 0
        while i < 5:
            j = 0
            while j < 5:
                if num == i:
                    self.__listsab[i].append(sabores)
                    j = 5
                else:
                    j += 1
            i += 1

    def validaPeso(self, tipo):
        band = False
        i = 0
        while i < len(self.__tipoHelado):
            if tipo == i:
                band = True
                i = len(self.__tipoHelado)
            else:
                i += 1
        return band

    #cuenta por sabor las veces que se pide
    def acumular(self, id):
        self.__contSabores[id - 1] += 1

    #acumula por sabor los gramos vendidos
    def acumgramo(self, ids, gr):
        i = 0
        while i < len(self.__acumgramos):
            j = 0
            while j < len(ids):
                if ids[j] == i:
                    self.__acumgramos[i] += gr
                j += 1
            i += 1

    def RegistroVenta(self, ms):
        cad = ' REGISTRAR VENTA '
        print(cad.center(50, '='))
        
        i = 0
        while i < len(self.__tipoHelado):       #lista los tipos de helado
            print('Tipo de helado %s - %s gs.' % (i+1, self.__tipoHelado[i]))
            i += 1

        band = False
        while not band:
            tipohelado = ValidaEntero('Ingrese tipo de helado: ')
            if self.validaPeso(tipohelado - 1) == True:
                #print('Peso de helado correcto.')
                band = True
            else:
                print('Tipo de helado incorrecto.')
            
        sabores = []
        listadeids = []
        print()
        t = 0
        os.system('cls')
        print('Eligió el tipo de helado de {}gs.\n'.format(self.__tipoHelado[tipohelado - 1]))
        print(ms)   #muestra los sabores disponibles
        print('Una venta de helado incluye de 1 a 4 sabores.')
        idSabor = ValidaEntero('Ingrese ID de sabor(Finalice con 0): ')
        while (idSabor != 0) and (0 <= t < 4):
            bande = False
            while not bande:
                if ms.validaSabor(idSabor) == True:
                    #print('ID de sabor correcto.')
                    self.acumular(idSabor)
                    sabor = ms.getSabor(idSabor)
                    listadeids.append(idSabor - 1)
                    bande = True
                else:
                    print('ID de sabor incorrecto.')

            sabores.append(sabor)
            t += 1
            idSabor = int(input('Ingrese ID de sabor(Finalice con 0): '))

        self.agregarlista(sabores, tipohelado - 1)      #agrega los sabores a la lista por tipo de helado
        pesohelado = self.__tipoHelado[tipohelado - 1]
        gramos = pesohelado / len(sabores)
        self.acumgramo(listadeids, gramos)  #acumula los gramos de un sabor
        unHelado = Helado(pesohelado, sabores)
        self.agregar(unHelado)

    def most5sab(self, ms):
        cont = self.__contSabores   
        ms.b5sabores(cont)      #función de manejasabor

    def mostraracum(self, ms):
        acum = self.__acumgramos
        ms.gramosabor(acum)

    def item4(self):
        band = False
        while not band:
            tipo = ValidaEntero('Ingrese un tipo de helado(1...5): ')
            if self.validaPeso(tipo - 1) == True:
                #print('Tipo de helado valido.')
                band = True
            else:
                print('Tipo de helado incorrecto.')
        
        i = 0
        while i < 5:
            if (tipo - 1) == i:
                print('Tipo de helado %s - Sabores Vendidos: %s' % (i+1, self.__listsab[i]))
            i += 1

    def __str__(self):
        s = ''
        for helado in self.__lista:
            s += str(helado) + '\n'
        return s