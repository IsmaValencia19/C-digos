from ClaseLibro import Libro
from ClaseCapitulo import Capitulo
import csv

class ManejaLibro:
    __lista = []        

    def __init__(self):
        self.__lista = []

    def agregar(self, libro):
        self.__lista.append(libro)

    def cargarLista(self):
        archivo = open('libros.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            if len(fila) == 6:
                unLibro = Libro(int(fila[0]), fila[1], fila[2], fila[3], int(fila[4]), int(fila[5]))
                self.agregar(unLibro)
            else:
                cap = Capitulo(fila[0], int(fila[1]))
                unLibro.agregarCapitulo(cap)
        archivo.close()

    def buscarId(self, id):
        i = 0
        libro = None
        while i < len(self.__lista) and libro == None:
            if id == self.__lista[i].getId():
                libro = self.__lista[i]
                i = len(self.__lista)
            else:
                i += 1
        return libro

    #retorna la cantidad de páginas de un libro
    def getCantPaginas(self, libro):
        cantpag = 0
        lista_capitulos = libro.getCapitulos()
        cada_capitulo = None
        i = 0
        while i < len(lista_capitulos):
            cada_capitulo = lista_capitulos[i]
            cantpag += cada_capitulo.getPag()
            i += 1
        return cantpag

    #muestra los capitulos de un libro
    def mostrarCapi(self, libro):
        lista_capitulos = libro.getCapitulos()
        for cap in lista_capitulos:
            print(cap)

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