import numpy as np

class ManejaInscripcion:
    __arre = 0

    def __init__(self):
        self.__arre = np.array([])

    def agregaInscripcion(self, inscrip):
        self.__arre = np.append(self.__arre, inscrip)

    def buscapersona(self, dni, mt):
        i = 0
        while i < len(self.__arre):
            persona = self.__arre[i].getPersona()
            if persona.getDni() == dni:
                taller = self.__arre[i].getTaller()
                print('Esta inscripto/a en el taller de: %s.' % (taller))
                p = self.__arre[i].getPago()
                if p == False:
                    debe = mt.getPago(taller)
                    print('Debe pagar: $%s.' % (debe))
                else:
                    print('No adeuda dinero de inscripción.')
                i = len(self.__arre)
            else:
                i += 1

    def consultaInscriptos(self, mt):
        print(mt)
        band = False
        while not band:
            id = int(input('Ingrese ID de taller para listar inscriptos: '))
            if mt.validataller(id) == True:
                band = True
            else:
                print('ID incorrecto.')
                id = int(input('Ingrese ID de taller para listar inscriptos: '))
        
        print()
        taller = mt.getTaller(id)
        i = 0
        while i < len(self.__arre):
            if taller == self.__arre[i].getTaller():
                persona = self.__arre[i].getPersona()
                print(persona)
            i +=1

    def buscaparapagar(self, dni, mt):
        i = 0
        while i < len(self.__arre):
            persona = self.__arre[i].getPersona()
            if dni == persona.getDni():
                taller = self.__arre[i].getTaller()
                p = self.__arre[i].getPago()
                if p == False:
                    debe = mt.getPago(taller)
                    print('Debe pagar: $%s.' % (debe))

                    band = False
                    while not band:
                        pag = int(input('Ingrese su pago: '))
                        if pag == debe:
                            self.__arre[i].modificapago()
                            print()
                            print('Pago realizado con exito!')
                            band = True
                        else:
                            print('Pago incorrecto.')
                            pag = int(input('Ingrese su pago: '))
                else:
                    print('No adeuda dinero.')
                i = len(self.__arre)
            else:
                i += 1

    def guardarArchivo(self):
                 

    def __str__(self):
        s = ''
        for insc in self.__arre:
            s += str(insc)
        return s