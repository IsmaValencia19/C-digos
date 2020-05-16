class claseConjunto:
    __listaConjuntos = []

    def __init__(self, lista = []):
        if(type(lista) == type(self.__listaConjuntos)):
            self.__listaConjuntos = lista
        else:
            print("Los datos deben ser de tipo lista.")
    
    def getLista(self):
        return self.__listaConjuntos

    def mostrar(self):
        print(self.__listaConjuntos)

    #Sobrecarga de Operador "+"
    def __add__(self, otroConjunto):
        union = claseConjunto(self.__listaConjuntos)
        lista = union.getLista()
        lista.extend(otroConjunto.getLista())
        
        unicos = []

        for i in range(len(lista) -1, -1, -1):
            if lista[i] not in unicos:
                unicos.append(lista[i])
            else:
                lista.remove(lista[i])
        return lista
    
    #Sobrecarga de Operador "-"
    def __sub__(self, otroConjunto):
        primerlista = claseConjunto(self.__listaConjuntos)
        lista1 = primerlista.getLista()
        lista2 = otroConjunto.getLista() 
        i = 0
        while i < len(lista2) - 1:
            j = 0
            while j < len(lista1) - 1:
                if(lista2[i] == lista1[j]):
                    lista1.remove(lista2[i])
                j += 1
            i += 1
        return lista1

    #Sobrecarga de Operador "=="
    def __eq__(self, otroConjunto):
        primerlista = claseConjunto(self.__listaConjuntos)
        lista1 = primerlista.getLista()
        lista2 = otroConjunto.getLista()
        return lista1, lista2