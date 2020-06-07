import os
from Lista import ListaVehiculos
from Menu import Menu

if __name__ == '__main__':

    lista=ListaVehiculos()
    menu=Menu(lista)
    salir=False
    while not salir:
        print('Menú de Opciones:\n--------------------------')
        print("1. Insertar vehciulo en una posicion")
        print("2. Agregar vehiculo")
        print("3. Mostrar un vehiculo de una posicion")
        print("4. Modificar precio base de un vehiculo")
        print("5. Datos del vehiculo mas economico")
        print("6. Guardar datos")
        print("7. Leer datos")
        print("8. Mostrar datos")
        print("0. Salir")
        op = int(input('Ingresar una opcion: '))
        os.system('cls')
        menu.opcion(op)
        salir = op == 0
    print('Salir')
