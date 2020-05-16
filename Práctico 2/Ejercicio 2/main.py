from Clases import claseViajero
from manejadorViajeros import clasemanejadorViajero
import csv
import os

if __name__ == '__main__':
    os.system("cls")
    mv = clasemanejadorViajero()
    mv.testViajeros()
    print('>>>>>>>>>>>>>LISTA DE VIAJEROS<<<<<<<<<<<<<\n')
    print(mv)
    idViaj = int(input('Ingrese número de viajero frecuente: '))
    indice = mv.buscarViajero(idViaj)

    if indice == None:
        print('El numero de viajero {} no corresponde a un viajero.'.format(idViaj))
    else:
        viajero = mv.getId(indice)    
        bandera = False 
        while not bandera:
            print("")
            print("0 - Salir")
            print("1 - Consultar cantidad de millas.")
            print("2 - Acumular millas.")
            print("3 - Canjear millas.")
            opcion= int(input("Ingrese una opción: "))
            if int(opcion) == 1:
                print('\n{} es el ID de{}, que tiene {} millas acumuladas.'.format(idViaj, viajero.getNom(), viajero.cantTotalMillas()))
            elif int(opcion) == 2:
                millas = int(input('\nIngrese millas para acumular: '))
                viajero.acumMillas(millas)
                print('Se actualizaron las millas: ', viajero.cantTotalMillas())
            elif int(opcion) == 3:
                print('\nCon quien desea canjear millas:')
                print(mv)
                idcanjear = int(input('Ingrese ID de persona para canjear millas: '))
                indiceCanjear = mv.buscarViajero(idcanjear)
                if indiceCanjear == None:
                    print('La persona con el ID: {} no existe.'.format(idcanjear))
                else:
                    viajerocanjear = mv.getId(indiceCanjear)
                    millascanje = int(input('\nIngrese millas para canje: '))
                    if millascanje <= viajerocanjear.cantTotalMillas():
                        viajerocanjear.canjearMillas(millascanje)
                        viajero.acumMillas(millascanje)

                    else:
                        print('\nNo tiene millas suficientes.')   
            bandera = int(opcion)==0
        
        os.system("cls")