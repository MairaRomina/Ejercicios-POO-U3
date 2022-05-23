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
            arre = objetoArreglo.getArreglo()
            #objetoArreglo.mostrar()
            objetoLista.registraVenta( arre )
        else:
            print('Error de tipo en menu')
        
    def opcion2 (self, objetoLista, objetoArreglo): 
        if isinstance( objetoLista, ManejadorR) and isinstance( objetoArreglo, ManejadorF ):
            print('************************* Carreras *************************')
            nom = input('Ingrese el nombre de una carrera: ')
            objetoLista.listarCarreras( nom )
        else:
            print('Error de tipo en menu')

    def opcion3 (self, objetoLista, objetoArreglo): 
        if isinstance( objetoLista ) == ManejadorR and isinstance( objetoArreglo ) == ManejadorF:
            print('************************* Carreras *************************')
            nom = input('Ingrese el nombre de una carrera: ')
            objetoLista.listarCarreras( nom )
        else:
            print('Error de tipo en menu')   

    def salir (self):
        print('Usted salio del programa')