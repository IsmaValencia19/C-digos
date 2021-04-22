from ClaseManejadorIntegrante import ManejadorIntegrante
from ClaseManejadorProyecto import ManejadorProyecto
import os

if __name__ == '__main__':
    os.system('cls')
    mp = ManejadorProyecto()
    mp.carga()
    mi = ManejadorIntegrante()
    mi.carga()

    integrantes = mi.getLista()
    mp.asignarpuntaje(integrantes)
    print()
    mp.ordenar()