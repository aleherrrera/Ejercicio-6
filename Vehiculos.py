class Vehiculo(object):
    __marca=''
    __modelo=''
    __puertas=0
    __color=''
    __precioBase=0.0

    def __init__(self,marca,modelo,puertas,color,precioBase):
        self.__marca=marca
        self.__modelo=modelo
        self.__puertas=puertas
        self.__color=color
        self.__precioBase=precioBase

    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getPuertas(self):
        return self.__puertas
    def getColor(self):
        return self.__color
    def getPrecioBase(self):
        return self.__precioBase

    def setBase(self):
        precio=float(input('Ingresar el precio base: $'))
        self.__precioBase=precio
        return self.__precioBase

    def getImporte(self):
        importe=self.__precioBase+(self.__precioBase*self.getPorcentaje())
        return importe

    def __str__(self):
        cadena='Modelo: %s Puertas: %d Precio: $%.2f'%(self.__modelo,self.__puertas,self.getImporte())
        return cadena