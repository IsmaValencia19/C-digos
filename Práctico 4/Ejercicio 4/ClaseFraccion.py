class Fraccion():
    __numerador = 0
    __separador = ''
    __denominador = 0

    def __init__(self, numerador = 0, separador = '/', denominador = 0):
        self.__numerador = numerador
        self.__separador = separador
        self.__denominador = denominador
 
    def getNumerador(self):
        return self.__numerador

    def getDenominador(self):
        return self.__denominador

    def __add__(self, fraccion2):
        den1 = self.getDenominador()
        den2 = fraccion2.getDenominador()

        if den1 > den2:
            A = den1
            B = den2
        else:
            A = den2
            B = den1

        while B:
            mcd = B
            B = A % B
            A = mcd
        
        den3 = (den1 * den2) // mcd

        num1 = self.getNumerador()
        num2 = fraccion2.getNumerador()

        num3 = (num1 * (den3 // den1)) + (num2 * (den3 // den2))

        comun = self.simplifica(num3, den3)

        return Fraccion(num3 // comun, '/', den3 // comun)

    def __sub__(self, fraccion2):
        den1 = self.getDenominador()
        den2 = fraccion2.getDenominador()

        if den1 > den2:
            A = den1
            B = den2
        else:
            A = den2
            B = den1

        while B:
            mcd = B
            B = A % B
            A = mcd
        
        den3 = (den1 * den2) // mcd

        num1 = self.getNumerador()
        num2 = fraccion2.getNumerador()

        num3 = (num1 * (den3 // den1)) - (num2 * (den3 // den2))

        comun = self.simplifica(num3, den3)

        return Fraccion(num3 // comun, '/', den3 // comun)

    def __mul__(self, fraccion2):
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = fraccion2.getNumerador()
        den2= fraccion2.getDenominador()

        num3 = (num1 * num2)
        den3 = (den1 * den2)

        comun = self.simplifica(num3, den3)

        return Fraccion(num3 // comun, '/', den3 // comun)

    def __truediv__(self, fraccion2):
        num1 = self.getNumerador()
        den1 = self.getDenominador()
        num2 = fraccion2.getNumerador()
        den2= fraccion2.getDenominador()

        num3 = (num1 * den2)
        den3 = (den1 * num2)

        comun = self.simplifica(num3, den3)

        return Fraccion(num3 // comun, '/', den3 // comun)
        
    def simplifica(self, m, n):
        while m % n != 0:
            mViejo = m
            nViejo = n

            m = nViejo
            n = mViejo % nViejo
        return n    

    def __str__(self):
        return '%s%s%s' % (self.__numerador, self.__separador, self.__denominador)