from ClaseArtefacto import Artefacto


class Lavarropa(Artefacto):
    __capacidadLavado = int
    __velocidadCentrifugado = ''
    __cantidadProgramas = ''
    __tipoCarga = ''

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase, capacidadLavado, velocidadCentrifugado,
                 cantidadProgramas, tipoCarga):
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__capacidadLavado = capacidadLavado
        self.__velocidadCentrifugado = velocidadCentrifugado
        self.__cantidadProgramas = cantidadProgramas
        self.__tipoCarga = tipoCarga

    def __str__(self):
        cadena = '\nMarca: ' + self.getMarca()
        cadena += '\nModelo: ' + self.getModelo()
        cadena += '\nColor: ' + self.getColor()
        cadena += '\nPais de Fabricación: ' + self.getPais()
        cadena += '\nPrecio Base: $' + str(self.getImporte())
        cadena += '\nCapacidad de Lavado: ' + str(self.__capacidadLavado)
        cadena += '\nVelocidad de Centrifugado: ' + self.__velocidadCentrifugado
        cadena += '\nCantidad de Programas: ' + self.__cantidadProgramas
        cadena += '\nTipo de Carga: ' + self.__tipoCarga
        return cadena

    def getTipo (self):
        return self.__tipoCarga

    def calcularImporteTotal (self):
        total = 0
        if self.__capacidadLavado <= 5:
            total = (self.getImporte() * 0.01) + self.getImporte()
        elif self.__capacidadLavado > 5:
            total = (self.getImporte() * 0.03) + self.getImporte()
        return total

    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                precioBase = self.getImporte(),
                color = self.getColor(),
                paisFabricacion = self.getPais(),
                capacidadLavado = self.__capacidadLavado,
                velocidadCentrifugado = self.__velocidadCentrifugado,
                cantidadProgramas = self.__cantidadProgramas,
                tipoCarga = self.__tipoCarga
            )
        )