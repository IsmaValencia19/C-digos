from ClaseProvincia import Provincia
from ObjectEncoder import ObjectEncoder
from ClaseManejadorProvincias import ManejadorProvincias

class RepositorioProvincias(object):
    __conn = None
    __manejador = None

    def __init__(self, conn):
        self.__conn = conn
        diccionario = self.__conn.leerJSONArchivo()
        self.__manejador = self.__conn.decodificarDiccionario(diccionario)

    def to_values(self, provincia):
        return provincia.getNom(), provincia.getCap(), provincia.getCantidadHabitantes(), provincia.getCantidadDepartamentos(), provincia.getTemperatura(), provincia.getSensacionTermica(), provincia.getHumedad()

    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()

    def agregarProvincia(self, provincia):
        self.__manejador.agregarProvincia(provincia)
        return provincia

    def modificarProvincia(self, provincia):
        self.__manejador.actualizarProvincia(provincia)
        return provincia

    def borrarProvincia(self, provincia):
        self.__manejador.deleteProvincia(provincia)

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())