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

    def __radd__(self, hora):
        h = self.getHora() + hora.getHora()
        min = self.getMin() + hora.getMin()
        s = self.getSeg() + hora.getSeg()

        if(h > 23):
            h = h - 24
            d = hora.getDia() + 1
        
        if(min >= 60):
            h += 1
            min = min - 60
        
        if(s >= 60):
            min += 1
            s = s - 60
            
        aux = claseFechaHora(d, hora.getMes(), hora.getAño(), h, min, s)
        return aux

    def __add__(self, hora):
        aux = self
        h = self.__hora + hora.getHora()
        min = self.__min + hora.getMin()
        s = self.__seg + hora.getSeg()

        if(s >= 60):
            min += 1
            s = s - 60

        if(min >= 60):
            h += 1
            min = min - 60

        if(h > 23):
            h = h - 24
            d = hora.getDia() + 1

        if(hora.getMes() == 4 or hora.getMes() == 6 or hora.getMes() == 9 or hora.getMes() == 11):
            if(hora.getDia() > 30):
                hora.setDia(30)
                hora.aumentaMes()
        elif(hora.getMes() == 1 or hora.getMes() == 3 or hora.getMes() == 5 or hora.getMes() == 7 or hora.getMes() == 8 or hora.getMes() == 10 or hora.getMes() == 12):
            if(hora.getDia() > 31):
                if(hora.getMes() == 12):
                    hora.aumentaAño()
                    hora.setMes()
                else:
                    hora.aumentaMes()
                    hora.setDia(31) 
        else:
            if(((año % 4) == 0 and (año % 100) != 0) or (año % 400) == 0):
                if(hora.getDia() > 29):
                    hora.setDia(29)
                else:
                    if(hora.getDia() > 28):
                        hora.setDia(28)
                hora.aumentaMes()

        aux = claseFechaHora(d, hora.getMes(), hora.getAño(), h, min, s)
        return aux