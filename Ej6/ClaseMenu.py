from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa

class Menu:

    __switcher = None

    def __init__(self):
        self.__switcher = {
                            1: self.opcion1,
                            2: self.opcion2,
                            3: self.opcion3,
                            4: self.opcion4,
                            5: self.opcion5,
                            6: self.opcion6,
                            7: self.salir
                            }

    def mostrarMenu(self, lista):
        salir = False
        while not salir:
            print("\n************** Empresa Comercial *********************")
            print("********************* Menu *****************************\n"
                  "1. Insertar un aparato en cualquier posición de la colección"
                  "\n2. Agregar un aparato a la colección"
                  "\n3. Mostrar un tipo de aparato de la colección a partir de una posicion"
                  "\n4. Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea Phillips"
                  "\n5. ostrar la marca de todos los lavarropas que tienen carga superior"
                  "\n6. Mostrar para todos los aparatos que la empresa tiene a la venta"
                  "\n7. Salir")
            op = int(input('Ingrese una opcion: '))
            if op in range(1, 8) and type(op) is not str:
                self.opcion(op, lista)
                salir = op == 7
            else:
                print('La opción ingresada no es valida. Ingrese una opción válida')

    def getSwitcher(self):
        return self.__switcher

    def opcion(self, op, lista):
        func = self.__switcher.get(op, lambda: print("Opción no válida"))
        func(lista)

    def opcion1(self, lista): #INSERTA NODO ADENTRO DE LA LISTA
        print('\n1. Insertar un aparato en cualquier posición de la colección')
        op = input('Ingrese la letra del aparato que desea ingresar, T: Televisor, H: Heladera o L: Lavarropa: ')
        if op == 'T':
            marca = input('Ingrese marca del artefacto: ')
            modelo = input('Ingrese el modelo del artefacto: ')
            color = input('Ingrese el color: ')
            pais = input('Ingrese el pais de fabricacion: ')
            precio = input('Ingrese el precio base: ')
            pantalla = input('Ingrese tipo de pantalla: crt, vga, svga, plasma, lcd, TouchScreen, MultiTouch: ')
            pulgada = input('Ingrese pulgadas: ')
            definicion = input('Ingrese tipo de definicion: SD, HD, FULL HD: ')
            internet = input('Conexion a internet, True o False: ')
            unObjeto = Televisor( marca, modelo, color, pais, precio, pantalla, pulgada, definicion, internet )
        elif op == 'H':
            marca = input('Ingrese marca del artefacto: ')
            modelo = input('Ingrese el modelo del artefacto: ')
            color = input('Ingrese el color: ')
            pais = input('Ingrese el pais de fabricacion: ')
            precio = input('Ingrese el precio base: ')
            capacidad = input('Ingrese la capacidad en litros de la heladera: ')
            freezer = input('Ingrese True: tiene freezer o False: no tiene freezer:  ')
            ciclica = input('Ingrese True: si es ciclica o False: no es ciclica:  ')
            unObjeto = Heladera( marca, modelo, color, pais, precio, capacidad, freezer, ciclica )
        elif op == 'L':
            marca = input('Ingrese marca del artefacto: ')
            modelo = input('Ingrese el modelo del artefacto: ')
            color = input('Ingrese el color: ')
            pais = input('Ingrese el pais de fabricacion: ')
            precio = input('Ingrese el precio base: ')
            capacidad = input('Ingrese la capacidad del lavarropas en kg: ')
            velocidad = input('Ingrese la velocidad de centrifugado en rpm: ')
            cantidad = input('Ingrese la cantidad de programas que tiene: ')
            tipo = input('Ingrese el tipo de carga: Frontal o Superior: ')
            unObjeto = Lavarropa( marca, modelo, color, pais, precio, capacidad, velocidad, cantidad, tipo )
        else:
            print('Error')
        pos = int(input('Ingrese la posicion: '))
        try:
            lista.insertarAparato( unObjeto, pos )
            lista.mostrarTodaLista()
        except IndexError:
            print('ERROR! No fue posible ingresar el nodo en esa posicion')

    def opcion2(self, lista): #INSERTA AL PRINCIPIO DE LA LISTA
        print('\n2. Agregar un aparato a la colección')
        op = input('Ingrese la letra del aparato que desea ingresar, T: Televisor, H: Heladera o L: Lavarropa: ')
        if op == 'T':
            marca = input('Ingrese marca del artefacto: ')
            modelo = input('Ingrese el modelo del artefacto: ')
            color = input('Ingrese el color: ')
            pais = input('Ingrese el pais de fabricacion: ')
            precio = input('Ingrese el precio base: ')
            pantalla = input('Ingrese tipo de pantalla: crt, vga, svga, plasma, lcd, TouchScreen, MultiTouch: ')
            pulgada = input('Ingrese pulgadas: ')
            definicion = input('Ingrese tipo de definicion: SD, HD, FULL HD: ')
            internet = input('Conexion a internet, True o False: ')
            unObjeto = Televisor( marca, modelo, color, pais, precio, pantalla, pulgada, definicion, internet )
        elif op == 'H':
            marca = input('Ingrese marca del artefacto: ')
            modelo = input('Ingrese el modelo del artefacto: ')
            color = input('Ingrese el color: ')
            pais = input('Ingrese el pais de fabricacion: ')
            precio = input('Ingrese el precio base: ')
            capacidad = input('Ingrese la capacidad en litros de la heladera: ')
            freezer = input('Ingrese True: tiene freezer o False: no tiene freezer:  ')
            ciclica = input('Ingrese True: si es ciclica o False: no es ciclica:  ')
            unObjeto = Heladera( marca, modelo, color, pais, precio, capacidad, freezer, ciclica )
        elif op == 'L':
            marca = input('Ingrese marca del artefacto: ')
            modelo = input('Ingrese el modelo del artefacto: ')
            color = input('Ingrese el color: ')
            pais = input('Ingrese el pais de fabricacion: ')
            precio = input('Ingrese el precio base: ')
            capacidad = input('Ingrese la capacidad del lavarropas en kg: ')
            velocidad = input('Ingrese la velocidad de centrifugado en rpm: ')
            cantidad = input('Ingrese la cantidad de programas que tiene: ')
            tipo = input('Ingrese el tipo de carga: Frontal o Superior: ')
            unObjeto = Lavarropa( marca, modelo, color, pais, precio, capacidad, velocidad, cantidad, tipo )
        else:
            print('Error')
        lista.insertarPila( unObjeto )
        lista.mostrarTodaLista()

    def opcion3(self, lista): #BUSCA UNA POSICION DE LA LISTA
        print('\n3. Mostrar un tipo de aparato de la colección')
        indice = int(input('Ingrese la posicion: '))
        lista.MostrarAparato( indice - 1 )

    def opcion4(self, lista):
        print('\n4. Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea Phillips')
        lista.buscarMarca()

    def opcion5(self, lista):
        print('\n5. Mostrar la marca de todos los lavarropas que tienen carga superior')
        lista.buscaTipoLavarropa()

    def opcion6(self, lista):
        print('\n6. Mostrar para todos los aparatos que la empresa tiene a la venta')
        lista.listar()

    def salir(self, lista):
        print('\n Los datos fueron guardados en el archivo aparatoselectricos.json')