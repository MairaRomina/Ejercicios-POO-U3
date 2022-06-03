from ClaseArtefacto import Artefacto


class Televisor(Artefacto):
    __tipoPantalla = ''
    __pulgadas = ''
    __tipoDefinicion = ''
    __conexionInternet = ''

    def __init__(self, marca, modelo, color, paisFabricacion, precioBase, tipoPantalla, pulgadas, tipoDefinicion,
                 conexionInternet):
        super().__init__(marca, modelo, color, paisFabricacion, precioBase)
        self.__tipoPantalla = tipoPantalla
        self.__pulgadas = pulgadas
        self.__tipoDefinicion = tipoDefinicion
        self.__conexionInternet = conexionInternet

    def __str__(self):
        cadena = '\nMarca: ' + self.getMarca()
        cadena += '\nModelo: ' + self.getModelo()
        cadena += '\nColor: ' + self.getColor()
        cadena += '\nPais de Fabricación: ' + self.getPais()
        cadena += '\nPrecio Base: $' + str(self.getImporte())
        cadena += '\nTipo de Pantalla: ' + self.__tipoPantalla
        cadena += '\nPulgadas: ' + self.__pulgadas
        cadena += '\nTipo de Definición: ' + self.__tipoDefinicion
        cadena += '\nConexión a Internet: ' + str(self.__conexionInternet)
        return cadena

    def calcularImporteTotal (self):
        total = 0
        if self.__tipoDefinicion == 'SD':
            total = (self.getImporte() * 0.01) + self.getImporte()
        elif self.__tipoDefinicion == 'HD':
            total = (self.getImporte() * 0.02) + self.getImporte()
        elif self.__tipoDefinicion == 'FULL HD':
            total = (self.getImporte() * 0.03) + self.getImporte()
        if self.__conexionInternet == 'Si':
            total += self.getImporte() * 0.10
        return total

    def toJSON(self):
        return dict(
            __class__ = self.__class__.__name__,
            __atributos__=dict(
                marca = self.getMarca(),
                modelo = self.getModelo(),
                precioBase = self.getImporte(),
                color = self.getColor(),
                paisFabricacion = self.getPais(),
                tipoPantalla = self.__tipoPantalla,
                pulgadas = self.__pulgadas,
                tipoDefinicion = self.__tipoDefinicion,
                conexionInternet = self.__conexionInternet
            )
        )