from ClaseHelado import Helado
from ClaseManejaSabores import ManejaSabores

class ManejaHelados:
    __lista = []

    def __init__(self):
        self.__lista = []

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

    def RegistroVenta(self, ms):
        lista_helado = []
        band = False
        while not band:
            pesohelado = int(input('Ingrese peso de helado: '))
            if self.validaPeso(pesohelado) == True:
                print('Peso de helado correcto.')
                band = True
            else:
                print('Peso de helado incorrecto.')
        
        sabores = []
        saborHelado = input('Ingrese sabor de helado(Finaliza con "x"): ')
        while saborHelado != 'x':
            bande = False
            while not bande:
                if ms.validaSabor(saborHelado) == True:
                    print('Sabor correcto.')
                    bande = True
                else:
                    print('Sabor de helado incorrecto.')
                    saborHelado = input('Ingrese sabor de helado(Finaliza con "x"): ')
            sabores.append(saborHelado)
            saborHelado = input('Ingrese sabor de helado(Finaliza con "x"): ')
        unHelado = Helado(pesohelado)
        #lista_helado = [unHelado, sabores]
        self.agregar(unHelado)

    def __str__(self):
        s = ''
        for helado in self.__lista:
            s += str(helado) + '\n'
        return s