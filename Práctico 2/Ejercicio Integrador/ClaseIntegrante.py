class Integrante:
    __idProyecto = ''
    __apellidoNombre = ''
    __dni = ''
    __categoria = ''
    __rol = ''

    def __init__(self, ID = '', apenom = '', dni = '', categ = '', rol = ''):
        self.__idProyecto = ID
        self.__apellidoNombre = apenom
        self.__dni = dni
        self.__categoria = categ
        self.__rol = rol

    def getId(self):
        return self.__idProyecto

    def getCategoria(self):
        return self.__categoria

    def getRol(self):
        return self.__rol

    def __str__(self):
        return 'ID Proyecto: %s - Nombre y Apellido: %s - DNI: %s - Categoria: %s - Rol: %s' % (self.__idProyecto, self.__apellidoNombre, self.__dni, self.__categoria, self.__rol)