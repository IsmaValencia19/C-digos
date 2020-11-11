class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña =''

    def __init__(self, id = '', dom = '', tipdom = '', contra = ''):
        self.__idCuenta = id
        self.__dominio = dom
        self.__tipoDominio = tipdom
        self.__contraseña = contra

    def getDominio(self):
        return self.__dominio

    def setCont(self, contra):
        self.__contraseña = contra

    def getCont(self):
        return self.__contraseña

    def crearCuenta(self, correo):
        a, b = correo.split('@')
        b, c = b.split('.')
        mail = Email(a, b, c)
        return mail

    def __str__(self):
        return '%s@%s.%s' % (self.__idCuenta, self.__dominio, self.__tipoDominio)