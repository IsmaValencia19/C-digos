from Validador import ValidaEntero
import numpy as np
import csv

class ManejaInscripcion:
    __arre = None

    def __init__(self):
        self.__arre = np.array([])

    def agregaInscripcion(self, inscrip):
        self.__arre = np.append(self.__arre, inscrip)

    #verifica si una persona debe dinero o no
    def verificaDeuda(self, persona):
        i = 0
        while i < len(self.__arre):
            if persona == self.__arre[i].getPersona():
                taller = self.__arre[i].getTaller()
                print('Esta inscripto/a en el taller de: %s.' % (taller.getNom()))
                if self.__arre[i].getPago() == False:
                    debe = taller.getMonto()
                    print('Debe pagar: $%s.' % (debe))
                else:
                    print('No adeuda dinero de inscripción.')
                i = len(self.__arre)
            else:
                i += 1

    #muestra los inscriptos en un taller ingresado por teclado
    def mostrarInscriptos(self, taller):
        print()
        i = 0
        while i < len(self.__arre):
            if taller == self.__arre[i].getTaller():
                persona = self.__arre[i].getPersona()
                print(persona)
            i +=1
        if taller.getVacantes() == 50:
            print('El taller de %s por el momento no registra personas inscriptas.' % (taller.getNom()))

    #ingresa dni de algún inscripto para pagar si adeuda
    def buscaparapagar(self, persona):
        i = 0
        while i < len(self.__arre):
            if persona == self.__arre[i].getPersona():
                taller = self.__arre[i].getTaller()
                if self.__arre[i].getPago() == False:
                    print('\nDebe pagar: $%s.\n' % (taller.getMonto()))
                    band = False
                    while not band:
                        pago = ValidaEntero('Ingrese su pago: ')
                        if pago == taller.getMonto():
                            self.__arre[i].modificapago()
                            print('\nPago realizado con exito!\n')
                            band = True
                        else:
                            print('Pago incorrecto.\n')
                else:
                    print('No adeuda dinero.')
                i = len(self.__arre)
            else:
                i += 1

    def guardarArchivo(self, mp, mt):
        archivo = open('inscriptos.csv', 'w')
        i = 0
        while i < len(self.__arre):
            persona = self.__arre[i].getPersona()
            dni = str(persona.getDni())
            taller = self.__arre[i].getTaller()

            ID = str(mt.getId(taller))
            fecha = self.__arre[i].getFecha()
            pago = self.__arre[i].getPago()

            archivo.write(dni)
            archivo.write(',')
            archivo.write(ID)
            archivo.write(',')
            archivo.write(str(fecha))
            archivo.write(',')
            if pago == True:
                archivo.write('Si\n')
            else:
                archivo.write('No\n')
            i += 1

        print('Archivo guardado con exito.')
        archivo.close()

    def __str__(self):
        s = ''
        for insc in self.__arre:
            s += str(insc)
        return s