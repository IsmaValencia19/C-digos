from ClaseLista import Lista
from ClaseCasa import Casa
import json

class ObjectEncoder(object):
    def Guardar(self, elementos):
        archivo = 'dolares.json'
        with open(archivo, "w", encoding = "UTF-8") as destino:
            json.dump(elementos, destino, indent = 4)
            destino.close()

    def Leer(self):
        archivo = 'dolares.json'
        with open(archivo, encoding = "UTF-8") as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario

    def Decoder(self, d):
        if "__class__" not in d:
            return d
        else:
            lista = []
            for i in range(len(elementos)):
                delemento = elementos[i]
                class_name = delemento.pop("__class__")
                class_ = eval(class_name)
                atributos = delemento["__atributos__"]
                unaCasa = class_(**atributos)
                lista.append(unaCasa)
            return lista