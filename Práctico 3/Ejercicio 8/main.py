from ClaseManejadorEmpleados import ManejaEmpleados
from interfaceTesorero import ITesorero
from interfaceGerente import IGerente
from VistaTesorero import Tesorero
from VistaGerente import Gerente
import os

def acceso(me):
    band = False
    while not band:
        print('==== Acceso a Cuenta ====')
        usuario = input('Ingrese usuario: ')
        clave = input('Ingrese contraseña: ')
        if usuario.lower() == 'uTesorero'.lower() and clave == 'ag@74ck':
            Tesorero(ITesorero(me))
            band = True
        elif usuario.lower() == 'uGerente'.lower() and clave == 'ufC77#!1':
            Gerente(IGerente(me))
            band = True
        else:
            os.system("cls")
            print('ERROR: Datos ingresados incorrectos.\n')

if __name__ == '__main__':
    os.system("cls")
    me = ManejaEmpleados(8)
    me.cargaArre()
    acceso(me)