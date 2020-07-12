from claseProvincia import Provincia

class ManejadorProvincia:
    indice=0
    __provincias=None

    def __init__(self):
        self.__provincias=[]

    def agregarProvincia(self,provincia):
        provincia.rowid=ManejadorProvincia.indice
        ManejadorProvincia.indice += 1
        self.__provincias.append(provincia)

    def getListaProvincias(self):
        return self.__provincias

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            provincias=[provincia.toJSON() for provincia in self.__provincias]
        )
        return d