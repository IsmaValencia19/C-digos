class Helado:
    __gramos = 0
    __sabor = []

    def __init__(self, gramos, sabor):
        self.__gramos = gramos
        self.__sabor = sabor

    def getGramos(self):
        return self.__gramos

    def __str__(self):
        s = '\nSABOR/ES:\n'
        for sabor in self.__sabor:
            s += str(sabor) + '\n'
        s += 'PESO: %sgs' % (self.__gramos)
        return s