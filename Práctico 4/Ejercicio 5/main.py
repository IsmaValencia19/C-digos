from ClaseRepositorioPacientes import RepositorioPacientes
from ClaseControladorPacientes import ControladorPacientes
from vista_listapacientes import VistaPaciente
from ObjectEncoder import ObjectEncoder

def run():
    conn = ObjectEncoder('pacientes.json')
    repo = RepositorioPacientes(conn)
    vista = VistaPaciente()
    ctrl = ControladorPacientes(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == '__main__':
    run()