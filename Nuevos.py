from Vehiculos import Vehiculo

class Nuevo(Vehiculo):
    __version=''

    def __init__(self,marca,modelo,puertas,color,precioBase,version):
        super().__init__(marca,modelo,puertas,color,precioBase)
        self.__version=version

    def getPorcentaje(self):
        patentamiento=0.1
        version=0
        if self.__version=='full':
            version=0.02
        porcentaje=patentamiento+version
        return porcentaje

    def Informacion(self):
        cadena = '%s %s    %d     %s   $%.2f   %s    $%.2f' % (self.getMarca(), self.getModelo(), self.getPuertas(), self.getColor(),
                                                               self.getPrecioBase(), self.__version, self.getImporte())
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
                version=self.__version
            )
        )
        return d
