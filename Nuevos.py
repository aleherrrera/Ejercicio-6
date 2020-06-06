from Vehiculos import Vehiculo

class Nuevo(Vehiculo):
    __version=''

    def __init__(self,marca,modelo,puertas,color,precioBase,version):
        super().__init__(marca,modelo,puertas,color,precioBase)
        self.__version=version

    def getInfo(self):
        return self.__version

    def getPorcentaje(self):
        patentamiento=0.1
        version=0
        if self.__version=='full':
            version=0.02
        porcentaje=patentamiento+version
        return porcentaje

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
