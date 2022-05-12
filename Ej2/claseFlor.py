from turtle import color


class Flor:
    __numero: int
    __nombre: str
    __color: str
    __descripcion: str
    __flores = []

    def __init__ (self, num, nom, col, des):
        self.__numero = num
        self.__nombre = nom
        self.__color = col
        self.__descripcion = des
        self.__flores = []

    def __str__ (self):
        return '{} {:5} {:5} {}'.format( self.__numero, self.__nombre, self.__color, self.__descripcion )

    