from claseAlumno import claseAlumno
import csv

class manejadorAlumno:
    __listaAlumno = []

    def __init__(self):
        self.__listaAlumno = []
    
    def agregarAlumno(self, alumno):
        self.__listaAlumno.append(alumno)
    
    def __str__(self):
        s = ''
        for alumno in self.__listaAlumno:
            s += str(alumno) + '\n'
        return s

    def testAlumnos(self):
        archivo = open('alumnos.csv')
        reader = csv.reader(archivo, delimiter = ',')
        for fila in reader:
            nom = fila[0]
            año = fila[1]
            div = fila[2]
            cant_inas = fila[3]
            unAlumno = claseAlumno(nom, año, div, cant_inas)
            self.agregarAlumno(unAlumno)
        archivo.close()

    def porcentAlum(self, añ, di):
        for i in self.__listaAlumno:
            año = i.getAño()
            div = i.getDiv()
            inasis = i.getInasis()
            if(año == añ) and (div == di) and (inasis > claseAlumno.getMaxInas()):
                print('{:<25}{}%'.format(i.getNom(), i.porcen_inasis()))