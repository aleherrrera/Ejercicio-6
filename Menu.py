import os
from Lista import ListaVehiculos
from ObjectEncoder import ObjectEncoder


class Menu(object):
    __switcher=None
    __lista= None
    __jsonF=ObjectEncoder()
    def __init__(self,lista):
        self.__switcher = { 0:self.salir,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.opcion6,
                            7:self.opcion7,
                            8:self.opcion8
                            }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def salir(self):
        print('Salir')
    def opcion1(self):
        posicion = int(input('Ingresar posicion: '))
        os.system('cls')
        try:
            self.__lista.insertarElemento(posicion - 1)
        except IndexError:
            print('Posicion incorrecta')
        except ValueError:
            print('Estado incorrecto')
    def opcion2(self):
        try:
            self.__lista.agregarElemento()
        except ValueError:
            print('Estado incorrecto')
    def opcion3(self):
        posicion = int(input('Ingresar posicion: '))
        os.system('cls')
        try:
            self.__lista.mostrarElemento(posicion - 1)
        except IndexError:
            print('Posicion incorrecta')
    def opcion4(self):
        patente = str(input('Ingresar patente: '))
        os.system('cls')
        self.__lista.modificaBase(patente)
    def opcion5(self):
        self.__lista.Economico()
    def opcion6(self):
        d = self.__lista.toJSON()
        self.__jsonF.guardarJSONArchivo(d, 'vehiculos.json')
        print('Datos guardados')
    def opcion7(self):
        diccionario = self.__jsonF.leerJSONArchivo('vehiculos.json')
        self.__lista = self.__jsonF.decodificarDiccionario(diccionario)
    def opcion8(self):
        for dato in self.__lista:
            print(dato)
