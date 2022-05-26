from claseManFlor import ManejadorF
from claseManRamo import ManejadorR

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '4': self.salir
        }

    def opcion (self, op, objetoLista, objetoArreglo):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2' or op == '3':
            func( objetoLista, objetoArreglo )
        else:
            func()

    def opcion1 (self, objetoLista, objetoArreglo):  
        if isinstance( objetoLista, ManejadorR) and isinstance( objetoArreglo, ManejadorF ):
            print('************************* Registrar venta *************************')
            print('Ingrese el tamaño del ramo: 1 Ramo chico 4 Ramo mediano 6 RAmo mediano')
            opcion = int(input('Opcion: '))
            objetoLista.registraVenta( opcion, objetoArreglo )
        else:
            print('Error de tipo en menu')
        
    def opcion2 (self, objetoLista, objetoArreglo): 
        if isinstance( objetoLista, ManejadorR) and isinstance( objetoArreglo, ManejadorF ):
            """ 2. Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos. """
            print('************************* Mostrar el nombre de las 5 flores  más pedidas en un ramo *************************')
            objetoLista.masPedidas( objetoArreglo )
        else:
            print('Error de tipo en menu')

    def opcion3 (self, objetoLista, objetoArreglo): 
        if isinstance( objetoLista, ManejadorR) and isinstance( objetoArreglo, ManejadorF ):
            print('************************* Carreras *************************')
            print('Ingrese el tamaño del ramo: chico mediano grande')
            opcion = input('Opcion: ')
            objetoLista.masVendidas( opcion )
        else:
            print('Error de tipo en menu')   

    def salir (self):
        print('Usted salio del programa')
