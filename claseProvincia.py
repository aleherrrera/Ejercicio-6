class Provincia(object):

    __nombre= None
    __capital=None
    __habitantes=None
    __departamentos=None

    def __init__(self,nombre,capital,habitantes,departamentos):
        self.__nombre=self.requerido(nombre,'Nombre requerido')
        self.__capital=self.requerido(capital,'Capital requerido')
        self.__habitantes=self.requerido(habitantes,'Habitantes requerido')
        self.__departamentos=self.requerido(departamentos,'Departamentos requerido')

    def getNombre(self):
        return self.__nombre
    def getCapital(self):
        return self.__capital
    def getHabitantes(self):
        return self.__habitantes
    def getDepartamentos(self):
        return self.__departamentos

    def requerido(self,valor,mensaje):
        if not valor:
            raise ValueError(mensaje)
        return valor

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            __atributos__=dict(
                                nombre=self.__nombre,
                                capital=self.__capital,
                                habitantes=self.__habitantes,
                                departamentos=self.__departamentos
                            )
            )
        return d