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

        if(self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11):
            if(self.__dia > 30):
                self.__dia -= 30
                self.__mes += 1
        elif(self.__mes == 1 or self.__mes == 3 or self.__mes == 5 or self.__mes == 7 or self.__mes == 8 or self.__mes == 10 or self.__mes == 12):
            if(self.__dia > 31):
                if(self.__mes == 12):
                    self.__año += 1
                    self.__mes = 1
                else:
                    self.__mes += 1
                    self.__dia -= 31
        else:
            if(((año % 4) == 0 and (año % 100) != 0) or (año % 400) == 0):
                if(self.__dia > 29):
                    self.__dia -= 29
                else:
                    if(self.__dia > 28):
                        self.__dia -= 28
                self.__mes += 1

        aux = claseFechaHora(d, hora.getMes(), hora.getAño(), h, min, s)
        return aux