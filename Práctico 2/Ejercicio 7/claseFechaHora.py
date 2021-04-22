class FechaHora:
    __dia = 0
    __mes = 0
    __año = 0
    __hora = 0
    __min = 0
    __seg = 0

    def __init__(self, dia = 1, mes = 1, año = 2020, hora = 0, m = 0, seg = 0):
        if(1 <= dia <=31):
            if mes == 2 and año % 400 == 0 and dia <= 29: 
                self.__dia = dia
            if mes == 2 and año % 400 != 0 and dia <=28:
                self.__dia = dia
            if (1 <= mes <= 7 and mes!=2 and mes % 2 !=0 and dia <= 31) or ( 8<= mes <=12 and mes % 2 == 0 and dia <= 31): 
                self.__dia = dia
            if (1 <= mes <= 7 and mes != 2 and mes % 2 == 0 and dia <= 30) or ( 8<= mes <=12 and mes % 2 != 0 and dia <= 30): 
                self.__dia = dia
        else:
            print("ERROR: El dia no es valido.")

        if(1 <= mes <= 12):
            self.__mes = mes
        else:
            print('ERROR: El mes no es valido.')

        if(año > 0):
            self.__año = año
        else:
            print('ERROR: El año no es valido.')

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

    def getDia(self):
        return self.__dia
 
    def getMes(self):
        return self.__mes

    def getAño(self):
        return self.__año

    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__min

    def getSeg(self):
        return self.__seg

    def validar(self):
        band = None
        if(self.__año in range(3000)):
            if(self.__mes in range(13)):
                if((self.__mes == 4) or (self.__mes == 6) or (self.__mes == 9) or (self.__mes == 11)):
                    if(self.__dia in range(31)):
                        if(self.__hora in range(24)):
                            if(self.__min in range(60)):
                                if(self.__seg in range(60)):
                                    band = True
                                else:
                                    #print('Para los segundos los valores válidos son de 0...59.')
                                    band = False
                            else:
                                #print('Para los minutos los valores válidos son de 0...59.')
                                band = False
                        else:
                            #print('Para las horas los valores válidos son de 0...23.')
                            band = False
                    else:
                        #print('Los valores válidos para un dia en el mes', self.__mes,'son de 1...30.')
                        band = False
                elif((self.__mes == 1) or (self.__mes ==3) or (self.__mes == 5) or (self.__mes == 7) or (self.__mes == 8) or (self.__mes == 10) or (self.__mes == 12)):
                    if(self.__dia in range(32)):
                        if(self.__hora in range (24)):
                            if(self.__min in range(60)):
                                if(self.__seg in range(60)):
                                    band = True
                                else:
                                    #print('Para los segundos los valores válidos son de 0...59.')
                                    band = False
                            else:
                                #print('Para los minutos los valores válidos son de 0...59.')
                                band = False
                        else:
                            #print('Para las horas los valores válidos son de 0...23.')
                            band = False
                    else:
                        #print('Los valores válidos para un dia en el mes', self.__mes,'son de 1...31.')
                        band = False
                elif((self.__mes == 2) and (((self.__año % 4) == 0 and (self.__año % 100) != 0) or (self.__año % 400) == 0)):
                    if(self.__dia in range(30)):
                        if(self.__hora in range (24)):
                            if(self.__min in range(60)):
                                if(self.__seg in range(60)):
                                    band = True
                                else:
                                    #print('Para los segundos los valores válidos son de 0...59.')
                                    band = False
                            else:
                                #print('Para los minutos los valores válidos son de 0...59.')
                                band = False
                        else:
                            #print('Para las horas los valores válidos son de 0...23.')
                            band = False
                    else:
                        #print("Los valores válidos para un dia en el mes", self.__mes, 'son de 1...29.')
                        band = False
                else:
                    if(self.__dia in range(29)):
                        if(self.__hora in range (24)):
                            if(self.__min in range(60)):
                                if(self.__seg in range(60)):
                                    band = True
                                else:
                                    #print('Para los segundos los valores válidos son de 0...59.')
                                    band = False
                            else:
                                #print('Para los minutos los valores válidos son de 0...59.')
                                band = False
                        else:
                            #print('Para las horas los valores válidos son de 0...23.')
                            band = False
                    else:
                        #print("Los valores válidos para un dia en el mes", self.__mes, 'son de 1...28.')
                        band = False
        return band

    def verificarhora(self, d = 0, mes = 0, a = 0, h = 0, m = 0, s = 0):
        self.__dia += d
        self.__mes += mes
        self.__año += a
        self.__hora += h
        self.__min += m
        self.__seg += s

        i = 0
        while not self.validar() and i < 30:
            if(self.__seg >= 60):
                self.__min += 1
                self.__seg = self.__seg - 60

            if(self.__min >= 60):
                self.__hora += 1
                self.__min = self.__min - 60

            if(self.__hora > 23):
                self.__dia += 1
                self.__hora = self.__hora - 24

            if(self.__mes in range(13)):    
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
                    if(((self.__año % 4) == 0 and (self.__año % 100) != 0) or (self.__año % 400) == 0):
                        if(self.__dia > 29):
                            self.__dia -= 29
                        else:
                            if(self.__dia > 28):
                                self.__dia -= 28
                        self.__mes += 1
            else:
                self.__año += 1
                self.__mes = self.__mes - 12
            i += 1

    def PonerEnHora(self, hora = 0, m = 0, seg = 0):
        self.__hora = hora
        self.__min = m
        self.__seg = seg
        self.verificarhora(0, 0, 0, 0, 0, 0)
                
    def AdelantarHora(self, hora = 0, m = 0, seg = 0):
        self.verificarhora(0, 0, 0, hora, m, seg)

    def __add__(self, fechahora):
        fecha = FechaHora(self.__dia, self.__mes, self.__año, self.__hora, self.__min, self.__seg)
        if hasattr(fechahora, 'fechahora.getDia()'):
            fecha.verificarhora(fechahora.getDia(), fechahora.getMes(), fechahora.getAño(), fechahora.getHora(), fechahora.getMin(), fechahora.getSeg())
        else:
            fecha.AdelantarHora(fechahora.getHora(), fechahora.getMin(), fechahora.getSeg())
        return fecha

    def __radd__(self, fechahora):
        fecha = FechaHora(self.__dia, self.__mes, self.__año, self.__hora, self.__min, self.__seg)
        if hasattr(fechahora, 'fechahora.getHora()'):
            fecha.verificarhora(fechahora.getDia(), fechahora.getMes(), fechahora.getAño(), fechahora.getHora(), fechahora.getMin(), fechahora.getSeg())
        else:
            fecha.verificarhora(fechahora)
        return fecha

    def verificarresta(self, d = 0, mes = 0, año = 0, h = 0, m = 0, s = 0):
        self.__dia -= d
        self.__mes -= mes
        self.__año -= año
        self.__hora -= h
        self.__min -= m
        self.__seg -= s

        i = 0
        while not self.validar() and i < 30:
            if self.__mes == 2 and self.__año % 400 == 0 and self.__dia < 1:
                a = self.__dia + 29
                self.__dia = a
                self.__mes -= 1
            if self.__mes == 2 and self.__año % 400 != 0 and self.__dia < 1:
                a = self.__dia + 28
                self.__dia = a
                self.__mes -= 1
            if (1 <= self.__mes <= 7 and self.__mes!=2 and self.__mes % 2 !=0 and self.__dia < 1) or ( 8<= self.__mes <= 12 and self.__mes % 2 == 0 and self.__dia < 1):
                a = self.__dia + 31
                self.__dia = a
                self.__mes -= 1
            if (1 <= self.__mes <= 7 and self.__mes != 2 and self.__mes % 2 == 0 and self.__dia < 1) or ( 8<= self.__mes <= 12 and self.__mes % 2 != 0 and self.__dia < 1):
                a = self.__dia + 30
                self.__dia = a
                self.__mes -= 1

            if self.__mes < 1:
                a = self.__mes + 12
                self.__mes = a
                self.__año -= 1

            if self.__hora < 0:
                a = self.__hora + 24
                self.__hora = a
                self.__dia -= 1

            if self.__min < 0:
                a = self.__min + 60
                self.__min = a
                self.__hora -= 1

            if self.__seg < 0:
                a = self.__seg + 60
                self.__seg = a
                self.__min -= 1
            i += 1
            
    def __sub__(self, fechahora):
        fecha = FechaHora(self.__dia, self.__mes, self.__año, self.__hora, self.__min, self.__seg)
        if hasattr(fechahora, 'fechahora.getDia()'):
            fecha.verificarresta(fechahora.getDia(), fechahora.getMes(), fechahora.getAño(), fechahora.getHora(), fechahora.getMin(), fechahora.getSeg())
        else:
            fecha.verificarresta(fechahora)
        return fecha

    def __str__(self):
        return '{}/{}/{}  {}:{}:{}'.format(self.__dia, self.__mes, self.__año, self.__hora, self.__min, self.__seg)