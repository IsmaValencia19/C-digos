from ClaseManejaSabores import ManejaSabores
from Validador import ValidaEntero
from ClaseHelado import Helado
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
            if num == i:
                self.__listsab[i] += sabores
                i = 5
            else:
                i += 1

    def validaPeso(self):
        band = False
        while not band:
            tipohelado = ValidaEntero('Ingrese tipo de helado: ')
            i = 0
            while i < len(self.__tipoHelado):
                if (tipohelado - 1) == i:
                    band = True
                    tipohelado -= 1
                    i = len(self.__tipoHelado)
                else:
                    i += 1
            if not band:
                print('\nERROR: Tipo de helado incorrecto.\n')
        return tipohelado

    #cuenta por sabor las veces que se pide
    def acumular(self, id):
        self.__contSabores[id - 1] += 1

    #acumula por sabor los gramos vendidos
    def acumgramo(self, ids, gr):
        i = 0
        while i < len(self.__acumgramos):
            j = 0
            while j < len(ids):
                if ids[j] == i:   #compara los ids de la venta de un helado con los ids registrados para acumular gramos
                    self.__acumgramos[i] += gr
                j += 1
            i += 1

    def MostrarTipoHelados(self):
        i = 0
        while i < len(self.__tipoHelado):
            print('Tipo de helado %s - %s gs.' % (i+1, self.__tipoHelado[i]))
            i += 1

    def RegistroVenta(self, ms):
        cad = ' REGISTRAR VENTA '
        print(cad.center(50, '='))
        self.MostrarTipoHelados()
        tipohelado = self.validaPeso()  # se ingresa el tipo de helado
        sabores = []    #lista utilizada para guardar los sabores de un helado vendido
        listadeids = []     #lista utilizada para guardar los id de los sabores 
        print()
        os.system('cls')
        print('Eligió el tipo de helado de {}gs.\n'.format(self.__tipoHelado[tipohelado]))
        print(ms)   #muestra los sabores disponibles
        print('Una venta de helado incluye de 1 a 4 sabores.')
        t = 0  #variable utilizada para verificar que se puede comprar hasta cuatro sabores
        while 0 <= t < 4:
            bande = False
            while not bande:
                idSabor = ValidaEntero('Ingrese ID de sabor(Finalice con 0): ')
                if idSabor == 0:  # verifica si el id del sabor es 0 para salir del menú de elección de sabores
                    bande = True
                    t = 4
                else:
                    sabor = ms.buscarSabor(idSabor)
                    if sabor != None:
                        #print('Sabor correcto.')
                        sabores.append(sabor)
                        self.acumular(idSabor)
                        listadeids.append(idSabor - 1)
                        bande = True
                    else:
                        print('ID de sabor incorrecto.')
            t += 1
        self.agregarlista(sabores, tipohelado)   #agrega los sabores a la lista por tipo de helado
        pesohelado = self.__tipoHelado[tipohelado]
        gramos = pesohelado / len(sabores)
        self.acumgramo(listadeids, gramos)  #acumula los gramos de un sabor
        unHelado = Helado(pesohelado, sabores)
        self.agregar(unHelado)

    def mostrar5sabores(self, ms):
        cont = self.__contSabores   
        ms.cincoSabores(cont)      #función de manejasabor

    def mostraracum(self, ms):
        acum = self.__acumgramos
        ms.gramosabor(acum)

    def item4(self):
        self.MostrarTipoHelados()
        tipo = self.validaPeso()
        print('\nSabores vendidos para el tipo de helado %s:' % (tipo + 1))
        i = 0
        while i < 5:
            if tipo == i:
                if self.__listsab[i] != []:  # verifica si tiene sabores vendidos
                    lista_nueva = []  # lista usada para guardar los sabores que no estan repetidos
                    for e in self.__listsab[i]:   # for usado para verificar si hay sabores repetidos los elimina
                        if e not in lista_nueva:
                            lista_nueva.append(e)
                    j = 0
                    while j < len(lista_nueva):
                        print('- %s' % (lista_nueva[j].getNom()))
                        j += 1
                    i = 5
                else:
                    print('No vendieron sabores para este tipo de helado.')
                    i = 5
            else:
                i += 1

    def __str__(self):
        s = ''
        for helado in self.__lista:
            s += str(helado) + '\n'
        return s