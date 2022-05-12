class Ramo:
    __tamaño: int

    def __init__(self, tam):
        self.__tamaño = tam
    
    def __str__ (self):
        return 'Tamaño: {}',format( self.__tamaño )

    