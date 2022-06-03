class Artefacto:
    __marca = ''
    __modelo = ''
    __color = ''
    __paisFabricacion = ''
    __precioBase = float

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisFabricacion = paisFabricacion
        self.__precioBase = precioBase

    def __str__(self):
        cadena = '\nMarca: ' + self.__marca
        cadena += '\nModelo: ' + self.__modelo
        cadena += '\nColor: ' + self.__color
        cadena += '\nPais de Fabricación: ' + self.__paisFabricacion
        cadena += '\nPrecio Base: $' + str(self.__precioBase)
        return cadena

    def getImporte(self):
        return self.__precioBase

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    def getColor(self):
        return self.__color

    def getPais(self):
        return self.__paisFabricacion

    def calcularImporteTotal (self):
        pass
    

"""     @abc.abstractmethod
    def getImporteVenta(self):
        pass

    @abc.abstractmethod
    def obtenerArtefacto(self):
        pass """