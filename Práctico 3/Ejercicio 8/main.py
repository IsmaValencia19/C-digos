from ClaseManejadorEmpleados import ManejaEmpleados, tesorero, gerente
from interfaceTesorero import ITesorero
from interfaceGerente import IGerente
import os

def test(me):
    os.system("cls")
    band = False
    while not band:
        print('==== Acceso a Cuenta ====')
        usuario = input('Ingrese usuario: ')
        clave = input('Ingrese contraseña: ')
        if usuario.lower() == 'uTesorero'.lower() and clave == 'ag@74ck':
            tesorero(ITesorero(me))
            band = True
        elif usuario.lower() == 'uGerente'.lower() and clave == 'ufC77#!1':
            gerente(IGerente(me))
            band = True
        else:
            os.system("cls")
            print('ERROR, datos incorrectos.\n')

if __name__ == '__main__':
    me = ManejaEmpleados(8)
    me.cargaArre()
    test(me)