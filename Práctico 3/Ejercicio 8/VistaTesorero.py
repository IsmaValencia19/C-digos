from Validador import ValidaEntero
import os

def Tesorero(me):
    os.system("cls")
    tesorero = ' CUENTA DE TESORERO '
    print(tesorero.center(50, '='))
    band = False
    while not band:
        dni = ValidaEntero('Ingrese DNI de un empleado para verificar el sueldo: ')
        if me.gastosSueldoPorEmpleado(dni):
            band = True
        else:
            print('ERROR: DNI ingresado incorrecto.\n')