from claseCAMION import claseCamion
from claseCOSECHA import claseCosecha
from validar import entero , cadena , nombre , flotante , alfanum
import csv

def cargaCamion(lista):
    archivo = open('camiones.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for fila in reader:
        if( entero('ID', fila[0]) and nombre('Nombre', fila[1]) and alfanum('Patente', fila[2]) and cadena('Marca del camión', fila[3]) and entero('Tara', fila[4])) == 1:
            aux = claseCamion((fila[0]), fila[1], fila[2], fila[3], fila[4])
            lista.append(aux)

def cargaCosecha(cosecha):
    archivo = open('cosechas.csv')
    reader = csv.reader(archivo, delimiter = ',')
    for fila in reader:
        cosecha.agregar(int(fila[0]), int(fila[1]), fila[2])

def buscar(id, lista):
    i = 0
    while i < len(lista):
        if i == id:
            a, b = lista[i].getDatos()
            return(a, b)
        i += 1