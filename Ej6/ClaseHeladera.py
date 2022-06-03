from ClaseArtefacto import Artefacto


class Heladera(Artefacto):
    __capacidad = int
    __frezzer = ''
    __ciclica = ''

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase, capacidad, frezzer, ciclica):
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__capacidad = capacidad
        self.__frezzer = frezzer
        self.__ciclica = ciclica

    def __str__(self):
        cadena = '\nMarca: ' + self.getMarca()
        cadena += '\nModelo: ' + self.getModelo()
        cadena += '\nColor: ' + self.getColor()
        cadena += '\nPais de Fabricación: ' + self.getPais()
        cadena += '\nPrecio Base: $' + str(self.getImporte())
        cadena += '\nCapacidad: ' + self.__capacidad
        cadena += '\nFrezzer: ' + str(self.__frezzer)
        cadena += '\nCíclica: ' + str(self.__ciclica)
        return cadena

    def calcularImporteTotal (self):
        total = 0
        if self.__frezzer == 'Si':
            total = (self.getImporte() * 0.05) + self.getImporte()
        elif self.__frezzer == 'No':
            total = (self.getImporte() * 0.01) + self.getImporte()
        if self.__ciclica == 'Si':
            total += self.getImporte() * 0.10
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
                capacidad = self.__capacidad,
                frezzer = self.__frezzer,
                ciclica = self.__ciclica,
            )
        )
