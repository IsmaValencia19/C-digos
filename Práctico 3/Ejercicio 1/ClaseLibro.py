from ClaseCapitulo import Capitulo
class Libro:
    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantCapitulos = 0
    __capitulo = []

    def __init__(self, id = 0, tit = '', aut = '', edit = '', isbn = 0, cap = 0):
        self.__idLibro = id
        self.__titulo = tit
        self.__autor = aut
        self.__editorial = edit
        self.__isbn = isbn
        self.__cantCapitulos = cap
        self.__capitulo = []

    def getId(self):
        return self.__idLibro

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def agregarCapitulo(self, cap):
        self.__capitulo.append(cap)

    def getCapitulos(self):
        return self.__capitulo

    def __str__(self):
        s = 'ID: %s - TÍTULO DEL LIBRO: %s - AUTOR: %s - EDITORIAL: %s - ISBN: %s - CANTIDAD DE CAPÍTULOS: %s\n' % (self.__idLibro, self.__titulo, self.__autor, self.__editorial, self.__isbn, self.__cantCapitulos)
        for capi in self.__capitulo:
            s += str(capi) + '\n'
        return s