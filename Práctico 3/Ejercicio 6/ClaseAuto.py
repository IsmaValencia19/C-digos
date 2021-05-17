class Auto:
    __modelo = ''
    __puertas = 0
    __color = ''
    __precio = 0

    def __init__(self, modelo, puertas, color, precio):
        self.__modelo = modelo
        self.__puertas = puertas
        self.__color = color
        self.__precio = precio
 
    def getModelo(self):
        return self.__modelo

    def getPuertas(self):
        return self.__puertas

    def getColor(self):
        return self.__color

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, precio):
        self.__precio = precio

    def mostrar(self):
        print('MODELO: %s - CANTIDAD DE PUERTAS: %s - COLOR: %s - PRECIO BASE: $%s' % (self.__modelo, self.__puertas, self.__color, self.getPrecio()))