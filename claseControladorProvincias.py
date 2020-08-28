import re
import requests
from vistaProvincias import ProvinciasView, NewProvincia
from claseManejadorProvincias import ManejadorProvincia

class ControladorProvincias(object):

    def __init__(self,repo,vista):
        self.repo=repo
        self.vista=vista
        self.seleccion=-1
        self.provincias= list(repo.obtenerListaProvincias())

    def crearProvincia(self):
        nuevaProvincia= NewProvincia(self.vista).show()
        if nuevaProvincia:
            provincia= self.repo.agregarProvincia(nuevaProvincia)
            self.provincias.append(provincia)
            self.vista.agregarProvincia(provincia)
    def getApiKey(self):
        key = "1680391ead4ade58e792335abfa10f26"
        return key
    def seleccionarProvincia(self,index):
        self.seleccion=index
        provincia=self.provincias[index]
        complete_url = 'https://api.openweathermap.org/data/2.5/weather?q=' + provincia.getCapital() + '&units=metric&appid=' + self.getApiKey()
        r = requests.get(complete_url)
        x = r.json()
        datos = (x['main'])
        self.vista.verProvinciaEnForm(provincia,datos)
    def start(self):
        for c in self.provincias:
            self.vista.agregarProvincia(c)
        self.vista.mainloop()
    def salirGrabarDatos(self):
        self.repo.grabarDatos()