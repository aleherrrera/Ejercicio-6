
class FechaHora:

    __dia = 0
    __mes = 0
    __anio = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__hora = hora
        self.__minutos = minuto
        self.__segundos = segundo

    def __str__(self):
        return '{}/{}/{}/  {}:{}:{}'.format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos)

    def Mostrar(self):
        s = 'DIA/MES/AÑO    HORA:MIN:SEG\n'
        print('{}{}/{}/{}          {}:{}:{}'.format(s,self.__dia,self.__mes,self.__anio,self.__hora,self.__minutos,self.__segundos))

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAnio(self):
        return self.__anio

    def getHora(self):
        return self.__hora

    def getMin(self):
        return self.__minutos

    def getSeg(self):
        return self.__segundos

    def Bisiesto(self,anio):
        m = anio%4
        if m == 0:
            m = anio%100
            if m == 0:
                m = anio%400
                if m == 0:
                    return 29
                else:
                    return 28

    def Mes(self,mes):
        if (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
            return 31
        if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11):
            return 30
        else:
            a = self.Bisiesto(self.__anio)
            return a

    def PonerEnHora(self,hora=0,min=0,seg=0):
        self.__hora = hora
        self.__minutos = min
        self.__segundos = seg

    def __add__(self, otraHora):
        return FechaHora(self.__dia+0,self.__mes+0,self.__anio+0,self.__hora + otraHora.getHora(),self.__minutos + otraHora.getMin(),self.__segundos + otraHora.getSeg())

    def CorregirSuma(self,suma):

        if suma.getSeg() > 59:
            suma.__segundos = suma.getSeg() - 60
            suma.__minutos += 1
        else:
            suma.__segundos = suma.getSeg()
        if suma.getMin() > 59:
            suma.__minutos = suma.getMin() - 60
            suma.__hora += 1
        else:
            suma.__minutos = suma.getMin()
        if suma.getHora() > 23:
            suma.__hora = suma.getHora() - 24
            suma.__dia += 1
            m = suma.Mes(suma.__mes)
            if suma.__dia > m:
                suma.__mes += 1
                if suma.__mes > 12:
                    suma.__anio += 1
        else:
            suma.__hora = suma.getHora()

    def __sub__(self, otraHora):
        return FechaHora(self.__dia-0,self.__mes-0,self.__anio-0,self.__hora - otraHora.getHora(),self.__minutos - otraHora.getMin(),self.__segundos - otraHora.getSeg())

    def CorregirResta(self,resta):
        if resta.getSeg() < 0:
            resta.__segundos = resta.getSeg() + 60
            resta.__minutos -= 1
        else:
            resta.__segundos = resta.getSeg()
        if resta.getMin() < 0:
            resta.__minutos = resta.getMin() + 60
            resta.__hora -= 1
        else:
            resta.__minutos = resta.getMin()
        if resta.getHora() < 0:
            resta.__hora = resta.getHora() + 24
            resta.__dia -= 1
            print(resta.getDia())
            if resta.getDia() == 0:
                resta.__mes -= 1
                if resta.getMes() == 0:
                    resta.__mes = 12
                    print()
                    resta.__anio -= 1
                    m = resta.Mes(resta.__mes)
                    resta.__dia = m
        else:
            resta.__hora = resta.getHora()
