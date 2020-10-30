from ClaseEmail import Email
from dominios import contador
import os

if __name__ == '__main__':
    os.system("cls")

    nom = input('Ingrese su nombre: ') 
    id = input('Ingrese id de cuenta: ')
    dom = input('Ingrese dominio: ')
    tipdom = input('Ingrese el tipo de dominio: ')
    contra = input('Ingrese su contraseña: ')
    mail = Email(id, dom, tipdom, contra)
    print('\nEstimado', nom, 'te enviaremos tus mensajes a la dirección', mail)

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
    band = False
    while band == False:
        correo = input('\nIngrese correo para generar un objeto: ')
        if correo.find('@') != -1:
            nuevo_email = correo.split('@')
            usuario = nuevo_email[0]
            resto = nuevo_email[1]
            if resto.find('.') != -1:
                continuacion = resto.split('.')
                dominio = continuacion[0]
                tipodominio = continuacion[1]
                uncorreo = Email(usuario, dominio, tipodominio)
                email = mail.crearCuenta(correo)
                print('\nObjeto generado:', email)
                band = True
            else:
                print('ERROR, falta el PUNTO separador del dominio y tipo de dominio.')
        else:
            print('ERROR, falta el @ en el correo ingresado.')

    print('\nSI PRESIONA UNA TECLA SEGUIRA AL SIGUIENTE ITEM.')
    os.system("pause")

    os.system("cls")
    print('>>>CONTADOR DE DOMINIOS<<<\n')
    dominios = contador()
    dominios.testing()
    print(dominios)
    dominio = input('Ingrese dominio: ')
    cant = dominios.buscardominio(dominio)
    print('Hay', cant, 'cuenta\s con el dominio %s.' % (dominio))

    print('\nPRESIONE PARA FINALIZAR.')
    os.system("pause")