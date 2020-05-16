from claseCAMION import claseCamion
from claseCOSECHA import claseCosecha
from manejador import cargaCamion, cargaCosecha, buscar
import csv
import os

def opcion1(cosecha):
    print()
    id = int(input('Ingrese id: '))
    print()
    parar = 0
    while parar == 1:
        if((id) == 1 and 0 < (id - 1) < 20):
            for i in range(44):
                acum += cosecha.getValor(i, (id - 1))
            print('La cantidad de kg cargados del camión', id, 'es', acum)
            parar = 0
        else:
            id = int(input('Ingrese ID: '))
            id -= 1
    print()
    os.system("pause")

def opcion2(cosecha, listacamion):
    print('')
    dia = int(input('Ingrese dia: '))
    dia = int(dia)
    dia -= 1
    print()
    salir = 1
    while salir == 1:
        if((dia) == 1 and 0 < (dia - 1) < 45):
            print('%10s' % 'PATENTE', '%13s' % 'NOMBRE', '%10s' % 'KILOS')
            for i in range(20):
                p, nom = buscar(i, listacamion)
                print('%10s' % p, '%13s' % nom, '%10s' % cosecha.getValor(i, dia - 1))
                salir = 0
        else:
            dia = int(input('Ingrese dia: '))
    print()
    os.system("pause")

def salir():
    print('>>>Salio del programa<<<')

def menu(cosecha, listacamion):
    op = 0
    while op != 3:
        os.system("cls")
        print('>>>>>MENÚ<<<<<')
        print('1 - Ingrese ID de camión para ver el total de kg.')
        print('2 - Ingrese dia para mostrar un listado.')
        print('3 - Salir.')
        op = int(input('Ingrese opción: '))

        if(op == 1):
            opcion1(cosecha)

        elif(op == 2):
            opcion2(cosecha, listacamion)

        elif(op == 3):
            salir()

if __name__ == '__main__':
    os.system("cls")
    listacamion = []
    cosecha = claseCosecha()
    cargaCamion(listacamion)
    cargaCosecha(cosecha)
    menu(cosecha, listacamion)