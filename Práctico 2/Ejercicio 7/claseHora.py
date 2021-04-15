from claseFechaHora import FechaHora

class Hora:
    __hora = 0
    __min = 0
    __seg = 0

    def __init__(self, hora = 0, m = 0, seg = 0):
        if(0 <= hora < 24):
            self.__hora = hora
        else:
            print('ERROR: La hora no es valida.')

        if(0 <= m < 60):
            self.__min = m
        else:
            print('ERROR: Los minutos no son validos.')

        if(0 <= seg < 60):
            self.__seg = seg
        else:
            print('ERROR: Los segundo no son validos.')
 
    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg

    def __radd__(self, fechahora):
        h = self.getHora() + fechahora.getHora()
        m = self.getMin() + fechahora.getMin()
        s = self.getSeg() + fechahora.getSeg()
        fechahora.verificarhora(d, fechahora.getMes(), fechahora.getAño(), h, m, s)
        aux = FechaHora(d, fechahora.getMes(), fechahora.getAño(), h, m, s)
        return aux

    def __add__(self, fechahora):
        h = self.__hora + fechahora.getHora()
        m = self.__min + fechahora.getMin()
        s = self.__seg + fechahora.getSeg()
        fechahora.PonerEnHora(h, m, s)
        return fechahora

    def __str__(self):
        return '{}:{}:{}'.format(self.__hora, self.__min, self.__seg) 