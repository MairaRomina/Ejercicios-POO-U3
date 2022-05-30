class Equipo:
    __nombre: str
    __ciudad: str

    def __init__ (self, no, ciu):
        self.__nombre = no
        self.__ciudad = ciu

    def __str__ (self):
        cadena = '\nNombre: ' + self.__nombre
        cadena += '\nCiudad: ' + self.__ciudad
        return cadena

    def getNombre (self):
        return self.__nombre

    