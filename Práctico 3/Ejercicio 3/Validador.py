import re

def ValidaEntero(mensaje):
    band = False
    while band == False:
        try:
            numero = int(input(mensaje))
            band = True
        except ValueError:
            print('ERROR: debes ingresar un número entero.')
    return numero

def ValidaFlotante(mensaje):
    band = False
    while band == False:
        try:
            numero = float(input(mensaje))
            band = True
        except ValueError:
            print('ERROR: debes ingresar un número real.')
    return numero

def ValidaCadena(mensaje):
    band = False
    while band == False:
        try:
            cad = str(input(mensaje))
            band = True
        except ValueError:
            print('ERROR: debes ingresar una cadena de caracteres.')
    return cad

def ValidaCadenaAlfabetica(mensaje):
    band = False
    while band == False:
        vari = str(input(mensaje))
        if vari.isalpha() == True:
            band = True
        else:
            print('ERROR: debes ingresar sólo letras.')
    return vari

def ValidaCadenaAlfanumerica(mensaje):
    band = False
    while band == False:
        vari = str(input(mensaje))
        if vari.isalnum() == True:
            band = True
        else:
            print('ERROR: debes ingresar letras y números sin espacios ni caracteres especiales.')
    return vari

def ValidaEmail(mensaje):
    band = False
    while band == False:
        correo = str(input(mensaje))
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',correo.lower()):
            band = True
        else:
            print("ERROR: la estructura del correo ingresada es incorrecta.\n")
    return correo