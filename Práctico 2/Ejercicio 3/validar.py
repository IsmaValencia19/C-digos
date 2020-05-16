def entero(dato = '', valor = ''):
    try:
        int(valor)
    except:
        print("ERROR: {} debe ser un valor entero.".format(dato.upper()))
        return 0
    else:
        return 1

def flotante(dato = '', valor = ''):
    try:
        flaot(valor)
    except:
        print("ERROR: {} debe ser un valor de punto flotante.".format(dato.upper()))
        return 0
    else:
        return 1

def cadena(dato = '', valor = ''):
    try:
        str(valor)
    except:
        print("ERROR: {} debe ser una cadena de caracteres.".format(dato.upper()))
        return 0
    else:
        return 1

def nombre(dato = '', valor = ''):
    for char in valor.lower():
        if  not ("a" <= char and char <= "z") or (char == " "):
            print("ERROR: {} solo puede contener letras y espacios.".format(dato.upper()))
            return 0
    else:
        return 1

def alfanum(dato = '', valor = ''):
    if not valor.isalnum():
        print("ERROR: {} debe ser un una cadena alfanumerica.".format(dato.upper()))
        return 0
    else:
        return 1