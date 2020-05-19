from ClaseManejaSabores import ManejaSabores
from ClaseManejaHelados import ManejaHelados
from ClaseHelado import Helado
import os

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4
                          }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, ms, mh):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(ms, mh)

    def salir(self, ms, mh):
        os.system("cls")
        cad = ' SALIÓ DEL PROGRAMA '
        print(cad.center(70, '='))
        print()

    def opcion1(self, ms, mh):
        os.system("cls")
        mh.RegistroVenta(ms)
        cad = ' VENTAS '
        print(cad.center(50, '='))
        print(mh)
        os.system("pause")

    def opcion2(self, ms, mh):
        os.system("cls")
        #c = ms.cantSabores()
        #print('Hay', c, 'sabores.')
        mh.most5sab(ms)
        os.system("pause")

    def opcion3(self, ms, mh):
        os.system("cls")
        print('opcion3')
        print()
        os.system("pause")

    def opcion4(self, ms, mh):
        os.system("cls")
        print('opcion4')
        print()
        os.system("pause")