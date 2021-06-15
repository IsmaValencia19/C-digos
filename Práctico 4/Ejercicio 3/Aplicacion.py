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
        self.__ventana.geometry('265x230')
        self.__ventana.resizable(0, 0)
        self.__actualizacion = StringVar()

        mainframe = ttk.Frame(self.__ventana, padding = '5')
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        mainframe['width'] = '300'

        style = ttk.Style()
        style.configure('T.TSeparator', background = '#77dd77')

        frame = Frame(mainframe, bg = '#77dd77')
        frame.grid(column = 0, row = 0, columnspan = 4, sticky = (N, W, E, S))
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        frame['borderwidth'] = 2

        text1 = Label(frame, text = 'Moneda', anchor = 'w', width = 19, bg = '#77dd77')
        text1.grid(column = 0, row = 0, sticky = W)
        text2 = Label(frame, text = 'Compra', anchor = 'e', width = 6, bg = '#77dd77')
        text2.grid(column = 2, row = 0, sticky = E)
        text3 = Label(frame, text = 'Venta', anchor = 'e', width = 8, bg = '#77dd77')
        text3.grid(column = 3, row = 0, sticky = E)

        self.cargadolar()

        frame1 = Frame(mainframe)
        frame1.grid(column = 0, row = 1, columnspan = 4, sticky = (N, W, E, S))
        frame1.columnconfigure(0, weight = 1)
        frame1.rowconfigure(0, weight = 1)
        frame1['borderwidth'] = 2
        dolar1 = Label(frame1, text = self.list[0][0]).grid(column = 0, row = 1, sticky = W)
        dolar1compra = Label(frame1, text = self.list[0][1]).grid(column = 2, row = 1, sticky = N)
        dolar1venta = Label(frame1, text = self.list[0][2]).grid(column = 3, row = 1, sticky = N)

        ttk.Separator(frame1, orient=HORIZONTAL, style='T.TSeparator').grid(row=2, column=0, columnspan=4, sticky="EW")

        frame2 = Frame(mainframe)
        frame2.grid(column = 0, row = 3, columnspan = 4, sticky = (N, W, E, S))
        frame2.columnconfigure(0, weight = 1)
        frame2.rowconfigure(0, weight = 1)
        frame2['borderwidth'] = 2
        dolar2 = Label(frame2, text = self.list[1][0]).grid(column = 0, row = 3, sticky = W)
        dolar2compra = Label(frame2, text = self.list[1][1]).grid(column = 2, row = 3, sticky = N)
        dolar2venta = Label(frame2, text = self.list[1][2]).grid(column = 3, row = 3, sticky = N)

        ttk.Separator(frame2, orient=HORIZONTAL, style='T.TSeparator').grid(row=4, column=0, columnspan=4, sticky="EW")

        frame3 = Frame(mainframe)
        frame3.grid(column = 0, row = 5, columnspan = 4, sticky = (N, W, E, S))
        frame3.columnconfigure(0, weight = 1)
        frame3.rowconfigure(0, weight = 1)
        frame3['borderwidth'] = 2
        dolar3 = Label(frame3, text = self.list[2][0]).grid(column = 0, row = 5, sticky = W)
        dolar3compra = Label(frame3, text = self.list[2][1]).grid(column = 2, row = 5, sticky = N)
        dolar3venta = Label(frame3, text = self.list[2][2]).grid(column = 3, row = 5, sticky = N)

        ttk.Separator(frame3, orient=HORIZONTAL, style='T.TSeparator').grid(row=6, column=0, columnspan=4, sticky="EW")

        frame4 = Frame(mainframe)
        frame4.grid(column = 0, row = 7, columnspan = 4, sticky = (N, W, E, S))
        frame4.columnconfigure(0, weight = 1)
        frame4.rowconfigure(0, weight = 1)
        frame4['borderwidth'] = 2
        dolar4 = Label(frame4, text = self.list[3][0]).grid(column = 0, row = 7, sticky = W)
        dolar4compra = Label(frame4, text = self.list[3][1]).grid(column = 2, row = 7, sticky = N)
        dolar4venta = Label(frame4, text = self.list[3][2]).grid(column = 3, row = 7, sticky = N)

        ttk.Separator(frame4, orient=HORIZONTAL, style='T.TSeparator').grid(row=8, column=0, columnspan=4, sticky="EW")

        frame5 = Frame(mainframe)
        frame5.grid(column = 0, row = 9, columnspan = 4, sticky = (N, W, E, S))
        frame5.columnconfigure(0, weight = 1)
        frame5.rowconfigure(0, weight = 1)
        frame5['borderwidth'] = 2
        dolar5 = Label(frame5, text = self.list[4][0]).grid(column = 0, row = 9, sticky = W)
        dolar5compra = Label(frame5, text = self.list[4][1]).grid(column = 2, row = 9, sticky = N)
        dolar5venta = Label(frame5, text = self.list[4][2]).grid(column = 3, row = 9, sticky = N)

        ttk.Separator(frame5, orient=HORIZONTAL, style='T.TSeparator').grid(row=10, column=0, columnspan=4, sticky="EW")

        frame6 = Frame(mainframe)
        frame6.grid(column = 0, row = 10, columnspan = 4, sticky = (N, W, E, S))
        frame6.columnconfigure(0, weight = 1)
        frame6.rowconfigure(0, weight = 1)
        frame6['borderwidth'] = 2
        dolar6 = Label(frame6, text = self.list[5][0]).grid(column = 0, row = 10, sticky = W)
        dolar6compra = Label(frame6, text = '$%s' % (self.list[5][1])).grid(column = 2, row = 10, sticky = N)
        dolar6venta = Label(frame6, text = self.list[5][2]).grid(column = 3, row = 10, sticky = N)

        ttk.Separator(frame6, orient=HORIZONTAL, style='T.TSeparator').grid(row=11, column=0, columnspan=4, sticky="EW")

        frame7 = Frame(mainframe)
        frame7.grid(column = 0, row = 12, columnspan = 4, sticky = (N, W, E, S))
        frame7.columnconfigure(0, weight = 1)
        frame7.rowconfigure(0, weight = 1)
        frame7['borderwidth'] = 2
        boton = Button(frame7, text = 'ACTUALIZAR', command = self.actualizar, bg = '#77dd77')
        boton.grid(column = 0, row = 12, sticky = W)
        text4 = Label(frame7, textvariable = self.__actualizacion)
        text4.grid(column = 1, row = 12, columnspan = 4, sticky = W)

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