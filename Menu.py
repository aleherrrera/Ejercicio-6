class Menu(object):
    def mostrarMenu(self):
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

        opcionCorrecta = False
        while not opcionCorrecta:
            opcion = int(input('Seleccione un número del 1 al 8 (0 para salir): '))
            if opcion in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
                opcionCorrecta = True
        return opcion