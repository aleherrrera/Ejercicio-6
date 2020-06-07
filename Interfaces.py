from zope.interface import Interface

class IConjunto(Interface):

    def insertarElemento(posicion,elementp):
        pass

    def agregarElemento(posicion,elemento):
        pass

    def mostrarElemento(posicion):
        pass
    