class Helado:
    __gramos = 0
    __sabor = []

    def __init__(self, gramos, sabor):
        self.__gramos = gramos
        self.__sabor = sabor

    def getGramos(self):
        return self.__gramos

    def __str__(self):
        s = 'PESO %sgs\n' % (self.__gramos)
        for sabor in self.__sabor:
            s += str(sabor) + '\n'
        return s