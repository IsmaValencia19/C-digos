class Helado:
    __gramos = 0

    def __init__(self, gramos = 0):
        self.__gramos = gramos

    def getGramos(self):
        return self.__gramos

    def __str__(self):
        return 'PESO: %s gs.' % (self.__gramos)