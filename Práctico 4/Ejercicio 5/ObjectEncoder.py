from ClaseManejadorPacientes import ManejadorPacientes
from ClasePaciente import Paciente
import json
from pathlib import Path
 
class ObjectEncoder(object):
    __pathArchivo = None

    def __init__(self, pathArchivo):
        self.__pathArchivo = pathArchivo

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'ManejadorPacientes':
                pacientes = d['pacientes']
                manejador = class_()
                for i in range(len(pacientes)):
                    dPaciente = pacientes[i]
                    class_name = dPaciente.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dPaciente['__atributos__']
                    unPaciente = class_(**atributos)
                    manejador.agregarPaciente(unPaciente)
            return manejador

    def guardarJSONArchivo(self, diccionario):
        with Path(self.__pathArchivo).open("w", encoding = "UTF-8") as destino:
            json.dump(diccionario, destino, indent = 4)
            destino.close()

    def leerJSONArchivo(self):
        with Path(self.__pathArchivo).open(encoding = "UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario