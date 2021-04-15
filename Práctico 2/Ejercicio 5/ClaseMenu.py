from Validador import ValidaEntero
import os

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2
                          }
    
    def getSwitcher(self):
        return self.__switcher
    
    def opcion(self, op, ma):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(ma)
    
    def salir(self, ma):
        os.system('cls')
        print()
        print('>>>>>Salio del programa<<<<<')
        print()
   
    def opcion1(self, ma):
        os.system("cls")

        año = ValidaEntero('Ingrese año: ')
        div = ValidaEntero('Ingrese división: ')
        print()
        alumnos = ma.porcentAlum(año, div)
        if alumnos != []:
            print('{:25}{}'.format('Alumno', 'Porcentaje'))
            i = 0
            while i < len(alumnos):
                print('{:<25}{}%'.format(alumnos[i].getNom(), alumnos[i].porcen_inasis()))
                i += 1
        else:
            print('En este año y división todavia no queda ningún alumno libre.')

        print()
        os.system("pause")
    
    def opcion2(self, ma):
        os.system("cls")

        max_inasis = ValidaEntero('Ingrese la nueva cantidad máxima de inasistencias : ')
        print()
        print('Asistencia antes de actualizar:')
        alumno = Alumno()
        alumno.verAsistencias()
        alumno.actualizarMaxInas(max_inasis)
        print()
        print('Asistencia actualizada.')
        alumno.verAsistencias()

        print()
        os.system("pause")