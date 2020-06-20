class Casa:
    __compra = ''
    __venta = ''
    __agencia = ''
    __nombre = ''
    __variacion = ''
    __ventaCero = ''
    __decimales = ''

    def init (self, compra = '', venta = '', agencia = '', nombre = '', variacion = '', ventaCero = '', decimales = ''):
        self.__compra = compra
        self.__venta = venta
        self.__agencia = agencia
        self.__nombre = nombre
        self.__variacion = variacion
        self.__ventaCero = ventaCero
        self.__decimales = decimales

    def __str__(self):
        return 'Compra: %s - Venta: %s - Agencia: %s - Nombre: %s - Variación: %s - Venta Cero: %s - Decimales: %s' % (self.__compra, self.__venta, self.__agencia, self.__nombre, self.__variacion, self.__ventaCero, self.__decimales)