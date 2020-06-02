from ClaseAutoNuevo import AutoNuevo
from ClaseAutoUsado import AutoUsado
from ClaseNodo import Nodo
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
                            7:self.opcion7
                          }

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, autos):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(autos)

    def salir(self, a):
        os.system("cls")
        cad = ' SALIÓ DEL PROGRAMA '
        print(cad.center(50, '='))
        print()

    def opcion1(self, a):
        os.system("cls")
        bande = False
        while not bande:
            band = False
            print('== INSERTA VEHÍCULO A LA COLECCIÓN EN UNA POSICIÓN DETERMINADA ==')
            op = int(input('ingrese |1| si el estado del vehículo es Nuevo, si es usado |2|: '))
            if op == 1:
                print('\n>>>>>>>>>>REGISTRANDO VEHÍCULO NUEVO<<<<<<<<<<')
                modelo = input('Ingrese el modelo(ej. Palio, Focus, etc): ')
                puertas = int(input('Ingrese número de puertas: '))
                color = input('Ingrese color: ')
                precio = int(input('Ingrese precio: '))
                while not band:
                    version = input('Ingrese versión(Full o Base): ')
                    if (version.capitalize() == 'Full') or (version.capitalize() == 'Base'):
                        band = True
                    else:
                        print('ERROR, versión incorrecta.')
                        version = input('Ingrese versión(Full o Base): ')
                posicion = int(input('Ingrese posición en la que desea insertar el vehículo: '))
                unAutoNuevo = AutoNuevo(modelo.capitalize(), puertas, color.capitalize(), precio, version.capitalize())
                a.insertarElemento(unAutoNuevo, posicion - 1)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.')
                bande = True
            elif op == 2:
                print('\n>>>>>>>>>>REGISTRANDO VEHÍCULO USADO<<<<<<<<<<')
                modelo = input('Ingrese el modelo(ej. Palio, Focus, etc): ')
                puertas = int(input('Ingrese número de puertas: '))
                color = input('Ingrese color: ')
                precio = int(input('Ingrese precio: '))
                marca = input('Ingrese marca: ')
                patente = input('Ingrese patente: ')
                año = int(input('Ingrese año de fabrica: '))
                kilometraje = int(input('Ingrese kilometraje: '))
                posicion = int(input('Ingrese posición en la que desea insertar el vehículo: '))
                unAutoUsado = AutoUsado(modelo.capitalize(), puertas, color.capitalize(), precio, marca.capitalize(), patente, año, kilometraje)
                a.insertarElemento(unAutoUsado, posicion - 1)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.')
                bande = True
            else:
                print('ERROR, opción incorrecta.')

        os.system("pause")
    
    def opcion2(self, a):
        os.system("cls")
        bande = False
        while not bande:
            band = False
            print('================== AGREGAR VEHÍCULO A LA COLECCIÓN ==================')
            op = int(input('ingrese |1| si el estado del vehículo es Nuevo, si es usado |2|: '))
            if op == 1:
                print('\n>>>>>>>>REGISTRANDO VEHÍCULO NUEVO<<<<<<<<')
                modelo = input('Ingrese el modelo(ej. Palio, Focus, etc): ')
                puertas = int(input('Ingrese número de puertas: '))
                color = input('Ingrese color: ')
                precio = int(input('Ingrese precio: '))
                while not band:
                    version = input('Ingrese versión(Full o Base): ')
                    if (version.capitalize() == 'Full') or (version.capitalize() == 'Base'):
                        band = True
                    else:
                        print('ERROR, versión incorrecta.')
                        version = input('Ingrese versión(Full o Base): ')
                unAutoNuevo = AutoNuevo(modelo.capitalize(), puertas, color.capitalize(), precio, version.capitalize())
                a.agregarElemento(unAutoNuevo)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.')
                print()
                bande = True
            elif op == 2:
                print('\n>>>>>>>>REGISTRANDO VEHÍCULO USADO<<<<<<<<')
                modelo = input('Ingrese el modelo(ej. Palio, Focus, etc): ')
                puertas = int(input('Ingrese número de puertas: '))
                color = input('Ingrese color: ')
                precio = int(input('Ingrese precio: '))
                marca = input('Ingrese marca: ')
                patente = input('Ingrese patente: ')
                año = int(input('Ingrese año de fabrica: '))
                kilometraje = int(input('Ingrese kilometraje: '))
                unAutoUsado = AutoUsado(modelo.capitalize(), puertas, color.capitalize(), precio, marca.capitalize(), patente, año, kilometraje)
                a.agregarElemento(unAutoUsado)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.')
                print()
                bande = True
            else:
                print('ERROR, opción incorrecta.')

        os.system("pause")

    def opcion3(self, a):
        os.system("cls")
        pos = int(input('Ingrese posición de la lista para ver el tipo de objeto: '))
        auto = a.mostrarElemento(pos - 1)
        print('El objeto de la posición %s es de tipo %s.' % (pos, auto))
        os.system("pause")

    def opcion4(self, a):
        os.system("cls")
        print()
        os.system("pause")

    def opcion5(self, a):
        os.system("cls")
        print()
        os.system("pause")

    def opcion6(self, a):
        os.system("cls")
        a.mostrar()
        os.system("pause")

    def opcion7(self, a):
        os.system("cls")
        print()
        os.system("pause")