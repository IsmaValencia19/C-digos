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

    def opcion(self, op, me):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(me)

    def salir(self, me):
        os.system("cls")
        cad = ' SALIO DEL PROGRAMA '
        print(cad.center(70, '='))
        print()

    def opcion1(self, me):
        os.system("cls")
        me.item1()
        os.system("pause")
        
    def opcion2(self, me):
        os.system("cls")
        me.item2()
        print()
        os.system("pause")
        
    def opcion3(self, me):
        os.system("cls")
        me.item3()
        os.system("pause")
        
    def opcion4(self, me):
        os.system("cls")
        me.item4()
        os.system("pause")