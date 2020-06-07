from Vehiculos import Vehiculo
from datetime import datetime

class Usado(Vehiculo):
    __patente=''
    __año=0
    __km=0

    def __init__(self,marca,modelo,puertas,color,precioBase,patente,año,km):
        super().__init__(marca,modelo,puertas,color,precioBase)
        self.__patente=patente
        self.__año=año
        self.__km=km

    def getPatente(self):
        return self.__patente

    def getPorcentaje(self):
        añoActual=int(datetime.now().year)
        descuentoAño=(añoActual-self.__año)/100
        descuentoKm=0
        if self.__km>100000:
            descuentoKm=0.02
        porcentaje=-(descuentoAño+descuentoKm)
        return porcentaje

    def Informacion(self):
        cadena = '%s %s    %d     %s   $%.2f   %s %d %d    $%.2f' % (self.getMarca(), self.getModelo(), self.getPuertas(), self.getColor(),
                                                               self.getPrecioBase(),self.__patente,self.__año,self.__km, self.getImporte())
        return cadena

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                marca=self.getMarca(),
                modelo=self.getModelo(),
                puertas=self.getPuertas(),
                color=self.getColor(),
                precioBase=self.getPrecioBase(),
                patente=self.__patente,
                año=self.__año,
                km=self.__km
            )
        )
        return d
