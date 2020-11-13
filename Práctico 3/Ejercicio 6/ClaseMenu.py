from ObjectEncoder import ObjectEncoder
from Validador import ValidaEntero, ValidaCadena, ValidaCadenaAlfabetica
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

    def opcion(self, op, autos, obj):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(autos, obj)

    def salir(self, a, obj):
        os.system("cls")
        cad = ' SALIÓ DEL PROGRAMA '
        print(cad.center(50, '='))
        print()

    def opcion1(self, a, obj):
        os.system("cls")
        bande = False
        while not bande:
            band = False
            print('== INSERTA VEHÍCULO A LA COLECCIÓN EN UNA POSICIÓN DETERMINADA ==')
            op = ValidaEntero('Ingrese |1| si el estado del vehículo es Nuevo, si es usado |2|: ')
            if op == 1:
                print('\n>>>>>>>>>>REGISTRANDO VEHÍCULO NUEVO<<<<<<<<<<')
                modelo = ValidaCadena('Ingrese el modelo(ej. Palio, Punto, etc): ')
                puertas = ValidaEntero('Ingrese la cantidad de puertas: ')
                color = ValidaCadenaAlfabetica('Ingrese color: ')
                precio = ValidaEntero('Ingrese precio: ')
                while not band:
                    version = ValidaCadenaAlfabetica('Ingrese versión(Full o Base): ')
                    if (version.capitalize() == 'Full') or (version.capitalize() == 'Base'):
                        band = True
                    else:
                        print('ERROR, versión incorrecta.')
                posicion = ValidaEntero('Ingrese posición en la que desea insertar el vehículo: ')
                unAutoNuevo = AutoNuevo(modelo.capitalize(), puertas, color.capitalize(), precio, version.capitalize())
                a.insertarElemento(unAutoNuevo, posicion - 1)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.\n')
                bande = True
            elif op == 2:
                print('\n>>>>>>>>>>REGISTRANDO VEHÍCULO USADO<<<<<<<<<<')
                modelo = ValidaCadena('Ingrese el modelo(ej. Palio, Focus, etc): ')
                puertas = ValidaEntero('Ingrese la cantidad de puertas: ')
                color = ValidaCadenaAlfabetica('Ingrese color: ')
                precio = ValidaEntero('Ingrese precio: ')
                marca = ValidaCadena('Ingrese marca: ')
                patente = ValidaCadena('Ingrese patente: ')
                año = ValidaEntero('Ingrese año de fabrica: ')
                kilometraje = ValidaEntero('Ingrese kilometraje: ')
                posicion = ValidaEntero('Ingrese posición en la que desea insertar el vehículo: ')
                unAutoUsado = AutoUsado(modelo.capitalize(), puertas, color.capitalize(), precio, marca.capitalize(), patente, año, kilometraje)
                a.insertarElemento(unAutoUsado, posicion - 1)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.\n')
                bande = True
            else:
                print('ERROR, opción incorrecta.')

        os.system("pause")
    
    def opcion2(self, a, obj):
        os.system("cls")
        bande = False
        while not bande:
            band = False
            print('================== AGREGAR VEHÍCULO A LA COLECCIÓN ==================')
            op = ValidaEntero('Ingrese |1| si el estado del vehículo es Nuevo, si es usado |2|: ')
            if op == 1:
                print('\n>>>>>>>>REGISTRANDO VEHÍCULO NUEVO<<<<<<<<')
                modelo = ValidaCadena('Ingrese el modelo(ej. Palio, Punto, etc): ')
                puertas = ValidaEntero('Ingrese la cantidad de puertas: ')
                color = ValidaCadenaAlfabetica('Ingrese color: ')
                precio = ValidaEntero('Ingrese precio: ')
                while not band:
                    version = ValidaCadenaAlfabetica('Ingrese versión(Full o Base): ')
                    if (version.capitalize() == 'Full') or (version.capitalize() == 'Base'):
                        band = True
                    else:
                        print('ERROR, versión incorrecta.')
                unAutoNuevo = AutoNuevo(modelo.capitalize(), puertas, color.capitalize(), precio, version.capitalize())
                a.agregarElemento(unAutoNuevo)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.\n')
                bande = True
            elif op == 2:
                print('\n>>>>>>>>REGISTRANDO VEHÍCULO USADO<<<<<<<<')
                modelo = ValidaCadena('Ingrese el modelo(ej. Palio, Focus, etc): ')
                puertas = ValidaEntero('Ingrese la cantidad de puertas: ')
                color = ValidaCadenaAlfabetica('Ingrese color: ')
                precio = ValidaEntero('Ingrese precio: ')
                marca = ValidaCadena('Ingrese marca: ')
                patente = ValidaCadena('Ingrese patente: ')
                año = ValidaEntero('Ingrese año de fabrica: ')
                kilometraje = ValidaEntero('Ingrese kilometraje: ')
                unAutoUsado = AutoUsado(modelo.capitalize(), puertas, color.capitalize(), precio, marca.capitalize(), patente, año, kilometraje)
                a.agregarElemento(unAutoUsado)
                print('\nVEHÍCULO REGISTRADO CON ÉXITO.\n')
                bande = True
            else:
                print('ERROR, opción incorrecta.')

        os.system("pause")

    def opcion3(self, a, obj):
        os.system("cls")
        pos = ValidaEntero('Ingrese posición de la lista para ver el tipo de objeto: ')
        auto = a.mostrarElemento(pos - 1)
        print('\nEl objeto de la posición %s es de tipo %s.\n' % (pos, auto))
        os.system("pause")

    def opcion4(self, a, obj):
        os.system("cls")
        a.item4()
        os.system("pause")

    def opcion5(self, a, obj):
        os.system("cls")
        a.item5()
        os.system("pause")

    def opcion6(self, a, obj):
        os.system("cls")
        a.mostrar()
        os.system("pause")

    def opcion7(self, a, obj):
        os.system("cls")
        autos = a.toJSON()
        obj.Guardar(autos)
        print('Archivo guardado con éxito.')
        print()
        os.system("pause")