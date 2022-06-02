class Calefactor:
    __marca: str
    __modelo: str

    def __init__ (self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo

    def __str__(self):
        cadena = '\nMarca: ' + self.__marca
        cadena += '\nModelo: ' + self.__modelo
        return cadena

    def calcularConsumo (self, cant, costo):
        pass
    