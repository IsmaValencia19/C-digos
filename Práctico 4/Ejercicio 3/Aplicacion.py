from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
import json

class Aplicacion():
    __ventana = None
    __actualizacion = None
    list = []

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('315x500')
        self.__actualizacion = StringVar()

        mainframe = ttk.Frame(self.__ventana, padding = '5 5 12 5')
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        text1 = Label(mainframe, text = 'Moneda', anchor = 'w', width = 20)
        text1.grid(column = 0, row = 0, sticky = W)
        text2 = Label(mainframe, text = 'Compra')
        text2.grid(column = 1, row = 0, sticky = N)
        text3 = Label(mainframe, text = 'Venta')
        text3.grid(column = 2, row = 0, sticky = N)

        self.cargadolar()

        dolar1 = Label(mainframe, text = self.list[0][0]).grid(column = 0, row = 1, sticky = W)
        dolar1compra = Label(mainframe, text = self.list[0][1]).grid(column = 1, row = 1, sticky = N)
        dolar1venta = Label(mainframe, text = self.list[0][2]).grid(column = 2, row = 1, sticky = N)

        dolar2 = Label(mainframe, text = self.list[1][0]).grid(column = 0, row = 2, sticky = W)
        dolar2compra = Label(mainframe, text = self.list[1][1]).grid(column = 1, row = 2, sticky = N)
        dolar2venta = Label(mainframe, text = self.list[1][2]).grid(column = 2, row = 2, sticky = N)

        dolar3 = Label(mainframe, text = self.list[2][0]).grid(column = 0, row = 3, sticky = W)
        dolar3compra = Label(mainframe, text = self.list[2][1]).grid(column = 1, row = 3, sticky = N)
        dolar3venta = Label(mainframe, text = self.list[2][2]).grid(column = 2, row = 3, sticky = N)

        dolar4 = Label(mainframe, text = self.list[3][0]).grid(column = 0, row = 4, sticky = W)
        dolar4compra = Label(mainframe, text = self.list[3][1]).grid(column = 1, row = 4, sticky = N)
        dolar4venta = Label(mainframe, text = self.list[3][2]).grid(column = 2, row = 4, sticky = N)

        dolar5 = Label(mainframe, text = self.list[4][0]).grid(column = 0, row = 5, sticky = W)
        dolar5compra = Label(mainframe, text = self.list[4][1]).grid(column = 1, row = 5, sticky = N)
        dolar5venta = Label(mainframe, text = self.list[4][2]).grid(column = 2, row = 5, sticky = N)

        dolar6 = Label(mainframe, text = self.list[5][0]).grid(column = 0, row = 6, sticky = W)
        dolar6compra = Label(mainframe, text = '$%s' % (self.list[5][1])).grid(column = 1, row = 6, sticky = N)
        dolar6venta = Label(mainframe, text = self.list[5][2]).grid(column = 2, row = 6, sticky = N)

        boton = Button(mainframe, text = 'ACTUALIZAR', command = self.actualizar)
        boton.grid(column = 0, row = 8, sticky = W)
        text4 = Label(mainframe, textvariable = self.__actualizacion)
        text4.grid(column = 1, row = 8, columnspan = 3, sticky = W)
        
        fecha = datetime.now()
        self.__actualizacion.set('Actualizado {}/{}/{} {}:{}'.format(fecha.day, fecha.month, fecha.year, fecha.hour, fecha.minute))

        self.__ventana.mainloop()

    def cargadolar(self):
        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        re = r.json()

        for i in range(len(re)):
            if re[i]['casa']['nombre'].find('Dolar') >= 0 and re[i]['casa']['compra'] != '0' and re[i]['casa']['venta'] != '0':
                dolar = [re[i]['casa']['nombre'], re[i]['casa']['compra'], re[i]['casa']['venta']]
                self.list.append(dolar)

    def actualizar(self):
        self.list = []
        self.cargadolar()
        fecha = datetime.now()
        self.__actualizacion.set('Actualizado {}/{}/{} {}:{}'.format(fecha.day, fecha.month, fecha.year, fecha.hour, fecha.minute))

if __name__ == '__main__':
    app = Aplicacion()