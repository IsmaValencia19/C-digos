from ClaseRepositor import RepositorioProvincias
from vista import VistaProvincia
from ClaseControlador import ControladorProvincias
from ObjectEncoder import ObjectEncoder
 
def run():
    obj = ObjectEncoder('datos.json')
    repo = RepositorioProvincias(obj)
    vista = VistaProvincia()
    ctrl = ControladorProvincias(repo, vista)
    vista.setControlador(ctrl)
    ctrl.start()
    ctrl.salirGrabarDatos()

if __name__ == '__main__':
    run()