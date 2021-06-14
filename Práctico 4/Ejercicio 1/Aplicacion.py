from tkinter import *
from tkinter import ttk, messagebox, font

class Aplicacion():
    __ventana = None
    __peso = None
    __altura = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('417x240')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.config(bg = 'white')
        self.__ventana.resizable(0, 0)

        self.__peso = StringVar()
        self.__altura = StringVar()
        self.resultado = StringVar()
        self.composicion_corporal = StringVar()

        frame2 = Frame(self.__ventana)
        frame2.config(bg = '#f5f5f5')
        frame2.grid(column = 0, row = 0, columnspan = 5)
        frame2.columnconfigure(0, weight = 1)
        frame2.rowconfigure(0, weight = 1)
        frame2['borderwidth'] = 2
        frame2['relief'] = 'flat'
        fuente = font.Font(weight = 'bold')
        fuente2 = font.Font(weight = 'bold', size = 9)
        Label(frame2, text = 'Calculadora de IMC', font = fuente, bg = '#f5f5f5').grid(padx = 130, pady = 8, column = 0, row = 0, columnspan = 5)

        Label(self.__ventana, text = 'Altura: ', bg = 'white', fg = '#757575').grid(pady = 20, column = 0, row = 1, sticky = W)
        self.alturaEntry = Entry(self.__ventana, textvariable = self.__altura, width = 55)
        self.alturaEntry.grid(column = 1, row = 1, sticky = E, columnspan = 2)

        Label(self.__ventana, text = 'Peso: ', bg = 'white', fg = '#757575').grid(column = 0, row = 2, sticky = W)
        self.pesoEntry = Entry(self.__ventana, textvariable = self.__peso, width = 55)
        self.pesoEntry.grid(column = 1, row = 2, sticky = E, columnspan = 2)

        Button(self.__ventana, text = 'Calcular', command = self.calcular, width = 20, fg = 'white', bg = '#5cb95c', activeforeground = 'red', relief = 'flat', overrelief = 'raised').grid(pady = 7, column = 0, row = 3, columnspan = 2, sticky = N)
        Button(self.__ventana, text = 'Limpiar', command = self.limpiar, width = 20, fg = 'white', bg = '#5cb95c', relief = 'flat', overrelief = 'raised').grid(column = 1, row = 3, columnspan = 2, sticky = E)
        Label(self.__ventana, text = 'cm', bg = '#f5f5f5').grid(column = 3, row = 1, sticky = W)
        Label(self.__ventana, text = ' kg', bg = '#f5f5f5').grid(column = 3, row = 2, sticky = W)

        frame = Frame(self.__ventana)
        frame.config(bg = '#f5f5f5')
        frame.grid(column = 1, row = 4, sticky = N, columnspan = 2)
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        frame['borderwidth'] = 2
        frame['relief'] = 'flat'

        Label(frame, text = 'Tu indice de Masa Corporal (IMC) es', bg = '#f5f5f5', fg = '#5cb95c').grid(column = 1, row = 4)
        Label(frame, textvariable = self.resultado, bg = '#f5f5f5', fg = '#5cb95c', font = fuente2).grid(column = 2, row = 4)
        Label(frame, textvariable = self.composicion_corporal, bg = '#f5f5f5', fg = '#5cb95c').grid(column = 1, row = 5, sticky = E)
        
        self.__ventana.mainloop()

    def calcular(self):
            try:
                peso = float(self.pesoEntry.get())
                altura = float(self.alturaEntry.get())
                resultado = peso / (altura / 100)**2
                self.resultado.set('%.2f Kg/m2' % (resultado))
                if resultado < 18.5:
                    self.composicion_corporal.set('Peso inferior al normal')
                elif 18.5 <= resultado <= 24.9:
                    self.composicion_corporal.set('Peso normal')
                elif 25 <= resultado <= 29.9:
                    self.composicion_corporal.set('Peso superior al normal')
                elif resultado >= 30:
                    self.composicion_corporal.set('Obesidad')
            except ValueError:
                messagebox.showerror(title = 'ERROR, tipo de dato incorrecto', message = 'Debe ingresar un valor numérico')

    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.resultado.set('')
        self.composicion_corporal.set('')