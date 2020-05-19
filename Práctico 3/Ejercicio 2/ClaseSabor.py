class Sabor:
    __num = 0
    __nom = ''
    __descripcion = ''

    def __init__(self, num = 0, nom = '', desc = ''):
        self.__num = num
        self.__nom = nom
        self.__descripcion = desc

    def getNom(self):
        return self.__nom

    def getId(self):
        return self.__num

    def __str__(self):
        return 'ID: %s - NOMBRE DE SABOR: %s - DESCRIPCIÓN: %s' % (self.__num, self.__nom, self.__descripcion)