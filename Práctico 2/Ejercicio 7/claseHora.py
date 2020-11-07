from claseFechaHora import claseFechaHora

class claseHora:
    __hora = 0
    __min = 0
    __seg = 0

    def __init__(self, hora = 0, min = 0, seg = 0):
        self.__hora = hora
        self.__min = min
        self.__seg = seg

    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg

    def Mostrar(self):
        print('          {}:{}:{}'.format(self.__hora, self.__min, self.__seg)) 

    def __radd__(self, fechahora):
        h = self.getHora() + fechahora.getHora()
        min = self.getMin() + fechahora.getMin()
        s = self.getSeg() + fechahora.getSeg()

        if(h > 23):
            h = h - 24
            d = fechahora.getDia() + 1
        
        if(min >= 60):
            h += 1
            min = min - 60
        
        if(s >= 60):
            min += 1
            s = s - 60
            
        aux = claseFechaHora(d, fechahora.getMes(), fechahora.getAño(), h, min, s)
        return aux

    def __add__(self, fechahora):
        aux = self
        h = self.__hora + fechahora.getHora()
        min = self.__min + fechahora.getMin()
        s = self.__seg + fechahora.getSeg()

        if(s >= 60):
            min += 1
            s = s - 60

        if(min >= 60):
            h += 1
            min = min - 60

        if(h > 23):
            h = h - 24
            d = fechahora.getDia() + 1

        if(fechahora.getMes() == 4 or fechahora.getMes() == 6 or fechahora.getMes() == 9 or fechahora.getMes() == 11):
            if(fechahora.getDia() > 30):
                fechahora.setDia(30)
                fechahora.aumentaMes()
        elif(fechahora.getMes() == 1 or fechahora.getMes() == 3 or fechahora.getMes() == 5 or fechahora.getMes() == 7 or fechahora.getMes() == 8 or fechahora.getMes() == 10 or fechahora.getMes() == 12):
            if(fechahora.getDia() > 31):
                if(fechahora.getMes() == 12):
                    fechahora.aumentaAño()
                    fechahora.setMes()
                else:
                    fechahora.aumentaMes()
                    fechahora.setDia(31) 
        else:
            if(((año % 4) == 0 and (año % 100) != 0) or (año % 400) == 0):
                if(fechahora.getDia() > 29):
                    fechahora.setDia(29)
                else:
                    if(fechahora.getDia() > 28):
                        fechahora.setDia(28)
                fechahora.aumentaMes()

        aux = claseFechaHora(d, fechahora.getMes(), fechahora.getAño(), h, min, s)
        return aux