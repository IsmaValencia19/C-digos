class Capitulo:
    __titulo =''
    __cantPag = 0

    def __init__(self, tit = '', pag = 0):
        self.__titulo = tit
        self.__cantPag = pag

    def getTit(self):
        return self.__titulo

    def getPag(self):
        return self.__cantPag

    def __str__(self):
        return 'TÍTULO DEL CAPÍTULO: %s - CANTIDAD DE PÁGINAS: %s' % (self.__titulo, self.__cantPag)