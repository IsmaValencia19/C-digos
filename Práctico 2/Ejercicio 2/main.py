from manejadorViajeros import clasemanejadorViajero
from ClaseViajeroFrecuente import ViajeroFrecuente
from Validador import ValidaEntero
import csv
import os
 
if __name__ == '__main__':
    os.system("cls")
    mv = clasemanejadorViajero()
    mv.testViajeros()
    print('>>>>>>>>>>>>>LISTA DE VIAJEROS<<<<<<<<<<<<<\n')
    print(mv)
    band = False
    while not band:
        idViaj = ValidaEntero('Ingrese número de viajero frecuente: ')
        indice = mv.buscarViajero(idViaj)
        if indice == None:
            print('El número de viajero {} no corresponde a un viajero.'.format(idViaj))
        else:
            band = True
            viajero = mv.getId(indice)    
            bandera = False 
            while not bandera:
                os.system('cls')
                print('Has introducido el ID {}.'.format(idViaj))
                print("0 - Salir")
                print("1 - Consultar cantidad de millas.")
                print("2 - Acumular millas.")
                print("3 - Canjear millas.")
                opcion = ValidaEntero('Ingrese una opción: ')
                if opcion == 1:
                    print('\n{} es el ID de {}, que tiene {} millas acumuladas.'.format(idViaj, viajero.getNom(), viajero.cantTotalMillas()))
                    os.system('pause')
                elif opcion == 2:
                    millas = ValidaEntero('Ingrese millas para acumular: ')
                    viajero.acumMillas(millas)
                    print('Se actualizaron las millas: ', viajero.cantTotalMillas())
                    os.system('pause')
                elif opcion == 3:
                    print('\nCon quien desea canjear millas:')
                    print(mv)
                    idcanjear = ValidaEntero('Ingrese ID de una persona para canjear millas: ')
                    indiceCanjear = mv.buscarViajero(idcanjear)
                    if indiceCanjear == None:
                        print('La persona con el ID: {} no existe.'.format(idcanjear))
                    else:
                        viajerocanjear = mv.getId(indiceCanjear)
                        millascanje = ValidaEntero('\nIngrese millas para canje: ')
                        if millascanje <= viajerocanjear.cantTotalMillas():
                            viajerocanjear.canjearMillas(millascanje)
                            viajero.acumMillas(millascanje)
                        else:
                            print('\nNo tiene millas suficientes.')
                    os.system('pause')
                bandera = opcion == 0