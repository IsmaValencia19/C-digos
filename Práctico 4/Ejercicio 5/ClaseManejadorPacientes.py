from ClasePaciente import Paciente

class ManejadorPacientes:
    __lista = None
    indice = 0

    def __init__(self):
        self.__lista = []

    def agregarPaciente(self, paciente):
        paciente.rowid = ManejadorPacientes.indice
        ManejadorPacientes.indice += 1
        self.__lista.append(paciente)

    def getLista(self):
        return self.__lista

    def deletePaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__lista.pop(indice)
 
    def updatePaciente(self, paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__lista[indice] = paciente

    def obtenerIndicePaciente(self, paciente):
        band = False
        i = 0
        while not band and i < len(self.__lista):
            if self.__lista[i].rowid == paciente.rowid:
                band = True
            else:
                i += 1
        return i

    def toJSON(self):
        d = dict(
                __class__ = self.__class__.__name__,
                pacientes = [paciente.toJSON() for paciente in self.__lista]
        )
        return d

    def mostrar(self):
        for pac in self.__lista:
            print(pac)