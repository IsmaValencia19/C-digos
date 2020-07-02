class Provincia:
    __nombre = None
    __capital = None
    __cantidaddehabitantes = None
    __cantidaddedepartamentos = None

    def __init__(self, nombre = None, capital = None, cantidaddehabitantes = None, cantidaddedepartamentos = None, temperatura = None, sensaciontermica = None, humedad = None):
        self.__nombre = nombre
        self.__capital = capital
        self.__cantidaddehabitantes = cantidaddehabitantes
        self.__cantidaddedepartamentos = cantidaddedepartamentos

        self.__temperatura = temperatura
        self.__sensaciontermica = sensaciontermica
        self.__humedad = humedad

    def getNom(self):
        return self.__nombre

    def getCap(self):
        return self.__capital

    def getCantidadHabitantes(self):
        return self.__cantidaddehabitantes

    def getCantidadDepartamentos(self):
        return self.__cantidaddedepartamentos

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                capital = self.__capital,
                cantidaddehabitantes = self.__cantidaddehabitantes,
                cantidaddedepartamentos = self.__cantidaddedepartamentos
            )
        )
        return d