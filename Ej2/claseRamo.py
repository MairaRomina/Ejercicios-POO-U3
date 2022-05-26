class Ramo:
    __tamaño: int
    __lista = []

    def __init__(self, tam):
        self.__tamaño = tam
        self.__lista = []
    
    def __str__ (self):
        return 

    def __str__ (self):
        s = '* Tamaño: {} \n'.format( self.__tamaño )
        for ramo in self.__lista:
            s += str( ramo ) +  '\n'
        return s

    def agregaFlor (self, unaFlor):
        self.__lista.append( unaFlor )

    def getListaRamo (self):
        return self.__lista 

    def getTamaño (self):
        return self.__tamaño

    
    
    
