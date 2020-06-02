from ClaseAuto import Auto

class AutoNuevo(Auto):
    __marca = 'Fiat'
    __version = ''

    def __init__(self, modelo, puertas, color, precio, version):
        super().__init__(modelo, puertas, color, precio)
        self.__version = version

    def toJSON(self):
        return dict(
                    __class__ = self.__class__.__name__,
                    __atributos__ = dict(
                                            modelo = self.getModelo(),
                                            puertas = self.getPuertas(),
                                            color = self.getColor(),
                                            precio = self.getPrecio(),
                                            version = self.__version
                                        )
                    )

    def __str__(self):
        super().mostrar()
        return 'MARCA: %s - VERSIÓN: %s' % (self.__marca, self.__version)