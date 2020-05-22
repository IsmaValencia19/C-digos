import numpy as np
from ClasePersona import Persona

class ManejaInscripcion:
    __arre = 0

    def __init__(self):
        self.__arre = np.array([])

    def agregaInscripcion(self, inscrip):
        self.__arre = np.append(self.__arre, inscrip)

    def __str__(self):
        s = ''
        for insc in self.__arre:
            s += str(insc)
        return s