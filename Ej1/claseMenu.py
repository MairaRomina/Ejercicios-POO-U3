from claseManFacultad import Manejador

class Menu:
    __switcher = None

    def __init__(self):
        self.__switcher = {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.salir
        }

    def opcion (self, op, objetoLista):
        func = self.__switcher.get( op, lambda: print('Opcion no valida') )
        if op == '1' or op == '2':
            func( objetoLista )
        else:
            func()

    def opcion1 (self, objetoLista):  
        if type( objetoLista ) == Manejador:
            print('************************* Facultad *************************')
            ide = int(input('Ingrese el id de la facultad: '))
            objetoLista.mostrar( ide )
        else:
            print('Error de tipo en menu')
        
    def opcion2 (self, objetoLista): 
        if type( objetoLista ) == Manejador:
            print('************************* Carreras *************************')
            nom = input('Ingrese el nombre de una carrera: ')
            objetoLista.listarCarreras( nom )
        else:
            print('Error de tipo en menu')
        
    def salir (self):
        print('Usted salio del programa')
