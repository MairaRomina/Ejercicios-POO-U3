from claseRamo import Ramo

class ManejadorR:
    __lista = [] #si solo incializo la lista aca se vuelve variable de clase

    def __init__ (self):
        self.__lista = [] #tengo que colocar esto para evitar eso

    def __str__ (self):
        s = ""
        for ramo in self.__lista:
            s += str( ramo ) + '\n'
        return s
    
    def registraVenta (self, arre):
        print(str(arre))
        flor = input('Ingrese el numero de flor que desee: ')
        print(flor)
