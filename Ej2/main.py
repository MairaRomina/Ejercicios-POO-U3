from claseManFlor import ManejadorF
from claseManRamo import ManejadorR
from claseMenu import Menu

if __name__ == '__main__':
    arregloFlor = ManejadorF(10) #tengo que darle la dimension del arreglo
    listaRamo = ManejadorR()

    arregloFlor.testFlor()
    print( arregloFlor )


    menu = Menu()
    
    salir = False
    while not salir:
        print('-------------------- MENU --------------------')
        print('1. Registrar venta de un ramo')
        print('2. Mostrar el nombre de las 5 flores mas vendidas')
        print('3. Mostrar flores vendidas')
        print('4. Salir')
        
        op = input('Opcion: ')
        salir = menu.opcion( op, listaRamo, arregloFlor )
        #print( lista )