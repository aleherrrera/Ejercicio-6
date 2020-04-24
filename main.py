from FechaHora import FechaHora

def opcion0():
    print("Adiós")

def opcion1():
    suma = r1 + r2
    r1.Mostrar()
    r2.Mostrar()
    suma.CorregirSuma(suma)
    print('Suma Hora1+Hora2:',suma)


def opcion2():
    resta = r2 - r3
    r2.Mostrar()
    r3.Mostrar()
    resta.CorregirResta(resta)
    print('Resta Hora2-Hora3: ',resta)

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    d=1
    mes=1
    a=2020
    h = int(input("Ingrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    r1 = FechaHora(d,mes,a,h, m, s)
    r1.Mostrar()

    h = int(input("Ingrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    r2 = FechaHora(d,mes,a, h, m, s)
    r2.Mostrar()

    h = int(input("Ingrese Hora: "))
    m = int(input("Ingrese Minutos: "))
    s = int(input("Ingrese Segundos: "))
    r3 = FechaHora(d, mes, a, h, m, s)
    r3.Mostrar()

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0. Salir")
        print("1. Sumar hora")
        print("2. Restar hora")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
