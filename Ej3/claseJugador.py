class Jugador:
    __nombre: str
    __dni: str
    __ciudad: str
    __pais: str
    __fecha: str

    def __init__ (self, nom, dni, ciu, pa, fe):
        self.__nombre = nom
        self.__dni = dni
        self.__ciudad = ciu
        self.__pais = pa
        self.__fecha = fe
    
    def __str__ (self):
        cadena = '\nNombre: ' + self.__nombre
        cadena += '\nDNI: ' + self.__dni
        cadena += '\nCiudad Natal: ' + self.__ciudad
        cadena += '\nPais Origen: ' + self.__pais
        cadena += '\nFecha Nacimiento: ' + self.__fecha
        return cadena

    def getDni (self):
        return self.__dni

    def getNombre (self):
        return self.__nombre