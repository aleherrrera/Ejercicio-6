from zope.interface import implementer
from Interfaces import IConjunto
from Nodos import Nodo
from Nuevos import Nuevo
from Usados import Usado

@implementer(IConjunto)

class ListaVehiculos(object):
    __comienzo=None
    __actual=None
    __indice=0
    __tope=0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def crear(self):
        opcion = str(input('Ingresar estado(nuevo/usado): '))
        if opcion.lower() == 'nuevo':
            marca='Ford'
            modelo = str(input('Ingrese modelo de {}: '.format(marca)))
            puertas = int(input('Ingrese cantidad de puertas: '))
            color = str(input('Ingrse color: '))
            precioBase = float(input('Ingrese precio base: $'))
            version = str(input('Ingrese version: '))
            vehiculo = Nuevo(marca,modelo, puertas, color, precioBase, version)
        else:
            if opcion.lower() == 'usado':
                marca = str(input('Ingrese marca: '))
                modelo = str(input('Ingrese modelo de marca: '))
                puertas = int(input('Ingrese cantidad de puertas: '))
                color = str(input('Ingrse color: '))
                precioBase = float(input('Ingrese precio base: $'))
                patente = str(input('Ingrese patente: '))
                año = int(input('Ingrese año: '))
                km = int(input('Ingrese kilometraje del vehiculo: '))
                vehiculo = Usado(marca, modelo, puertas, color, precioBase, patente, año, km)
            else:
                raise ValueError
        return vehiculo

    def cargar(self,vehiculo=None):
        if vehiculo==None:
            vehiculo=self.crear()
        nodo = Nodo(vehiculo)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual=nodo
        self.__tope+=1

    def insertarElemento(self,posicion,vehiculo):
        if posicion>=0 and posicion < self.__tope:
            aux = self.__comienzo
            if posicion==0:
                if vehiculo!=None:
                    nodo=Nodo(vehiculo)
                    self.__comienzo=nodo
                    nodo.setSiguiente(aux)
                    self.__actual=nodo
                    self.__tope+=1
            else:
                i=1
                ant = aux
                aux = aux.getSiguiente()
                while i!=posicion:
                    i+=1
                    ant = aux
                    aux = aux.getSiguiente()
                if vehiculo!=None:
                    nodo=Nodo(vehiculo)
                    nodo.setSiguiente(aux)
                    ant.setSiguiente(nodo)
                    self.__tope+=1
        else:
            raise IndexError

    def agregarElemento(self,vehiculo):
        if vehiculo!=None:
            ant = self.__comienzo
            aux = ant.getSiguiente()
            while aux!=None:
                ant=aux
                aux=aux.getSiguiente()
            nodo=Nodo(vehiculo)
            nodo.setSiguiente(aux)
            ant.setSiguiente(nodo)
            self.__tope+=1
        else:
            raise ValueError

    def mostrarElemento(self,posicion):
        if posicion>=0 and posicion < self.__tope:
            aux=self.__comienzo
            i=0
            while i!=posicion:
                aux=aux.getSiguiente()
                i+=1
            if isinstance(aux.getDato(),Nuevo):
                print('Tipo de objeto: Vehiculo nuevo')
            else:
                if isinstance(aux.getDato(),Usado):
                    print('Tipo de objeto: Vehiculo usado')
        else:
            raise IndexError

    def modificaBase(self,patente):
        aux= self.__comienzo
        i=0
        bandera = False
        while bandera==False and i < self.__tope:
            if isinstance(aux.getDato(),Usado) and patente==aux.getDato().getPatente():
                bandera=True
            else:
                aux = aux.getSiguiente()
                i+=1
        if bandera==True:
            print(aux.getDato())
            aux.getDato().setBase()
            print('Precio: ${0:.2f}'.format(aux.getDato().getImporte()))

    def Economico(self):
        min=999999999
        for dato in self:
            if min > dato.getImporte():
                min= dato.getImporte()
                vehiculo=dato
        if isinstance(vehiculo,Nuevo):
            print('Marca Modelo Puertas Color Precio Base Version Importe de Venta ')
            print(vehiculo.Informacion())
        else:
            print('Marca Modelo Puertas Color Precio Base Patente Año Kilometros Importe de Venta')
            print(vehiculo.Informacion())

    def toJSON(self):
        d = dict(
            __class__=self.__class__.__name__,
            Vehiculos=[vehiculo.toJSON() for vehiculo in self]
        )
        return d