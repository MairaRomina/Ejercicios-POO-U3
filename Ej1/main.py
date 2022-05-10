from claseManFacultad import Manejador
from claseMenu import Menu

if __name__ == '__main__':
    lista = Manejador()
    lista.test()
    print( lista )

    menu = Menu()
    
    salir = False
    while not salir:
        print('-------------------- MENU --------------------')
        print('1. Mostrar informacion por facultad')
        print('2. Mostrar informacion por carrera')
        print('3. Salir')
        
        op = input('Opcion: ')
        salir = menu.opcion( op, lista )
        print( lista )
