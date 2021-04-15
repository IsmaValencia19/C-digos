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
    
    def opcion(self, op, mv, viajero):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(mv, viajero)
    
    def salir(self, mv, viajero):
        os.system('cls')
        print()
        print('>>>>>Salio del programa<<<<<')
        print()
   
    def opcion1(self, mv, viajero):
        os.system("cls")
        print('\n{} es el ID de {}, que tiene {} millas acumuladas.'.format(viajero.getId(), viajero.getNom(), viajero.cantTotalMillas()))
        print()
        os.system("pause")
    
    def opcion2(self, mv, viajero):
        os.system("cls")
        millas = ValidaEntero('Ingrese millas para acumular: ')
        viajero.acumMillas(millas)
        print('\nCantidad de millas antes de actualizar: %s\n\nCantidad de millas actualizadas: %s' % ((viajero.cantTotalMillas() - millas), viajero.cantTotalMillas()))
        print()
        os.system("pause")
   
    def opcion3(self, mv, viajero):
        os.system("cls")
        print('Con quien desea canjear millas:')
        print(mv)
        band = False
        while not band:
            idcanjear = ValidaEntero('Ingrese ID de una persona para canjear millas: ')
            viajerocanjear = mv.buscarViajero(idcanjear)
            if viajerocanjear == None:
                print('\nLa persona con el ID: {} no existe.\n'.format(idcanjear))
            else:
                millascanje = ValidaEntero('\nIngrese millas para canje: ')
                if millascanje <= viajerocanjear.cantTotalMillas():
                    viajerocanjear.canjearMillas(millascanje)
                    viajero.acumMillas(millascanje)
                    print('\nMillas canjeadas con éxito.')
                else:
                    print('\nNo tiene millas suficientes.')
                band = True
        print()
        os.system("pause")