from ClaseHelado import Helado
from ClaseManejaSabores import ManejaSabores
import numpy as np

class ManejaHelados:
    __lista = []
    __contSabores = 0   #variable usada para contar las veces que se pide un sabor

    def __init__(self):
        self.__lista = []
        self.__contSabores = 0

    def agregar(self, helado):
        self.__lista.append(helado)

    def validaPeso(self, peso):
        band = False
        tiposHelados = [100, 150, 250, 500, 1000]
        i = 0
        while i < len(tiposHelados):
            if peso == tiposHelados[i]:
                band = True
                i = len(tiposHelados)
            else:
                i += 1
        return band

    #en esta función convierto el contador que esta en atributos en un arreglo numpy
    def arreglo(self, ms):
        cantSabor = ms.cantSabores()
        self.__contSabores = np.full(cantSabor, 0)

    def RegistroVenta(self, ms):
        self.arreglo(ms)
        cad = ' REGISTRAR VENTA '
        print(cad.center(50, '='))
        pesohelado = int(input('Ingrese peso de helado(Finaliza con 0): '))
        while pesohelado != 0:
            band = False
            while not band:
                if self.validaPeso(pesohelado) == True:
                    print('Peso de helado correcto.')
                    band = True
                else:
                    print('Peso de helado incorrecto.')
                    pesohelado = int(input('Ingrese peso de helado: '))
            
            sabores = []
            print(ms)
            idHelado = int(input('Ingrese ID de helado(Finaliza con 0): '))
            while idHelado != 0:
                bande = False
                while not bande:
                    if ms.validaSabor(idHelado) == True:
                        print('Sabor correcto.')
                        self.__contSabores[idHelado - 1] += 1
                        sabor = ms.getSabor(idHelado)
                        bande = True
                    else:
                        print('Sabor de helado incorrecto.')
                        idHelado = int(input('Ingrese ID de helado: '))
                        self.__contSabores[idHelado - 1] += 1
                        sabor = ms.getSabor(idHelado)
                        
                sabores.append(sabor)
                idHelado = int(input('Ingrese ID de helado(Finaliza con 0): '))

            unHelado = Helado(pesohelado, sabores)
            self.agregar(unHelado)

            pesohelado = int(input('Ingrese peso de helado(Finaliza con 0): '))

    def most5sab(self, ms):
        cont = self.__contSabores
        ms.b5sabores(cont)

    def __str__(self):
        s = ''
        for helado in self.__lista:
            s += str(helado) + '\n'
        return s