from claseFechaHora import FechaHora
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

        hora = FechaHora(20, 10, 2021, 22, 30, 30)
        print('Hora 1: ', hora)
        print()
        hora2 = FechaHora(20, 10, 1, 23, 50, 50)
        print('Hora 2: ', hora2)
        print()
        hora3 = hora + hora2
        print('Hora 1 + 2 = ', hora3)
        print()

        os.system("pause")
    
    def opcion2(self):
        os.system("cls")

        hora = FechaHora(20, 10, 2021, 22, 30, 30)
        print('Hora 1: ', hora)
        print()
        hora2 = FechaHora(20, 10, 1, 23, 50, 50)
        print('Hora 2: ', hora2)
        print()
        hora3 = hora - hora2
        print('Hora 1 - 2 = ', hora3)
        print()

        os.system("pause")

    def opcion3(self):
        os.system("cls")

        hora = FechaHora(11, 4, 21, 20)
        print('Hora 1: ', hora)
        print()
        hora2 = FechaHora(11, 4, 21, 21)
        print('Hora 2: ', hora2)
        print()
        if(hora > hora2):
            print('La primera hora es mayor que la segunda.')
        else:
            print("la segunda hora es mayor que la primera.")
        print()
        
        os.system("pause")