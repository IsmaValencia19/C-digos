from tkinter import *
from tkinter import ttk, messagebox
from tkinter import font

class Aplicacion():
    __ventana = None
    __peso = None
    __altura = None

    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry('322x220')
        self.__ventana.title('Calculadora de IMC')

        self.__peso = StringVar()
        self.__altura = StringVar()
        self.resultado = StringVar()
        self.composicion_corporal = StringVar()

        Label(self.__ventana, text = 'Calculadora de IMC').grid(column = 1, row = 0)

        Label(self.__ventana, text = 'Altura: ').grid(column = 0, row = 1)
        self.alturaEntry = Entry(self.__ventana, width = 30, textvariable = self.__altura)
        self.alturaEntry.grid(column = 1, row = 1)

        Label(self.__ventana, text = 'Peso: ').grid(column = 0, row = 2)
        self.pesoEntry = Entry(self.__ventana, width = 30, textvariable = self.__peso)
        self.pesoEntry.grid(column = 1, row = 2)

        Button(self.__ventana, text = 'Calcular', command = self.calcular, fg = 'white', bg = '#5cb95c', activeforeground = 'red', relief = 'flat', overrelief = 'raised').grid(column = 0, row = 3)
        Button(self.__ventana, text = 'Limpiar', command = self.limpiar, fg = 'white', bg = '#5cb95c', relief = 'flat', overrelief = 'raised').grid(column = 1, row = 3)
        Label(self.__ventana, text = 'cm', bg = '#ccc').grid(column = 2, row = 1, sticky = W)
        Label(self.__ventana, text = 'kg', bg = '#ccc').grid(column = 2, row = 2, sticky = W)

        frame = Frame(self.__ventana)
        frame.config(bg = '#ccc')
        frame.grid(column = 1, row = 4, sticky = (N, W, E, S))
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        frame['borderwidth'] = 2
        frame['relief'] = 'flat'

        Label(frame, text = 'Tu indice de Masa Corporal (IMC) es', bg = '#ccc').grid(column = 1, row = 4)
        Label(frame, textvariable = self.resultado, bg = '#ccc').grid(column = 2, row = 4)
        Label(frame, textvariable = self.composicion_corporal, bg = '#ccc').grid(column = 1, row = 5, sticky = E)
        
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

if __name__ == '__main__':
    app = Aplicacion()