from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from archivodeinterface import inter
from ClasePersonal import Personal
from ClaseDocente import Docente
from ClasePersonaldeApoyo import PersonaldeApoyo
from ClaseNodo import Nodo
import zope

@zope.interface.implementer(inter)
class Lista:
    __comienzo = None
    __actual = None
    __tope = 0
    __indice = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarElemento(self, dato):
        nodo = Nodo(dato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarElemento(self, elemento, posicion):
        if posicion == 0:
            self.agregarElemento(elemento)
        else:
            aux = self.__comienzo
            i = 0
            elemento = Nodo(elemento)

            while i < posicion and aux != None:
                anterior = aux
                aux = aux.getSiguiente()
                i += 1

            if i > posicion:
                raise IndexError
            else:
                elemento.setSiguiente(aux)
                anterior.setSiguiente(elemento)
                self.__tope += 1

    def mostrarElemento(self, posicion):
        i = 0
        actual = self.__comienzo
        encontrado = None
        while actual != None and encontrado == None:
            if i == posicion:
                auto = actual.getDato()
                encontrado = auto
            else:
                actual = actual.getSiguiente()
                i += 1
        return encontrado

    def validacategoria(self, categoria):
        categorias = ['I', 'II', 'III', 'IV', 'V']
        encontrada = None
        i = 0
        while i < len(categorias) and encontrada == None:
            if categorias[i] == categoria:
                encontrada = categorias[i]
                i = len(categorias)
            else:
                i += 1
        return encontrada 

    def validacarrera(self, carrera):
        actual = self.__comienzo
        band = False
        while actual != None and band == False:
            personal = actual.getDato()
            if carrera == personal.getCarrera():
                band = True
            else:
                actual = actual.getSiguiente()
        return band

    def item4(self):
        band = False
        while not band:
            carrera = input('Ingrese nombre de carrera: ').capitalize()
            if self.validacarrera(carrera) == True:
                band = True
            else:
                print('ERROR, nombre de carrera incorrecta.')
        
        listadocenteinvestiga = [] #creo una lista para ordenar los objetos de la clase docente investigador
        actual = self.__comienzo
        while actual != None:
            personal = actual.getDato()
            if personal.getCarrera() == carrera:
                if isinstance(personal, DocenteInvestigador):
                    listadocenteinvestiga.append(personal) #agrego los docentes investigadores
            actual = actual.getSiguiente()

        print()
        sorted(listadocenteinvestiga)
        for doc in listadocenteinvestiga: 
            print(doc)

    def validaarea(self, area):
        band = False
        actual = self.__comienzo
        while actual != None and band == False:
            personal = actual.getDato()
            if isinstance(personal, Investigador) or isinstance(personal, DocenteInvestigador):
                if area == personal.getArea():
                    band = True
                else:
                    actual = actual.getSiguiente()
            else:
                actual = actual.getSiguiente()
        return band

    def item5(self):
        band = False
        while not band:
            areadeinvestigacion = input('Ingrese área de investigación: ').capitalize()
            if self.validaarea(areadeinvestigacion) == True:
                band = True
            else:
                print('ERROR, área de investigación incorrecta.')

        actual = self.__comienzo
        cont_investigador = 0
        cont_docinvestigador = 0
        while actual != None:
            personal = actual.getDato()
            if isinstance(personal, DocenteInvestigador) or isinstance(personal, Investigador):
                if areadeinvestigacion == personal.getArea():
                    if isinstance(personal, DocenteInvestigador):
                        cont_docinvestigador += 1
                    elif isinstance(personal, Investigador):
                        cont_investigador += 1
                actual = actual.getSiguiente()
            else:
                actual = actual.getSiguiente()
        
        print('\nEn el área de investigacion %s trabajan %s investigador/es y %s Docente/s Investigador/es.\n' % (areadeinvestigacion, cont_investigador, cont_docinvestigador))

    def item6(self):
        lista = []
        actual = self.__comienzo
        while actual != None:
            personal = actual.getDato()
            tipo = ''
            if type(personal) == DocenteInvestigador:
                tipo = 'Docente Investigador'
            elif isinstance(personal, PersonaldeApoyo):
                tipo = 'Personal de Apoyo'
            elif isinstance(personal, Investigador):
                tipo = 'Investigador'
            elif isinstance(personal, Docente):
                tipo = 'Docente'
            listapersonal = [personal.getNombre(), personal.getApellido(), tipo, personal.getSueldo()]
            lista.append(listapersonal)
            actual = actual.getSiguiente()

        lista.sort(key = lambda x:x[1], reverse = False)
        print('  Nombre    Apellido    Tipo de Agente     Sueldo')
        for per in lista:
            print(per)
        print()

    def item7(self):
        bande = False
        while not bande:
            print('=== CATEGORÍAS: I | II | III | IV | V ===')
            categoria = input('Ingrese categoría(i = I | v = V): ').upper()
            encontrada = self.validacategoria(categoria)
            if encontrada != None:
                categoria = encontrada
                bande = True
            else:
                print('ERROR, categoría incorrecta.')
        print()
        acum_importe = 0
        actual = self.__comienzo
        while actual != None:
            personal = actual.getDato()
            if isinstance(personal, DocenteInvestigador):
                if categoria == personal.getCategoria():
                    print('Apellido: %s | Nombre: %s | Importe extra por Docencia e Investigación: $%s' % (personal.getApellido(), personal.getNombre(), personal.getImporteextra())) 
                    acum_importe += personal.getImporteextra()
            actual = actual.getSiguiente()
        print('Importe total a pagar por el extra de Docencia e Investigación es: $%s.\n' % (acum_importe))

    def toJSON(self):
        listapersonal = []
        for a in self:
            listapersonal.append(a.toJSON())

        d = dict(__class__ = self.__class__.__name__, personal = listapersonal)
        return d

    def mostrar(self):
        for personal in self:
            print(personal.mostrar())

    def __len__(self):
        return self.__tope