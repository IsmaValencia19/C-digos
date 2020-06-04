from ClaseDocenteInvestigador import DocenteInvestigador
from ClasePersonaldeApoyo import PersonaldeApoyo
from ClaseInvestigador import Investigador
from ClaseDocente import Docente
from ClaseLista import Lista
import json

class ObjectEncoder(object):
    def Guardar(self, elementos):
        archivo = 'personal.json'
        with open(archivo, "w", encoding = "UTF-8") as destino:
            json.dump(elementos, destino, indent = 4)
            destino.close()

    def Leer(self):
        archivo = 'personal.json'
        with open(archivo, encoding = "UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def Decoder(self, d):
        if "__class__" not in d:
            return d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == 'Lista':
                elementos = d['personal']
                lista = class_()
                for i in range(len(elementos)):
                    delemento = elementos[i]
                    class_name = delemento.pop("__class__")
                    class_ = eval(class_name)
                    atributos = delemento["__atributos__"]
                    unPersonal = class_(**atributos)
                    lista.agregarElemento(unPersonal)
                return lista