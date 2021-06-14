import re
 
class Paciente:
    telefonoRegex = re.compile(r"\([0-9]{3}\)[0-9]{7}")
    __nombre = None
    __apellido = None
    __telefono = None
    __altura = None
    __peso = None

    def __init__(self, nombre = None, apellido = None, telefono = None, altura = None, peso = None):
        self.__nombre = self.requerido(nombre, 'Nombre es un valor requerido')
        self.__apellido = self.requerido(apellido, 'Apellido es un valor requerido')
        self.__telefono = self.formatoValido(telefono, Paciente.telefonoRegex, 'Teléfono no tiene formato correcto')
        self.__altura = self.requerido(altura, 'Altura es un valor requerido')
        self.__peso = self.requerido(peso, 'Peso es un valor requerido')

    def requerido(self, valor, mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def formatoValido(self, valor, regex, mensaje):
        if not valor or not regex.match(valor):
            raise ValueError(mensaje)
        return valor

    def getNom(self):
        return self.__nombre

    def getApe(self):
        return self.__apellido

    def getTel(self):
        return self.__telefono

    def getAlt(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                nombre = self.__nombre,
                apellido = self.__apellido,
                telefono = self.__telefono,
                altura = self.__altura,
                peso = self.__peso
            )
        )
        return d

    def __str__(self):
        return 'Nombre y Apellido: %s %s - Teléfono: %s - Altura: %scm - Peso: %skg' % (self.__nombre, self.__apellido, self.__telefono, self.__altura, self.__peso)