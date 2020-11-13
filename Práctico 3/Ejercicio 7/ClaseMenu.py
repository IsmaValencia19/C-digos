from ClaseDocenteInvestigador import DocenteInvestigador
from Validador import ValidaEntero, ValidaCadenaAlfabetica, ValidaCadenaAlfanumerica
from ClasePersonaldeApoyo import PersonaldeApoyo
from ClaseInvestigador import Investigador
from ClaseDocente import Docente
from ObjectEncoder import ObjectEncoder
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
                            7:self.opcion7,
                            8:self.opcion8,
                            9:self.opcion9
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
            print('1 - Personal de Apoyo')
            print('2 - Docente')
            print('3 - Investigador')
            print('4 - Docente Investigador.')
            op = ValidaEntero('Ingrese tipo de agente para insertar en la colección: ')
            if op == 1:
                print('>>>>>REGISTRANDO PERSONAL DE APOYO<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                bande = False
                while not bande:
                    print('=== CATEGORÍAS: I | II | III | IV | V ===')
                    categoria = ValidaCadenaAlfabetica('Ingrese categoría(i = I | v = V): ')
                    categoria.upper()
                    encontrada = p.validacategoria(categoria)
                    if encontrada != None:
                        categoria = encontrada
                        bande = True
                    else:
                        print('ERROR, categoría incorrecta.')
                posicion = ValidaEntero('Ingrese posición para insertar en la lista: ')
                unPersonaldeApoyo = PersonaldeApoyo(cuil, apellido, nombre, sueldobasico, antiguedad, categoria)
                p.insertarElemento(unPersonaldeApoyo, posicion - 1)
                print('\nAGENTE INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 2:
                print('>>>>>REGISTRANDO DOCENTE<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                carrera = input('Ingrese carrera en la que dicta clases: ').capitalize()
                cargo = input('Ingrese cargo que ocupa: ').capitalize()
                catedra = input('Ingrese cátedra: ').capitalize()
                posicion = ValidaEntero('Ingrese posición para insertar en la lista: ')
                unDocente = Docente(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra)
                p.insertarElemento(unDocente, posicion - 1)
                print('\nAGENTE INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 3:
                print('>>>>>REGISTRANDO INVESTIGADOR<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                areadeinvestigacion = input('Ingrese área de investigación: ').capitalize()
                tipodeinvestigacion = input('Ingrese tipo de investigación: ').capitalize()
                posicion = ValidaEntero('Ingrese posición para insertar en la lista: ')
                unInvestigador = Investigador(cuil, apellido, nombre, sueldobasico, antiguedad, areadeinvestigacion, tipodeinvestigacion)
                p.insertarElemento(unInvestigador, posicion - 1)
                print('\nAGENTE INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 4:
                print('>>>>>REGISTRANDO DOCENTE INVESTIGADOR<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                carrera = input('Ingrese carrera en la que dicta clases: ').capitalize()
                cargo = input('Ingrese cargo que ocupa: ').capitalize()
                catedra = input('Ingrese cátedra: ').capitalize()
                areadeinvestigacion = input('Ingrese área de investigación: ').capitalize()
                tipodeinvestigacion = input('Ingrese tipo de investigación: ').capitalize()
                bande = False
                while not bande:
                    print('=== CATEGORÍAS: I | II | III | IV | V ===')
                    categoria = ValidaCadenaAlfabetica('Ingrese categoría(i = I | v = V): ')
                    categoria.upper()
                    encontrada = p.validacategoria(categoria)
                    if encontrada != None:
                        categoria = encontrada
                        bande = True
                    else:
                        print('ERROR, categoría incorrecta.')
                importeextra = ValidaEntero('Ingrese importe extra por docencia e investigación: ')
                posicion = ValidaEntero('Ingrese posición para insertar en la lista: ')
                unDocenteInvestigador = DocenteInvestigador(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, areadeinvestigacion, tipodeinvestigacion, categoria, importeextra)
                p.insertarElemento(unDocenteInvestigador, posicion - 1)
                print('\nAGENTE INSERTADO EN LA COLECCIÓN CON ÉXITO.\n')
                band = True
            else:
                print('ERROR, opción de agente incorrecta.')
        os.system("pause")
    
    def opcion2(self, p, obj):
        os.system("cls")
        band = False
        while not band:
            print('=== AGREGAR AGENTES A LA COLECCIÓN ===')
            print('1 - Personal de Apoyo')
            print('2 - Docente')
            print('3 - Investigador')
            print('4 - Docente Investigador.')
            op = int(input('Ingrese tipo de agente para agregar: '))
            if op == 1:
                print('>>>>>REGISTRANDO PERSONAL DE APOYO<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                bande = False
                while not bande:
                    print('=== CATEGORÍAS: I | II | III | IV | V ===')
                    categoria = ValidaCadenaAlfabetica('Ingrese categoría(i = I | v = V): ')
                    categoria.upper()
                    encontrada = p.validacategoria(categoria)
                    if encontrada != None:
                        categoria = encontrada
                        bande = True
                    else:
                        print('ERROR, categoría incorrecta.')
                unPersonaldeApoyo = PersonaldeApoyo(cuil, apellido, nombre, sueldobasico, antiguedad, categoria)
                p.agregarElemento(unPersonaldeApoyo)
                print('\nAGENTE AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 2:
                print('>>>>>REGISTRANDO DOCENTE<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                carrera = input('Ingrese carrera en la que dicta clases: ').capitalize()
                cargo = input('Ingrese cargo que ocupa: ').capitalize()
                catedra = input('Ingrese cátedra: ').capitalize()
                unDocente = Docente(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra)
                p.agregarElemento(unDocente)
                print('\nAGENTE AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 3:
                print('>>>>>REGISTRANDO INVESTIGADOR<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                areadeinvestigacion = input('Ingrese área de investigación: ').capitalize()
                tipodeinvestigacion = input('Ingrese tipo de investigación: ').capitalize()
                unInvestigador = Investigador(cuil, apellido, nombre, sueldobasico, antiguedad, areadeinvestigacion, tipodeinvestigacion)
                p.agregarElemento(unInvestigador)
                print('\nAGENTE AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            elif op == 4:
                print('>>>>>REGISTRANDO DOCENTE INVESTIGADOR<<<<<')
                cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
                apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
                apellido.capitalize()
                nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
                nombre.capitalize()
                sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
                antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
                carrera = input('Ingrese carrera en la que dicta clases: ').capitalize()
                cargo = input('Ingrese cargo que ocupa: ').capitalize()
                catedra = input('Ingrese cátedra: ').capitalize()
                areadeinvestigacion = input('Ingrese área de investigación: ').capitalize()
                tipodeinvestigacion = input('Ingrese tipo de investigación: ').capitalize()
                bande = False
                while not bande:
                    print('=== CATEGORÍAS: I | II | III | IV | V ===')
                    categoria = ValidaCadenaAlfabetica('Ingrese categoría(i = I | v = V): ')
                    categoria.upper()
                    encontrada = p.validacategoria(categoria)
                    if encontrada != None:
                        categoria = encontrada
                        bande = True
                    else:
                        print('ERROR, categoría incorrecta.')
                importeextra = ValidaEntero('Ingrese importe extra por docencia e investigación: ')
                unDocenteInvestigador = DocenteInvestigador(cuil, apellido, nombre, sueldobasico, antiguedad, carrera, cargo, catedra, areadeinvestigacion, tipodeinvestigacion, categoria, importeextra)
                p.agregarElemento(unDocenteInvestigador)
                print('\nAGENTE AGREGADO A LA COLECCIÓN CON ÉXITO.\n')
                band = True
            else:
                print('ERROR, opción de agente incorrecta.')
        os.system("pause")

    def opcion3(self, p, obj):
        os.system("cls")
        pos = ValidaEntero('Ingrese posición de la lista para ver el tipo de objeto: ')
        personal = p.mostrarElemento(pos - 1)
        tipo = ''
        if isinstance(personal, Docente):
            tipo = 'Docente'
        elif isinstance(personal, PersonaldeApoyo):
            tipo = 'Personal de Apoyo'
        elif isinstance(personal, Investigador):
            tipo = 'Investigador'
        elif isinstance(personal, DocenteInvestigador):
            tipo = 'Docente Investigador'
        print('\nEl objeto de la posición %s es de tipo %s.\n' % (pos, tipo))
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
        os.system("pause")

    def opcion7(self, p, obj):
        os.system("cls")
        p.item7()
        os.system("pause")

    def opcion8(self, p, obj):
        os.system("cls")
        personal = p.toJSON()
        obj.Guardar(personal)
        print('Archivo guardado con éxito.')
        print()
        os.system("pause")

    def opcion9(self, p, obj):
        os.system("cls")
        p.mostrar()
        os.system("pause")