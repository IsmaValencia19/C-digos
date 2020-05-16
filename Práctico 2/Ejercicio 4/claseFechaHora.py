class claseFechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __min = 0
    __seg = 0

    def __init__(self, dia = 1, mes = 1, año = 2020, hora = 0, min = 0, seg = 0):
        self.__dia = dia
        self.__mes = mes
        self.__año = año
        self.__hora = hora
        self.__min = min
        self.__seg = seg

    def Mostrar(self):
        print('{}/{}/{}  {}:{}:{}'.format(self.__dia, self.__mes, self.__año, self.__hora, self.__min, self.__seg)) 

    def PonerEnHora(self, hora = 0, min = 0, seg = 0):
        self.__hora = hora
        self.__min = min
        self.__seg = seg
        if(self.__seg >= 60):
            self.__min += 1
            self.__seg = self.__seg - 60
        if(self.__min >= 60):
            self.__hora += 1
            self.__min = self.__min - 60
        if(self.__hora > 23):
            self.__dia += 1
            self.__hora = self.__hora - 24
                
    def AdelantarHora(self, hora = 0, min = 0, seg = 0):
        self.__hora += hora
        self.__min += min
        self.__seg += seg

        if(self.__seg >= 60):
            self.__min += 1
            self.__seg = self.__seg - 60

        if(self.__min >= 60):
            self.__hora += 1
            self.__min = self.__min - 60

        if(self.__hora > 23):
            self.__dia += 1
            self.__hora = self.__hora - 24

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