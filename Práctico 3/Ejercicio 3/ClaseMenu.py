import os

class Menu:
    __switcher = None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.opcion8
                          }
    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, mt, mp, mi):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mt, mp, mi)

    def salir(self, mt, mp, mi):
        os.system("cls")
        cad = ' SALIÓ DEL PROGRAMA '
        print(cad.center(50, '='))

    def opcion1(self, mt, mp, mi):
        os.system("cls")
        mp.registrar(mt, mi)
        print()
        os.system("pause")
    
    def opcion2(self, mt, mp, mi):
        os.system("cls")
        mp.consultaInscripcion(mt)
        print()
        os.system("pause")
    
    def opcion3(self, mt, mp, mi):
        os.system("cls")
        print('opcion')
        print()
        os.system("pause")
    
    def opcion4(self, mt, mp, mi):
        os.system("cls")
        print('opcion')
        print()
        os.system("pause")
    
    def opcion5(self, mt, mp, mi):
        os.system("cls")
        print('opcion')
        print()
        os.system("pause")

    def opcion6(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE TALLERES<<<<<')
        print()
        print(mt)
        os.system("pause")

    def opcion7(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE PERSONAS<<<<<')
        print()
        print(mp)
        os.system("pause")

    def opcion8(self, mt, mp, mi):
        os.system("cls")
        print('>>>>>MANEJADOR DE INSCRIPCIONES<<<<<')
        print(mi)
        print()
        os.system("pause")