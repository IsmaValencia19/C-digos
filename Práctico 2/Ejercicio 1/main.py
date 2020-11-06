from ClaseEmail import Email
from dominios import contador
from Validador import ValidaFlotante, ValidaEntero, ValidaEmail, ValidaCadenaAlfanumerica, ValidaCadenaAlfabetica
import os

if __name__ == '__main__':
    os.system("cls")

    nom = ValidaCadenaAlfabetica('Ingrese su nombre: ')
    id = str(input('Ingrese id de cuenta: '))
    dom = ValidaCadenaAlfabetica('Ingrese el dominio: ')
    tipdom = ValidaCadenaAlfabetica('Ingrese el tipo de dominio: ')
    contra = str(input('Ingrese su contraseña: '))
    mail = Email(id, dom, tipdom, contra)
    print('\nEstimado', nom, 'te enviaremos tus mensajes a la dirección %s.'% (mail))

    print('\nSI PRESIONA UNA TECLA SEGUIRA AL SIGUIENTE ITEM.')
    os.system("pause")
    
    os.system("cls")
    print('>>>Modificar contraseña<<<')
    band = False
    while band == False:
        contraActual = input('\nIngrese contraseña actual: ')
        if (contraActual == mail.getCont()):
            contraNueva = input('Ingrese nueva contraseña: ')
            mail.setCont(contraNueva)
            print('Contraseña actualizada.')
            band = True
        else:
            print('Contraseña incorrecta.')
    
    print('\nSI PRESIONA UNA TECLA SEGUIRA AL SIGUIENTE ITEM.')
    os.system("pause")

    os.system("cls")
    correo = ValidaEmail('Ingrese cuenta de email para generar un objeto: ')
    email = mail.crearCuenta(correo)
    print('\nObjeto generado:', email)

    print('\nSI PRESIONA UNA TECLA SEGUIRA AL SIGUIENTE ITEM.')
    os.system("pause")

    os.system("cls")
    print('>>>CONTADOR DE DOMINIOS<<<\n')
    dominios = contador()
    dominios.testing()
    print(dominios)
    dominio = ValidaCadenaAlfabetica('Ingrese un dominio: ')
    cant = dominios.buscardominio(dominio)
    print('Hay', cant, 'cuenta\s con el dominio %s.' % (dominio))

    print('\nPRESIONE PARA FINALIZAR.')
    os.system("pause")