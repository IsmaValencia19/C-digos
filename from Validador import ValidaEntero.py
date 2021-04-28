from Validador import ValidaEntero

class Conjunto:
    __listaConjuntos = []

    def __init__(self, lista = []):
        self.__listaConjuntos = lista

    def getLista(self):
        return self.__listaConjuntos

    def setLista(self, conjunto):
        self.__listaConjuntos = conjunto

    def generaelconjunto(self):
        elemento = ValidaEntero('Ingrese un elemento para el conjunto (Finalice con 00): ')
        while elemento != 00:
            self.__listaConjuntos.append(elemento)
            elemento = ValidaEntero('Ingrese un elemento para el conjunto (Finalice con 00): ')

    def ordenarLista(self):
        conjunto = Conjunto()
        conjunto.setLista(self.__listaConjuntos)
        longitud = len(conjunto.getLista())
        for i in range(longitud):
            for indice_actual in range(longitud - 1):
                indice_siguiente_elemento = indice_actual + 1
                if self.__listaConjuntos[indice_actual] > self.__listaConjuntos[indice_siguiente_elemento]:
                    self.__listaConjuntos[indice_siguiente_elemento], self.__listaConjuntos[indice_actual] = self.__listaConjuntos[indice_actual], self.__listaConjuntos[indice_siguiente_elemento]

    def __add__(self, otroConjunto):
        conjunto = self.__listaConjuntos
        conjunto.extend(otroConjunto.getLista())
        
        unicos = []

        for i in range(len(conjunto) -1, -1, -1):
            if conjunto[i] not in unicos:
                unicos.append(conjunto[i])
            else:
                conjunto.remove(conjunto[i])
        conjuntofinal = Conjunto()
        conjuntofinal.setLista(conjunto)
        return conjuntofinal
    
    def __sub__(self, otroConjunto):
        conjunto1 = self.__listaConjuntos
        conjunto2 = otroConjunto.getLista() 
        i = 0
        while i < len(conjunto2) - 1:
            j = 0
            while j < len(conjunto1) - 1:
                if(conjunto2[i] == conjunto1[j]):
                    conjunto1.remove(conjunto2[i])
                j += 1
            i += 1
        conjuntofinal = Conjunto()
        conjuntofinal.setLista(conjunto1)
        return conjuntofinal

    def __eq__(self, otroConjunto):
        primerconjunto = Conjunto()
        primerconjunto.setLista(self.__listaConjuntos)
        band = False
        primerconjunto.ordenarLista()
        segundoconjunto = Conjunto()
        segundoconjunto.setLista(otroConjunto)
        segundoconjunto.ordenarLista()
        if primerconjunto == segundoconjunto.getLista():
            band = True
        return band

    def mostrar(self):
        print(self.__listaConjuntos)