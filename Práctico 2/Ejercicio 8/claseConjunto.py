class Conjunto:
    __listaConjuntos = []

    def __init__(self, lista = []):
        if(type(lista) == type(self.__listaConjuntos)):
            self.__listaConjuntos = lista
        else:
            print("Los datos deben ser de tipo lista.")
    
    def getLista(self):
        return self.__listaConjuntos

    def ordenarLista(self):
        longitud = len(self.__listaConjuntos)
        for i in range(longitud):
            for indice_actual in range(longitud - 1):
                indice_siguiente_elemento = indice_actual + 1
                if self.__listaConjuntos[indice_actual] > self.__listaConjuntos[indice_siguiente_elemento]:
                    self.__listaConjuntos[indice_siguiente_elemento], self.__listaConjuntos[indice_actual] = self.__listaConjuntos[indice_actual], self.__listaConjuntos[indice_siguiente_elemento]

    def __add__(self, otroConjunto):
        union = Conjunto(self.__listaConjuntos)
        conjunto = union.getLista()
        conjunto.extend(otroConjunto.getLista())
        
        unicos = []

        for i in range(len(conjunto) -1, -1, -1):
            if conjunto[i] not in unicos:
                unicos.append(conjunto[i])
            else:
                conjunto.remove(conjunto[i])
        conjuntofinal = Conjunto(conjunto)
        return conjuntofinal
    
    def __sub__(self, otroConjunto):
        primerconjunto = Conjunto(self.__listaConjuntos)
        conjunto1 = primerconjunto.getLista()
        conjunto2 = otroConjunto.getLista() 
        i = 0
        while i < len(conjunto2) - 1:
            j = 0
            while j < len(conjunto1) - 1:
                if(conjunto2[i] == conjunto1[j]):
                    conjunto1.remove(conjunto2[i])
                j += 1
            i += 1
        conjuntofinal = Conjunto(conjunto1)
        return conjuntofinal

    def __eq__(self, otroConjunto):
        primerconjunto = Conjunto(self.__listaConjuntos)
        band = False
        primerconjunto.ordenarLista()
        otroConjunto.ordenarLista()
        if primerconjunto.getLista() == otroConjunto.getLista():
            band = True
        return band

    def mostrar(self):
        print(self.__listaConjuntos)