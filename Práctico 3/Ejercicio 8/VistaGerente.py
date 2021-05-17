from Validador import ValidaEntero
import os

def Gerente(me):
    os.system("cls")
    gerente = ' CUENTA DE GERENTE '
    print(gerente.center(55, '='))
    cad = ' MENÚ '
    cade = ''
    print(cad.center(55, '='))
    print('1 - Modificar sueldo básico de un Empleado Planta.')
    print('2 - Mofidicar valor por hora de un Empleado Contratado.')
    print('3 - Modificar monto del viático de un Empleado Externo.')
    print(cade.center(55, '='))
    bande = False
    while not bande:
        op = ValidaEntero('Ingrese una opción: ')
        if op == 1:
            band = False
            while not band:
                dni = ValidaEntero('\nIngrese DNI de un Empleado Planta: ')
                sueldo = ValidaEntero('Ingrese nuevo sueldo básico: ')
                if me.modificarBasicoEPlanta(dni, sueldo):
                    band = True
                    bande = True
                else:
                    print('ERROR: El DNI ingresado no pertenece a un Empleado Planta.')
        elif op == 2:
            band = False
            while not band:
                dni = ValidaEntero('\nIngrese DNI de un Empleado Contratado: ')
                nuevovalor = ValidaEntero('Ingrese nuevo valor por hora: ')
                if me.modificarValorEPorHora(dni, nuevovalor):
                    band = True
                    bande = True
                else:
                    print('ERROR: El DNI ingresado no pertenece a un Empleado Contratado.')
        elif op == 3:
            band = False
            while not band:
                dni = ValidaEntero('\nIngrese DNI de un Empleado Externo: ')
                nuevovalor = ValidaEntero('Ingrese nuevo valor de viático: ')
                if me.modificarViaticoEExterno(dni, nuevovalor):
                    band = True
                    bande = True
                else:
                    print('ERROR: El DNI ingresado no pertenece a un Empleado Externo.')
        else:
            print('ERROR: opción ingresada incorrecta.\n')