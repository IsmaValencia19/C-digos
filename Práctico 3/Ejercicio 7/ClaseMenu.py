from Validador import ValidaEntero, ValidaCadenaAlfabetica, ValidaCadenaAlfanumerica
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

    def opcion(self, op, personal, obj):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(personal, obj)

    def salir(self, p, obj):
        os.system("cls")
        cad = ' SALIÓ DEL PROGRAMA '
        print(cad.center(50, '='))
        print()

    def opcion1(self, p, obj):
        os.system("cls")
        band = False
        while not band:
            print('=== INSERTAR AGENTES EN LA COLECCIÓN ===')
            print('1 - Personal de Apoyo.')
            print('2 - Docente.')
            print('3 - Investigador.')
            print('4 - Docente Investigador.')
            op = ValidaEntero('Ingrese tipo de agente para insertar en la colección: ')
            if op == 1:
                os.system('cls')
                unPersonaldeApoyo = p.RegistroPersonal()
                posicion = ValidaEntero('\nIngrese posición para insertar en la lista: ')
                p.insertarElemento(unPersonaldeApoyo, posicion - 1)
                print('\nPERSONAL DE APOYO INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 2:
                os.system('cls')
                unDocente = p.RegistroDocente()
                posicion = ValidaEntero('\nIngrese posición para insertar en la lista: ')
                p.insertarElemento(unDocente, posicion - 1)
                print('\nDOCENTE INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 3:
                os.system('cls')
                unInvestigador = p.RegistroInvestigador()
                posicion = ValidaEntero('\nIngrese posición para insertar en la lista: ')
                p.insertarElemento(unInvestigador, posicion - 1)
                print('\nINVESTIGADOR INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 4:
                os.system('cls')
                unDocenteInvestigador = p.RegistroDocenteInvestigador()
                posicion = ValidaEntero('\nIngrese posición para insertar en la lista: ')
                p.insertarElemento(unDocenteInvestigador, posicion - 1)
                print('\nDOCENTE INVESTIGADOR INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            else:
                print('ERROR: Opción ingresada incorrecta.')
        os.system("pause")
    
    def opcion2(self, p, obj):
        os.system("cls")
        band = False
        while not band:
            print('=== AGREGAR AGENTES A LA COLECCIÓN ===')
            print('1 - Personal de Apoyo.')
            print('2 - Docente.')
            print('3 - Investigador.')
            print('4 - Docente Investigador.')
            op = int(input('Ingrese tipo de agente para agregar: '))
            if op == 1:
                os.system('cls')
                unPersonaldeApoyo = p.RegistroPersonal()
                p.agregarElemento(unPersonaldeApoyo)
                print('\nPERSONAL DE APOYO AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 2:
                os.system('cls')
                unDocente = p.RegistroDocente()
                p.agregarElemento(unDocente)
                print('\nDOCENTE AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 3:
                os.system('cls')
                unInvestigador = p.RegistroInvestigador()
                p.agregarElemento(unInvestigador)
                print('\nINVESTIGADOR AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 4:
                os.system('cls')
                unDocenteInvestigador = p.RegistroDocenteInvestigador()
                p.agregarElemento(unDocenteInvestigador)
                print('\nDOCENTE INVESTIGADOR AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            else:
                print('ERROR: Opción ingresada incorrecta.')
        os.system("pause")

    def opcion3(self, p, obj):
        os.system("cls")
        pos = ValidaEntero('Ingrese posición de la lista para ver el tipo de objeto: ')
        personal = p.mostrarElemento(pos - 1)
        print('\nEl objeto de la posición %s es de tipo %s.\n' % (pos, personal.getType()))
        os.system("pause")

    def opcion4(self, p, obj):
        os.system("cls")
        p.item4()
        os.system("pause")

    def opcion5(self, p, obj):
        os.system("cls")
        p.item5()
        os.system("pause")

    def opcion6(self, p, obj):
        os.system("cls")
        p.item6()
        print()
        os.system("pause")

    def opcion7(self, p, obj):
        os.system("cls")
        p.item7()
        print()
        os.system("pause")

    def opcion8(self, p, obj):
        os.system("cls")
        personal = p.toJSON()
        obj.Guardar(personal)
        print('Archivo guardado con éxito.')
        print()
        os.system("pause")