from tkinter import *
from tkinter import ttk, messagebox
import requests
import json

class Aplicacion():
    __ventana = None
    __dolar = None
    __peso = None
    __valordeDolar = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('235x85')
        self.__ventana.title('Conversor de moneda')

        self.__dolar = StringVar()
        self.__peso = StringVar()

        mainframe = ttk.Frame(self.__ventana, padding = "5 5 12 5")
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        self.__dolar.trace('w', self.calcular)
        self.dolarEntry = ttk.Entry(mainframe, width = 7, textvariable = self.__dolar)
        self.dolarEntry.grid(column = 1, row = 0, sticky = (W))
        Label(mainframe, text = 'dólares').grid(column = 2, row = 0, sticky = W)
        Label(mainframe, text = 'es equivalente a').grid(column = 0, row = 1, sticky = E)
        Label(mainframe, textvariable = self.__peso).grid(column = 1, row = 1, sticky = (W))
        Label(mainframe, text = 'pesos').grid(column = 2, row = 1, sticky = W)
        ttk.Button(mainframe, text = 'Salir', command = self.__ventana.destroy).grid(column = 2, row = 2, sticky = W)
        self.dolarEntry.focus()
        self.__ventana.mainloop()

    def calcular(self, *args):
        url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        r = requests.get(url)
        re = r.json()

        for i in range(len(re)):
            if re[i]['casa']['nombre'] == 'Oficial':
                precioVenta = re[i]['casa']['venta']

        venta = float(precioVenta.replace(',', '.'))

        if self.dolarEntry.get() != '':
            try:
                valor = float(self.dolarEntry.get())
                self.__peso.set(venta * valor)
            except ValueError:
                messagebox.showerror(title = 'Error de tipo', message = 'Debe ingresar un valor numérico')
                self.__dolar.set('')
                self.dolarEntry.focus()
        else:
            self.__peso.set('')