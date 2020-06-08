from ClaseLibro import Libro
from ClaseCapitulo import Capitulo
from ClaseManejaLibros import ManejaLibro
import os

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2
                          }
    
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, ml):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(ml)
    
    def salir(self, ml):
        print()
        print('>>>>>Salio del programa<<<<<')
        print()
   
    def opcion1(self, ml):
        os.system("cls")
        libro = None
        band = False
        while not band:
            id = int(input('Ingrese ID: '))
            libro = ml.buscarId(id)
            if libro != None:
                band = True
            else:
                print('ERROR: El ID es incorrecto.\n')
        print('\nTÍTULO DEL LIBRO: %s' % libro.getTitulo())
        ml.mostrarCapi(libro)
        paginas = ml.getCantPaginas(libro)
        print('CANTIDAD DE PÁGINAS DEL LIBRO: %s' % paginas)
        print()
        os.system("pause")
    
    def opcion2(self, ml):
        os.system("cls")
        band = False
        while not band:
            palabra = input('Ingrese palabra a buscar: ')
            if ml.buscaPalabraenTitu(palabra) == True:
                print('\nLa palabra esta en el título de un libro.')
                band = True
            else:
                print('\nLa palabra no esta en el título de un libro.')
                if ml.buscaPalabraenCapi(palabra) == True:
                    print('\nLa palabra esta en el titulo de un capitulo.')
                    band = True
                else:
                    print('La palabra no esta en el titulo de un capitulo.')
        print()
        os.system("pause")