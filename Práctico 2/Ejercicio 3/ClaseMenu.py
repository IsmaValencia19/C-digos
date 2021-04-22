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
    
    def opcion(self, op, cam, cos):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(cam, cos)
    
    def salir(self, cam, cos):
        os.system('cls')
        print()
        print('>>>>>Salio del programa<<<<<')
        print()
   
    def opcion1(self, cam, cos):
        os.system("cls")

        kilos = 0
        band = False
        while not band:
            camion = cam.buscaCamion(ValidaEntero('Ingrese ID de camión: '))
            if camion != None:
                cos.kilos(camion.getId(), camion.getTara())
                band = True
            else:
                print('\nEl ID de camión ingresado no existe.\n')

        print()
        os.system("pause")
    
    def opcion2(self, cam, cos):
        os.system("cls")
        cosechas = cos.getLista()
        band = False
        while not band:
            dia = ValidaEntero('Ingrese un dia: ')
            if ( dia >= 1 and dia <= 45 ):
                print('\n%10s' % 'PATENTE', '%13s' % 'NOMBRE', '%10s' % 'KILOS')
                for i in range(20):
                    camion = cam.buscaCamion(i + 1)
                    print('%10s' % (camion.getPat()), '%13s' % (camion.getCond()), '%10s' % (cosechas.getValor((camion.getId()) - 1, dia - 1)))
                band = True
            else:
                print('\nEl dia ingresado es incorrecto.\n')
        print()
        os.system("pause")

    def opcion3(self, cam, cos):
        os.system("cls")
        band = False
        while not band:
            ID = ValidaEntero('Ingrese ID de camión: ')
            if ID > 0 and ID < 21:
                camion = cam.buscaCamion(ID)
                dia = ValidaEntero('Ingrese dia: ')
                if dia > 0 and dia < 46:
                    kg = ValidaEntero('Ingrese kilos: ')
                    tara = int(camion.getTara())
                    cosechas = cos.getLista()
                    cosechas.agregarKG(ID - 1, dia - 1, kg - tara)
                    band = True
                else:
                    print('\nERROR: El dia ingresado no es valido.\n')
            else:
                print('\nERROR: El ID de camión ingresado no es valido.\n')
        print('\nDatos registrado con éxito!')
        print()
        os.system("pause")