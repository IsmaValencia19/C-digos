from claseFechaHora import claseFechaHora
import os
os.system("cls")

def validar(d, mes, año, h, m, s):
    if(a in range(3000)):
        if(mes in range(13)):
            if((mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)):
                if(d in range(31)):
                    if(h in range(24)):
                        if(m in range(60)):
                            if(s in range(60)):
                                return True
                            else:
                                print('Para los segundos los valores válidos son de 0...59.')
                                return False
                        else:
                            print('Para los minutos los valores válidos son de 0...59.')
                            return False
                    else:
                        print('Para las horas los valores válidos son de 0...23.')
                        return False
                else:
                    print('Los valores válidos para un dia en el mes', mes,'son de 1...30.')
                    return False
            elif((mes == 1) or (mes ==3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12)):
                if(d in range(32)):
                    if(h in range (24)):
                        if(m in range(60)):
                            if(s in range(60)):
                                return True
                            else:
                                print('Para los segundos los valores válidos son de 0...59.')
                                return False
                        else:
                            print('Para los minutos los valores válidos son de 0...59.')
                            return False
                    else:
                        print('Para las horas los valores válidos son de 0...23.')
                        return False
                else:
                    print('Los valores válidos para un dia en el mes', mes,'son de 1...31.')
                    return False
            elif((mes == 2) and (((año % 4) == 0 and (año % 100) != 0) or (año % 400) == 0)):
                if(d in range(30)):
                    if(h in range (24)):
                        if(m in range(60)):
                            if(s in range(60)):
                                return True
                            else:
                                print('Para los segundos los valores válidos son de 0...59.')
                                return False
                        else:
                            print('Para los minutos los valores válidos son de 0...59.')
                            return False
                    else:
                        print('Para las horas los valores válidos son de 0...23.')
                        return False
                else:
                    print("Los valores válidos para un dia en el mes", mes, 'son de 1...29.')
                    return False
            else:
                if(d in range(29)):
                    if(h in range (24)):
                        if(m in range(60)):
                            if(s in range(60)):
                                return True
                            else:
                                print('Para los segundos los valores válidos son de 0...59.')
                                return False
                        else:
                            print('Para los minutos los valores válidos son de 0...59.')
                            return False
                    else:
                        print('Para las horas los valores válidos son de 0...23.')
                        return False
                else:
                    print("Los valores válidos para un dia en el mes", mes, 'son de 1...28.')
                    return False

if __name__ == '__main__':
    d = int(input('Ingrese dia: '))
    mes = int(input('Ingrese mes: '))
    a = int(input('Ingrese año: '))
    h = int(input('Ingrese hora: '))
    m = int(input('Ingrese minutos: '))
    s = int(input('Ingrese segundos: '))
    if validar(d, mes, a, h, m, s):
        r = claseFechaHora()
        r1 = claseFechaHora(d, mes, a)
        r2 = claseFechaHora(d, mes, a, h, m, s)
        r.Mostrar()
        r1.Mostrar()
        r2.Mostrar()  
        print()
        r.PonerEnHora(5)
        r.Mostrar()
        print()
        r2.PonerEnHora(13, 30)
        r2.Mostrar()
        r.PonerEnHora(14, 30, 25)
        r.Mostrar()
        print()                         
        r.AdelantarHora(3)
        r.Mostrar()
        print()
        r1.AdelantarHora(1, 15)
        r1.Mostrar()