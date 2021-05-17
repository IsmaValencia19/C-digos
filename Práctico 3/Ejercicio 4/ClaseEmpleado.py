import abc

class Empleado:
    __dni = 0
    __nom = ''
    __dir = ''
    __tel = 0
 
    def __init__(self, dni, nom, dir, tel):
        self.__dni = dni
        self.__nom = nom
        self.__dir = dir
        self.__tel = tel

    def getDni(self):
        return self.__dni

    def getNom(self):
        return self.__nom

    def getDir(self):
        return self.__dir

    def getTel(self):
        return self.__tel

    @abc.abstractmethod
    def getTarea(self):
        pass

    def __lt__(self, sueld):
        return self.getSueldo() < sueld

    def mostrar(self):
        print('DNI: %d - NOMBRE Y APELLIDO: %s - DIRECCIÓN: %s - CELULAR: %d' % (self.__dni, self.__nom, self.__dir, self.__tel))