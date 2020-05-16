from ClaseHelado import Helado

class ManejaHelados:
    __lista = []

    def __init__(self):
        self.__lista = []

    def RegistroVenta(self):
        band = False
        i = 0
        tipoHelado = [100, 150, 250, 500, 1000]
        while not band:
            pesohelado = int(input('Ingrese peso de helado: '))
            if pesohelado == tipoHelado[i]:
                print('Tipo de helado elegido: %sgs.' % tipoHelado[i])
                band = True
            else:
                print('Tipo de helado incorrecto.')
                i += 1
        