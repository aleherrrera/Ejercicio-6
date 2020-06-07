import json
from pathlib import Path
from Nuevos import Nuevo
from Usados import Usado
from Lista import ListaVehiculos


class ObjectEncoder(object):
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name=d['__class__']
            class_=eval(class_name)
            if class_name=='ListaVehiculos':
                vehiculos=d['Vehiculos']
                dVehiculos = vehiculos[0]
                lista=class_()
                for i in range(len(vehiculos)):
                    dVehiculos=vehiculos[i]
                    class_name=dVehiculos.pop('__class__')
                    class_=eval(class_name)
                    atributos=dVehiculos['__atributos__']
                    unVehiculo=class_(**atributos)
                    lista.cargar(unVehiculo)
        return lista

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario