from vista_listapacientes import NuevoPaciente, VistaPaciente, IMC
from ClaseManejadorPacientes import ManejadorPacientes
 
class ControladorPacientes:
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())

    def crearPaciente(self):
        nuevoPaciente = NuevoPaciente(self.vista).show()
        if nuevoPaciente:
            paciente = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)

    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)

    def modificarPaciente(self):
        if self.seleccion == -1:
            return
        rowid = self.pacientes[self.seleccion].rowid
        detallesPaciente = self.vista.obtenerDetalles()
        detallesPaciente.rowid = rowid
        paciente = self.repo.modificarPaciente(detallesPaciente)
        self.pacientes[self.seleccion] = paciente
        self.vista.modificarPaciente(paciente, self.seleccion)
        self.seleccion = -1

    def borrarPaciente(self):
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion = -1
#show
    def ver_imc(self):
        imc_pac = IMC(self.vista)
        if self.seleccion == -1:
            return
        paciente = self.pacientes[self.seleccion]
        imc_pac.resolver_imc(paciente)
        imc_pac.show()
        self.seleccion = -1

    def start(self):
        for p in self.pacientes:
            self.vista.agregarPaciente(p)
        self.vista.mainloop()
    
    def salirGrabarDatos(self):
        self.repo.grabarDatos()