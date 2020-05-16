class claseEmail:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña = ''

    def __init__(self, id = '', dom = '', tipdom = '', contra = ''):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipoDominio = tipdom
        self.__contraseña = contra
    def __str__(self):
        return '%s@%s.%s' % (self.__idCuenta, self.__dominio, self.__tipoDominio)
    def getDominio(self):
        return self.__dominio
    def setCont(self, contra):
        self.__contraseña = contra
    def getCont(self):
        return self.__contraseña