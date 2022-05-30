import datetime

class Contrato:
    __inicio: datetime
    __final: datetime
    __pago: float
    __equipo: None
    __jugador: None
    
    def __init__ (self, ini, fi, pa, equipo, jugador):
        self.__inicio = ini
        self.__final = fi
        self.__pago = pa
        self.__equipo = equipo #referencia al equipo de cada contrato
        self.__jugador = jugador #referencia al jugador de cada contrato

    def __str__ (self):
        cadena = '--------------------------------------------------------'
        cadena += '\nFecha de inicio: ' + str(self.__inicio)
        cadena += '\nFecha final: ' + str(self.__final)
        cadena += '\nPago: ' + str(self.__pago) + '\n'
        cadena += '* Equipo *'
        cadena += str( self.__equipo ) + '\n'
        cadena += '* Jugador *'
        cadena += str( self.__jugador )
        return cadena

    def getJugador (self):
        return self.__jugador

    def getEquipo (self):
        return self.__equipo

    def getFinal (self):
        return self.__final

    def getInicio (self):
        return self.__inicio

    def getPago (self):
        return self.__pago
    
    
    