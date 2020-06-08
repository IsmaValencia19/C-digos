from ClaseLibro import Libro
from ClaseCapitulo import Capitulo
import csv

class ManejaLibro:
    __lista = []        #lista de los libros
    #__listapag = []     #lista de las páginas de cada libro

    def __init__(self):
        self.__lista = []
        #self.__listapag = []

    def agregar(self, libro):
        self.__lista.append(libro)

    #en esta función lo que hice fue, primero la carga de los libros, capitulos y segundo ir contando las páginas de cada libro
    def cargarLista(self):
        archivo = open('libros.csv')
        reader = csv.reader(archivo, delimiter = ',')
        #compa = 0   #esta variable la use para que cada componente de la "listapag" sea la cantidad de páginas de un libro
        #cont = 0    #contador de páginas
        for fila in reader:
            if len(fila) == 6:
                unLibro = Libro(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.agregar(unLibro)
                #compa += 1
                #if cont != 0:
                    #self.__listapag.append(cont)
                    #cont -= cont
            else:
                cap = Capitulo(fila[0], int(fila[1]))
                unLibro.agregarCapitulo(cap)
                #cont += cap.getPag()
        #if compa > 1:
        #    self.__listapag.append(cont)
        archivo.close()

    def getLista(self):
        return self.__lista

    #busca id, si lo encuentra retorna True y si no False
    def buscarId(self, id):
        '''i = 0
        band = False
        while i < len(self.__lista):
            if id == self.__lista[i].getId():
                i = len(self.__lista)
                band = True
            else:
                i += 1
        return band'''

        i = 0
        libro = None
        while i < len(self.__lista) and libro == None:
            if id == self.__lista[i].getId():
                libro = self.__lista[i]
            else:
                i += 1
        return libro

    #retorna la cantidad de páginas de un libro
    '''def getCantPaginas(self, id):'''
    def getCantPaginas(self, libro):
        '''i = 0
        cantpag = 0
        while i < len(self.__listapag):
            if (id - 10001) == i:
                cantpag = self.__listapag[i]
                i = len(self.__listapag)
            else:
                i += 1
        return cantpag'''

        cantpag = 0
        lista_capitulos = libro.getCapitulos()
        cada_capitulo = None
        i = 0
        while i < len(lista_capitulos):
            cada_capitulo = lista_capitulos[i]
            cantpag += cada_capitulo.getPag()
            i += 1
        return cantpag

    #retorna el titulo del ID ingresado
    def buscaTitulo(self, id):
        i = 0
        tit = ''
        while i < len(self.__lista):
            if id == self.__lista[i].getId():
                tit = self.__lista[i].getTitulo()
                i = len(self.__lista)
            else:
                i += 1
        return tit

    #muestra los capitulos de un libro
    def mostrarCapi(self, id):
        i = 0
        capi = []
        while i < len(self.__lista):
            if id == self.__lista[i].getId():
                capi = self.__lista[i].getCapitulos()
                i = len(self.__lista)
            else:
                i += 1
        for i in capi:
            print(i)
#item2: busca la palabra en el título de los libros
    def buscaPalabraenTitu(self, palabra):
        band = False
        i = 0
        while i < len(self.__lista):
            titLibro = self.__lista[i].getTitulo()
            if titLibro.find(palabra) != -1:
                tit = self.__lista[i].getTitulo()
                aut = self.__lista[i].getAutor()
                print('\nTítulo del libro: %s - Autor: %s' % (tit, aut))
                band = True
                i = len(self.__lista)
            else:
                i += 1
        return band

#item2: busca la palabra en el título de los capitulos
    def buscaPalabraenCapi(self, palabra):
        band = False
        i = 0
        while i < len(self.__lista):
            capi = self.__lista[i].getCapitulos()
            j = 0
            while j < len(capi):
                tit = capi[j].getTit()
                if tit.find(palabra) != -1:
                    tit = self.__lista[i].getTitulo()
                    aut = self.__lista[i].getAutor()
                    print('\nTítulo del libro: %s - Autor: %s' % (tit, aut))
                    band = True
                    j = len(capi)
                else:
                    j += 1
            i += 1
        return band
    
    def __str__(self):
        s = ''
        for libro in self.__lista:
            s += str(libro) + '\n'
        return s