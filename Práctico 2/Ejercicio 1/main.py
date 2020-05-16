from Clases import claseEmail
from dominios import contador
import os 
import csv
import re

#def verificadominio(dom):
#    lineaCompleta = []
#    cont = 0    #contador de dominios
#    archivo = open('10correos.csv')
#    reader = csv.reader(archivo, delimiter = ',')
#    for fila in reader:
#        lineaCompleta = fila
#        print(lineaCompleta)

    #se cuenta el dominio para los 10 correos del archivo .csv
#    for elemento in lineaCompleta:
#        if re.findall(dom, elemento):
#            cont += 1

#    archivo.close()
#    return cont

#función que divide en partes el correo para poder generar un objeto de la clase email
#def crearCuenta(correo):
#        a, b = correo.split('@')
#        b, c = b.split('.')
#        mail = claseEmail(a, b, c)
#        return mail

def testing():
    listacorreos = []
    archivo = open('10correos.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for fila in reader:
        listacorreos = fila
        print(listacorreos)
    
    for i in reader:
        if listacorreos.find('@'):
            nuevo_email = listacorreos.split('@')
            usuario = nuevo_email[0]
            resto = nuevo_email[1]
            continuacion = resto.split('.')
            dominio = continuacion[0]
            tipodominio = continuacion[1]
            print(listacorreos)
        else:
            print('El correo no tiene arroba')
            
    archivo.close()

if __name__ == '__main__':
#    os.system("cls")
#    nom = input('Ingrese su nombre: ') 
#    id = input('Ingrese id de cuenta: ')
#    dom = input('Ingrese dominio: ')
#    tipdom = input('Ingrese el tipo de dominio: ')
#    contra = input('Ingrese su contraseña: ')
#    mail = claseEmail(id, dom, tipdom, contra)
#    os.system("cls")
    
#    print('Estimado', nom, 'te enviaremos tus mensajes a la dirección', mail)
    
#    print('\n>>>Modificar contraseña<<<\n')
#    contraActual = input('Ingrese contraseña actual: ')
#    if (contraActual == mail.getCont()):
#        contraNueva = input('Ingrese nueva contraseña: ')
#        mail.setCont(contraNueva)
#        print('Contraseña actualizada.')
#    else:
#        print('Contraseña incorrecta.')
    
#    os.system("pause")
#    os.system("cls")
#    correo = input('Ingrese correo para generar un objeto: ')
#    email = crearCuenta(correo)
#    print('Objeto generado:', email)

#   os.system("pause")
#    os.system("cls")
#    dominio = input('Ingrese dominio: ')
#    cant = verificadominio(dominio)
#    print('Hay', cant, 'cuenta\s con el dominio', dominio)
    cantdominios = contador()
    cantdominios.dominios()
    dominio = input('Ingrese dominio: ')
    cant = cantdominios.buscardominio(dominio)
    print('Hay', cant, 'cuenta\s con el dominio', dominio)
    testing()