from zope.interface import Interface

class IConjunto(Interface):

    def insertarElemento(posicion):
        pass

    def agregarElemento(posicion):
        pass

    def mostrarElemento(posicion):
        pass
    