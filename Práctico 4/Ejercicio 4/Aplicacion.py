from tkinter import *
from tkinter import ttk
from functools import partial
from ClaseFraccion import Fraccion

class Calculadora(object):
    __ventana = None
    __operador = None
    __panel = None
    __operadorAux = None
    __primerFraccion = None
    __segundaFraccion = None
    __resultado = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Calculadora de Fracciones')
        self.__ventana.resizable(0, 0)

        style = ttk.Style()
        style.configure('BW.TFrame', background = 'white')

        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10", style='BW.TFrame')
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'

        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None

        estilo = ttk.Style()
        estilo.configure('BW.TButton', background = 'white')
        estilo.theme_use('clam')

        operatorEntry = ttk.Entry(mainframe, style='BW.TButton', width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, style='BW.TButton', width=20, textvariable=self.__panel, justify='center',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, style='BW.TButton', text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='0', command=partial(self.ponerNUMERO, '0')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=8, sticky=E)
        ttk.Button(mainframe, style='BW.TButton', text='/', command = partial(self.ponerNUMERO, '/')).grid(column = 3, row = 7, sticky = W)
        ttk.Button(mainframe, style='BW.TButton', text='C', command=self.borrarPanel).grid(column=2, row=8, sticky=W)
        ttk.Button(mainframe, style='BW.TButton', text='SIMPLIFICA', command=self.simplifica).grid(column=1, row=8, columnspan=2, sticky=W)        
        self.__panel.set('')
        panelEntry.focus()
        self.__ventana.mainloop()

    def simplifica(self):
        num1 = self.__resultado.getNumerador()
        den1 = self.__resultado.getDenominador()

        comun = self.__resultado.mcm(num1, den1) #mcd
        # se divide el numerador y el denominador en el mcd para simplificar la fracción
        resultado = Fraccion(num1 // comun, '/', den1 // comun) 
        self.__resultado = None

        self.__panel.set(str(resultado))

    def ponerNUMERO(self, numero):
        if self.__operadorAux == None:
            valor = self.__panel.get()
            self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            num, den = valor.split('/')
            fraccion = Fraccion(int(num), '/', int(den))
            self.__primerFraccion = fraccion
            self.__panel.set(numero)
            
    def borrarPanel(self):
        self.__panel.set('')
        self.__operadorAux = None
        self.__operador.set('')

    def resolverOperacion(self, fraccion1, operacion, fraccion2):
        resultado = ''

        if operacion == '+':
            resultado = fraccion1 + fraccion2
        elif operacion == '-':
            resultado = fraccion1 - fraccion2
        elif operacion == '*':
            resultado = fraccion1 * fraccion2
        elif operacion == '%':
            resultado = fraccion1 / fraccion2

        self.__panel.set(str(resultado))
        self.__resultado = resultado

    def ponerOPERADOR(self, op):
        if op == '=':
            operacion = self.__operador.get()
            valor = self.__panel.get()
            num, den = valor.split('/')
            fraccion2 = Fraccion(int(num), '/', int(den))
            self.__segundaFraccion = fraccion2
            self.resolverOperacion(self.__primerFraccion, operacion, self.__segundaFraccion)
            self.__operador.set('')
            self.__operadorAux=None
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion = self.__operador.get()
                self.__segundaFraccion = int(self.__panel.get())
                self.resolverOperacion(self.__primerFraccion, operacion, self.__segundaFraccion)
                self.__operador.set(op)
                self.__operadorAux=op