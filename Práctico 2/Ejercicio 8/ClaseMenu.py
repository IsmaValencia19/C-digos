from claseConjunto import Conjunto
from Validador import ValidaEntero
import os

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3
                          }
    
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    
    def salir(self):
        os.system('cls')
        print()
        print('>>>>>Salio del programa<<<<<')
        print()
   
    def opcion1(self):
        os.system("cls")

        print()
        print('Conjuntos:')
        print()
        A = [20, 30, 12]
        conjunto = Conjunto(A)
        conjunto.mostrar()
        print()
        B = [20, 1, 2, 3, 4]
        conjunto2 = Conjunto(B)
        conjunto2.mostrar()
        print()
        union = conjunto + conjunto2
        print('Unión de conjuntos:')
        print()
        union.mostrar()
        print()

        os.system("pause")
    
    def opcion2(self):
        os.system("cls")

        print()
        print('Conjuntos:')
        print()
        A = [20, 30, 12]
        conjunto = Conjunto(A)
        conjunto.mostrar()
        print()
        B = [20, 1, 2, 3, 4]
        conjunto2 = Conjunto(B)
        conjunto2.mostrar()
        print()
        diferencia = conjunto - conjunto2
        print('Diferencia de conjuntos:')
        print()
        diferencia.mostrar()
        print()

        os.system("pause")

    def opcion3(self):
        os.system("cls")

        print()
        print('Conjuntos:')
        print()
        A = [20, 30, 13, 6, 45, 7, 1]
        conjunto = Conjunto(A)
        conjunto.mostrar()
        print()
        B = [20, 13, 30, 1, 45, 6, 7]
        conjunto2 = Conjunto(B)
        conjunto2.mostrar()
        print()
        if(conjunto == conjunto2):
            print('Los conjuntos son iguales.\n')
        else:
            print('Los conjuntos no son iguales.\n')
        
        os.system("pause")