from ClaseAuto import Auto

class AutoUsado(Auto):
    __marca = ''
    __patente = ''
    __año = 0
    __km = 0

    def __init__(self, modelo, puertas, color, precio, marca, patente, año, kilometraje):
        super().__init__(modelo, puertas, color, precio)
        self.__marca = marca
        self.__patente = patente
        self.__año = año
        self.__kilometraje = kilometraje

    def getPat(self):
        return self.__patente

    def toJSON(self):
        return dict(
                    __class__ = self.__class__.__name__,
                    __atributos__ = dict(
                                            modelo = self.getModelo(),
                                            puertas = self.getPuertas(),
                                            color = self.getColor(),
                                            precio = self.getPrecio(),
                                            marca = self.__marca,
                                            patente = self.__patente,
                                            año = self.__año,
                                            kilometraje = self.__km
                                        )
                    )

    def __str__(self):
        super().mostrar()
        return 'MARCA: %s - PATENTE: %s - AÑO: %s - KILOMETRAJE: %s' % (self.__marca, self.__patente, self.__año, self.__km)