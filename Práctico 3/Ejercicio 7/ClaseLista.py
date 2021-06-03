from ClaseDocenteInvestigador import DocenteInvestigador
from Validador import ValidaCadenaAlfabetica, ValidaCadenaAlfanumerica, ValidaEntero
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
                personal = actual.getDato()
                encontrado = personal
            else:
                actual = actual.getSiguiente()
                i += 1
        return encontrado

    def validacategoria(self, categoria):
        categorias = ['I', 'II', 'III', 'IV', 'V']
        encontrada = False
        i = 0
        while i < len(categorias) and encontrada == False:
            if categorias[i] == categoria:
                encontrada = True
            else:
                i += 1
        return encontrada 

    def ingresaCategoria(self):
        print('=== CATEGORÍAS: | I | II | III | IV | V | ===')
        bande = False
        while not bande:
            categoria = ValidaCadenaAlfabetica('Ingrese categoría(i = I | v = V): ')
            if self.validacategoria(categoria.upper()):
                bande = True
            else:
                print('ERROR: Categoría ingresada incorrecta.\n')
        return categoria.upper()

    def RegistroPersonal(self):
        print('>>>>>REGISTRANDO PERSONAL DE APOYO<<<<<')
        cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
        apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
        nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
        sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
        antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
        band = False
        while not band:
            categoria = ValidaEntero('Ingresa categoría (1...22): ')
            if categoria >= 1 and categoria <= 22:
                band = True
            else:
                print('ERROR: categoría ingresada incorrecta.\n')
        personal = PersonaldeApoyo(cuil, apellido.capitalize(), nombre.capitalize(), sueldobasico, antiguedad, categoria)
        return personal

    def RegistroDocente(self):
        print('>>>>>REGISTRANDO DOCENTE<<<<<')
        cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
        apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
        nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
        sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
        antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
        carrera = input('Ingrese carrera en la que dicta clases: ')
        cargo = input('Ingrese cargo que ocupa: ')
        catedra = input('Ingrese cátedra: ')
        docente = Docente(cuil, apellido.capitalize(), nombre.capitalize(), sueldobasico, antiguedad, carrera.capitalize(), cargo.capitalize(), catedra.capitalize())
        return docente

    def RegistroInvestigador(self):
        print('>>>>>REGISTRANDO INVESTIGADOR<<<<<')
        cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
        apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
        nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
        sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
        antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
        areadeinvestigacion = input('Ingrese área de investigación: ')
        tipodeinvestigacion = input('Ingrese tipo de investigación: ')
        investigador = Investigador(cuil, apellido.capitalize(), nombre.capitalize(), sueldobasico, antiguedad, areadeinvestigacion.capitalize(), tipodeinvestigacion.capitalize())
        return investigador

    def RegistroDocenteInvestigador(self):
        print('>>>>>REGISTRANDO DOCENTE INVESTIGADOR<<<<<')
        cuil = ValidaCadenaAlfanumerica('Ingrese cuil: ')
        apellido = ValidaCadenaAlfabetica('Ingrese apellido: ')
        nombre = ValidaCadenaAlfabetica('Ingrese nombre: ')
        sueldobasico = ValidaEntero('Ingrese sueldo básico: ')
        antiguedad = ValidaEntero('Ingrese años de antiguedad: ')
        carrera = input('Ingrese carrera en la que dicta clases: ')
        cargo = input('Ingrese cargo que ocupa: ')
        catedra = input('Ingrese cátedra: ')
        areadeinvestigacion = input('Ingrese área de investigación: ')
        tipodeinvestigacion = input('Ingrese tipo de investigación: ')
        categoria = self.ingresaCategoria()
        importeextra = ValidaEntero('Ingrese importe extra por docencia e investigación: ')
        docenteinvestigador = DocenteInvestigador(cuil, apellido.capitalize(), nombre.capitalize(), sueldobasico, antiguedad, carrera.capitalize(), cargo.capitalize(), catedra.capitalize(), areadeinvestigacion.capitalize(), tipodeinvestigacion.capitalize(), categoria, importeextra)
        return docenteinvestigador

    def validacarrera(self, carrera):
        actual = self.__comienzo
        band = False
        while actual != None and band == False:
            personal = actual.getDato()
            if isinstance(personal, Docente) or isinstance(personal, DocenteInvestigador):                
                if carrera == personal.getCarrera():
                    band = True
                else:
                    actual = actual.getSiguiente()
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
                print('ERROR: Nombre de carrera ingresado incorrecto.\n')
        
        listadocenteinvestiga = [] #creo una lista para ordenar los objetos de la clase docente investigador
        actual = self.__comienzo
        while actual != None:
            personal = actual.getDato()
            if isinstance(personal, DocenteInvestigador):
                if personal.getCarrera() == carrera:
                    listadocenteinvestiga.append(personal) #agrego los docentes investigadores
            actual = actual.getSiguiente()
        print()
        sorted(listadocenteinvestiga)
        for doc in listadocenteinvestiga: 
            doc.mostrar()
            print()

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
            if self.validaarea(areadeinvestigacion):
                band = True
            else:
                print('ERROR: Área de investigación ingresada incorrecta.\n')

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
        # Ordena intercambiando la posición de cada nodo
        ##########################################################
        '''fin = None
        while fin != self.__comienzo:
            r = p = self.__comienzo
            while p.getSiguiente() != fin:
                q = p.getSiguiente()
                primero = p.getDato()
                segundo = q.getDato()
                if primero.getApellido() > segundo.getApellido():
                    p.setSiguiente(q.getSiguiente())
                    q.setSiguiente(p)
                    if p != self.__comienzo:
                        r.setSiguiente(q)
                    else:
                        self.__comienzo = q
                    p, q = q, p
                r = p
                p = p.getSiguiente()
            fin = p'''
        ##########################################################

        # Ordena intercambiando los datos de cada nodo
        #####################################################################
        fin = None
        while fin != self.__comienzo:
            p = self.__comienzo
            while p.getSiguiente() != fin:
                q = p.getSiguiente()
                primero = p.getDato()
                segundo = q.getDato()
                if primero.getApellido() > segundo.getApellido():
                    primero, segundo = segundo, primero
                    p.setDato(primero)
                    q.setDato(segundo)
                p = p.getSiguiente()
            fin = p
        #####################################################################

        cad = ''
        print(cad.center(69, '='))
        print(' {0:<15} {1:<15} {2:^20} {3:^20}'.format('APELLIDO', 'NOMBRE', 'TIPO DE AGENTE', 'SUELDO'))
        print(cad.center(69, '='))
        actual = self.__comienzo
        while actual != None:
            per = actual.getDato()
            sueldo = '$%s' % (per.getSueldo())
            print(' {0:<15} {1:<15} {2:^20} {3:^20}'.format(per.getApellido(), per.getNombre(), per.getType(), sueldo))
            actual = actual.getSiguiente()
        print(cad.center(69, '='))

    def item7(self):
        categoria = self.ingresaCategoria()
        print()
        BanderaDocenteInvestigador = False  # variable utilizada para saber si aunque sea en la lista hay un docente investigador
        acum_importe = 0
        actual = self.__comienzo
        while actual != None:
            personal = actual.getDato()
            if isinstance(personal, DocenteInvestigador):
                if categoria == personal.getCategoria():
                    BanderaDocenteInvestigador = True
                    print('Apellido: %s | Nombre: %s | Importe extra por Docencia e Investigación: $%s' % (personal.getApellido(), personal.getNombre(), personal.getImporteextra())) 
                    acum_importe += personal.getImporteextra()
            actual = actual.getSiguiente()
        if BanderaDocenteInvestigador == True:
            print('\nImporte total a pagar por el extra de Docencia e Investigación es: $%s.' % (acum_importe))
        else:
            print('En la categoría ingresada no hay ningún Docente Investigador.')

    def toJSON(self):
        listapersonal = []
        for a in self:
            listapersonal.append(a.toJSON())

        d = dict(__class__ = self.__class__.__name__, personal = listapersonal)
        return d

    def mostrar(self):
        actual = self.__comienzo
        while actual != None:
            personal = actual.getDato()
            personal.mostrar()
            print()
            actual = actual.getSiguiente()

    def __len__(self):
        return self.__tope