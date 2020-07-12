import re
import requests
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
    def getApiKey(self):
        key="1680391ead4ade58e792335abfa10f26"
        return key
    def getTemp(self):
        temp=None
        complete_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + self.getNombre() + '&units=metric&appid=' + self.getApiKey()
        r = requests.get(complete_url)
        x = r.json()
        temp = float(x['main']['temp'])
        return temp
    def getSensTermica(self):
        sens=None
        complete_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + self.getNombre() + '&units=metric&appid=' + self.getApiKey()
        r = requests.get(complete_url)
        x = r.json()
        sens = float(x['main']['feels_like'])
        return sens
    def getHumedad(self):
        humedad= None
        complete_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + self.getNombre() + '&units=metric&appid=' + self.getApiKey()
        r = requests.get(complete_url)
        x = r.json()
        humedad = int(x['main']['humidity'])
        return humedad
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