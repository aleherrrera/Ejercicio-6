from Lista import ListaVehiculos
from ObjectEncoder import ObjectEncoder
from Menu import Menu

if __name__ == '__main__':

    lista=ListaVehiculos()
    jsonF = ObjectEncoder()
    bandera = True
    while bandera:
        menu = Menu()
        opcion = menu.mostrarMenu()
        if opcion == 1:
            posicion = int(input('Ingresar posicion: '))
            try:
                lista.insertarElemento(posicion - 1)
            except IndexError:
                print('Posicion incorrecta')
            except ValueError:
                print('Estado incorrecto')
        else:
            if opcion == 2:
                try:
                    lista.agregarElemento()
                except ValueError:
                        print('Estado incorrecto')
            else:
                if opcion == 3:
                    posicion = int(input('Ingresar posicion: '))
                    try:
                        lista.mostrarElemento(posicion - 1)
                    except IndexError:
                        print('Posicion incorrecta')
                else:
                    if opcion == 4:
                        patente = str(input('Ingresar patente: '))
                        lista.modificaBase(patente)
                    else:
                        if opcion == 5:
                            lista.Economico()
                        else:
                            if opcion == 6:
                                d = lista.toJSON()
                                jsonF.guardarJSONArchivo(d, 'vehiculos.json')
                                print('Datos guardados')
                            else:
                                if opcion == 7:
                                    diccionario = jsonF.leerJSONArchivo('vehiculos.json')
                                    lista = jsonF.decodificarDiccionario(diccionario)
                                else:
                                    if opcion == 8:
                                        for dato in lista:
                                            print(dato)
                                    else:
                                        bandera = False
                                        print('Ha seleccionado salir, hasta la vuelta')
