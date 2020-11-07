from ClaseAlumno import Alumno
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
            año = int(fila[1])
            div = int(fila[2])
            cant_inas = int(fila[3])
            unAlumno = Alumno(nom, año, div, cant_inas)
            self.agregarAlumno(unAlumno)
        archivo.close()

    def porcentAlum(self, añ, di):
        i = 0
        while i < len(self.__listaAlumno):
            año = self.__listaAlumno[i].getAño()
            div = self.__listaAlumno[i].getDiv()
            if (año == añ) and (div == di) and (self.__listaAlumno[i].getInasis() > Alumno.getMaxInas()):
                print('{:<25}{}%'.format(self.__listaAlumno[i].getNom(), self.__listaAlumno[i].porcen_inasis()))
            i += 1