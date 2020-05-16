from claseConjunto import claseConjunto
import os
os.system("cls")

def opcion1():
    #Unión de Conjuntos
    print()
    print('Conjuntos:')
    print()
    A = [20, 30, 12]
    lista = claseConjunto(A)
    lista.mostrar()
    B = [20, 1, 2, 3, 4]
    lista2 = claseConjunto(B)
    lista2.mostrar()
    print()
    union = lista + lista2
    print('Unión de conjuntos:')
    print(union)
    print()
    os.system("pause")
    
def opcion2():
    #Diferencia de Conjuntos
    print()
    print('Conjuntos:')
    print()
    A = [20, 30, 12]
    lista = claseConjunto(A)
    lista.mostrar()
    B = [20, 1, 2, 3, 4]
    lista2 = claseConjunto(B)
    lista2.mostrar()
    print()
    diferencia = lista - lista2
    print('Diferencia de conjuntos:')
    print(diferencia)
    print()
    os.system("pause")

def opcion3():
    #Igualdad de Conjuntos
    print()
    print('Conjuntos:')
    print()
    A = [20, 30, 13]
    lista = claseConjunto(A)
    lista.mostrar()
    B = [20, 30, 12]
    lista2 = claseConjunto(B)
    lista2.mostrar()
    print()
    list, listt = lista == lista2
    if(list == listt):
        print('Los conjuntos son iguales.')
        print()
    else:
        print('Los conjuntos no son iguales.')
        print()
    os.system("pause")

def salir():
    print()
    print('>>>Salio del programa.<<<')
    print()

def menu():
    op = 0
    while op != 4:
        os.system("cls")
        print('1 - Union de dos conjuntos.')
        print('2 - Diferencia de dos conjuntos.')
        print('3 - Verifica si dos conjuntos son iguales.')
        print('4 - Salir.')
        op = int(input('Ingrese opción: '))

        if(op == 1):
            opcion1()
        elif(op == 2):
            opcion2()
        elif(op == 3):
            opcion3()
        elif(op == 4):
            salir()

if __name__ == '__main__':
    menu()