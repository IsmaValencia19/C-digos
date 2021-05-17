from ClaseAutoNuevo import AutoNuevo
from ClaseLista import Lista
import unittest
import os

class Testing(unittest.TestCase):
    __manejador = None

    def setUp(self):
        self.__manejador = Lista()
        primerauto = AutoNuevo('Punto', 5, 'Negro', 1300000, 'FULL')
        segundoauto = AutoNuevo('Toro', 3, 'Blanca', 2000000, 'FULL')
        tercerauto = AutoNuevo('Palio', 5, 'Celeste', 1)

def ActivaTesting():
    os.system('cls')
    unittest.main()