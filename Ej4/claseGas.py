from claseCalefactor import Calefactor


class Gas ( Calefactor ):
    __matricula: str
    __calorias: int

    def __init__ (self, marca, modelo, matricula, calorias, consumo = 0):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias

    def __str__(self):
        cadena = super().__str__()
        cadena += '\nMartricula: ' + self.__matricula
        cadena += '\nCalorias: ' + str(self.__calorias)
        return cadena

    def calcularConsumo (self, cant, costo):
        consumo = self.__calorias / 1000 * cant * costo
        return consumo
