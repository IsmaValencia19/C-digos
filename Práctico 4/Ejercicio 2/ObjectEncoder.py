from ClaseLista import Lista
from ClaseCasa import Casa
import json

class ObjectEncoder(object):
    def Guardar(self, elementos):
        archivo = 'dolar.json'
        with open(archivo, "w", encoding = "UTF-8") as destino:
            json.dump(elementos, destino, indent = 4)
            destino.close()

    def Leer(self):
        archivo = 'dolar.json'
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
                elementos = d['casas']
                lista = class_()
                for i in range(len(elementos)):
                    delemento = elementos[i]
                    class_name = delemento.pop("__class__")
                    class_ = eval(class_name)
                    atributos = delemento["__atributos__"]
                    unAuto = class_(**atributos)
                    lista.agregarElemento(unAuto)
                return lista