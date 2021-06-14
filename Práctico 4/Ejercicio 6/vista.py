from tkinter import *
from tkinter import ttk, messagebox
from ClaseProvincia import Provincia
import json
import requests
 
class ListaProvincia(Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.lb = Listbox(self, **kwargs)
        scroll = Scrollbar(self, command = self.lb.yview)
        self.lb.config(yscrollcommand = scroll.set)
        scroll.pack(side = RIGHT, fill = Y)
        self.lb.pack(side = LEFT, fill = BOTH, expand = 1)

    def insertar(self, provincia, index = END):
        text = '{}'.format(provincia.getNom())
        self.lb.insert(index, text)

    def borrar(self, index):
        self.lb.delete(index, index)

    def modificar(self, provincia, index):
        self.borrar(index)
        self.insertar(provincia, index)

    def bind_doble_click(self, callback):
        handler = lambda _: callback(self.lb.curselection()[0])
        self.lb.bind("<Double-Button-1>", handler)

class FormularioProvincia(LabelFrame):
    fields = ('Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos', 'Temperatura', 'Sensación térmica', 'Humedad')
    
    def __init__(self, master, **kwargs):
        super().__init__(master, text = 'Provincia', padx = 10, pady = 10, **kwargs)
        self.frame = Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = Label(self.frame, text = text)
        entry = Entry(self.frame, width = 25)
        label.grid(row = position, column = 0, pady = 5)
        entry.grid(row = position, column = 1, pady = 5)
        return entry

    def mostrarEstadoProvinciaEnFormulario(self, provincia):
        name = provincia.getNom()

        url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&units=metric&appid=877b9e061606e376a171feb1c3b7a0b0' % (name)
        r = requests.get(url)
        re = r.json()

        temp = re['main']['temp']
        feels_like = re['main']['feels_like']
        humidity = re['main']['humidity']

        values = (provincia.getNom(), provincia.getCap(), provincia.getCantidadHabitantes(), provincia.getCantidadDepartamentos(), temp, feels_like, humidity)
        for entry, value in zip(self.entries, values):
            entry.delete(0, END)
            entry.insert(0, value)

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, END)

class FormularioNuevaProvincia(LabelFrame):
    fields = ('Nombre', 'Capital', 'Cantidad de habitantes', 'Cantidad de departamentos/partidos')
    
    def __init__(self, master, **kwargs):
        super().__init__(master, text = 'Provincia', padx = 10, pady = 10, **kwargs)
        self.frame = Frame(self)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()

    def crearCampo(self, field):
        position, text = field
        label = Label(self.frame, text = text)
        entry = Entry(self.frame, width = 25)
        label.grid(row = position, column = 0, pady = 5)
        entry.grid(row = position, column = 1, pady = 5)
        return entry

    def crearProvinciaDesdeFormulario(self):
        values = [e.get() for e in self.entries]
        provincia = None
        try:
            provincia = Provincia(*values)
        except ValueError as e:
            messagebox.showerror('Error de Validación', str(e), parent = self)
        return provincia

class NuevaProvincia(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.provincia = None
        self.form = FormularioNuevaProvincia(self)
        self.btn_add = Button(self, text = 'Confirmar', command = self.confirmar)
        self.form.pack(padx = 10, pady = 10)
        self.btn_add.pack(pady = 10)

    def confirmar(self):
        self.provincia = self.form.crearProvinciaDesdeFormulario()
        if self.provincia:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.provincia

class VistaProvincia(Tk):
    def __init__(self):
        super().__init__()
        self.title('Lista de Provincias')
        self.list = ListaProvincia(self, height = 15)
        self.form = FormularioProvincia(self)
        self.btn_new = Button(self, text = 'Agregar Provincia')
        self.list.pack(side = LEFT, padx = 10, pady = 10)
        self.form.pack(padx = 10, pady = 10)
        self.btn_new.pack(side = BOTTOM, pady = 5)

    def setControlador(self, ctrl):
        self.btn_new.config(command = ctrl.crearProvincia)
        self.list.bind_doble_click(ctrl.seleccionarProvincia)

    def agregarProvincia(self, provincia):
        self.list.insertar(provincia)

    def modificarProvincia(self, provincia, index):
        self.list.modificar(provincia, index)

    def borrarProvincia(self, index):
        self.form.limpiar()
        self.list.borrar(index)

    def obtenerDetalles(self):
        return self.form.crearProvinciaDesdeFormulario()

    def verProvinciaEnForm(self, provincia):
        self.form.mostrarEstadoProvinciaEnFormulario(provincia)