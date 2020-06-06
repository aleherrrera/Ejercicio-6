class Nodo(object):
    __vehiculo=None
    __siguente=None

    def __init__(self,vehiculo):
        self.__vehiculo=vehiculo
        self.__siguente=None

    def setSiguiente(self,siguiente):
        self.__siguente=siguiente
    def getSiguiente(self):
        return self.__siguente
    def getDato(self):
        return self.__vehiculo