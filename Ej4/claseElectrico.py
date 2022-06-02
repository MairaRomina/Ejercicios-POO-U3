from ctypes.wintypes import INT
from claseCalefactor import Calefactor


class Electrico ( Calefactor ):
    __potencia: int

    def __init__ (self, marca, modelo, potencia, consumo = 0):
        super().__init__(marca, modelo)
        self.__potencia = potencia
    
    def __str__(self):
        cadena = super().__str__()
        cadena += '\nPotencia Máxima: ' + str(self.__potencia)
        return cadena

    def calcularConsumo (self, cant, costo):
        consumo = self.__potencia / 1000 * cant * costo
        return consumo