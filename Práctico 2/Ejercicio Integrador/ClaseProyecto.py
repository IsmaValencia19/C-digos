class Proyecto:
    __id = ''
    __titulo = ''
    __palabrasClave = ''
    __puntaje = 0

    def __init__(self, ID = '', titulo = '', palabras = ''):
        self.__id = ID
        self.__titulo = titulo
        self.__palabrasClave = palabras
        self.__puntaje = 0

    def getId(self):
        return self.__id

    def getTitulo(self):
        return self.__titulo

    def getPuntaje(self):
        return self.__puntaje

    def ModificaPuntaje(self, puntaje):
        self.__puntaje += puntaje

    def __gt__(self, proyecto):
        return self.__puntaje < proyecto.getPuntaje()

    def __str__(self):
        return 'ID: %s - Titulo: %s - Palabras Claves: %s - Puntaje: %s' % (self.__id, self.__titulo, self.__palabrasClave, self.__puntaje)  