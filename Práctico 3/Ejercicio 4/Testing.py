from ClaseEmpleadoPlanta import Planta
import unittest
import os

class Testing(unittest.TestCase):
    __personal = None
    
    def setUp(self):
        self.__personal = Planta(42163931, 'Leonel', 'Av. Rawson 100 (S)', 2646023168, 19999, 2)
    
    def test_sueldo(self):
        self.assertEqual(self.__personal.getSueldoBasico(), 19999)

    def test_antiguedad(self):
        self.assertEqual(self.__personal.getAntig(), 2)

def ActivaTesting():
    os.system('cls')
    unittest.main()