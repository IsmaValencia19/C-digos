class Casa:
    __nombre = ''
    __compra = 0
    __venta = 0
    __agencia = 0
    __observaciones = None
    __geolocalizacion = None
    __telefono = 0
    __direccion = ''
    __decimales = 0

    def __init__(self, nombre = '', compra = 0, venta = 0, agencia = 0, observaciones = None, geolocalizacion = None, telefono = 0, direccion = '', decimales = 0):
        self.__nombre = nombre
        self.__compra = compra
        self.__venta = venta
        self.__agencia = agencia
        self.__observaciones = observaciones
        self.__geolocalizacion = geolocalizacion
        self.__telefono = telefono
        self.__direccion = direccion
        self.__decimales = decimales

    def getNombre(self):
        return self.__nombre

    def getCompra(self):
        return self.__compra

    def getVenta(self):
        return self.__venta

    def getAgencia(self):
        return self.__agencia

    def getObservaciones(self):
        return self.__observaciones

    def getGeolocalizacion(self):
        return self.__geolocalizacion

    def getTelefono(self):
        return self.__telefono

    def getDireccion(self):
        return self.__direccion

    def getDecimales(self):
        return self.__decimales

    def __str__(self):
        return 'Nombre: %s - Compra: %s - Venta: %s - Agencia: %s - Observaciones: %s - Geolocalización: %s - Telefono: %s - Dirección: %s - Decimales: %s' % (self.__nombre, self.__compra, self.__venta, self.__agencia, self.__observaciones, self.__geolocalizacion, self.__telefono, self.__direccion, self.__decimales)        