import csv 
from claseJugador import Jugador

class ManJugador:
    __lista = []

    def __init__ (self):
        self.__lista = []

    def __str__ (self):
        s = ""
        for jugador in self.__lista:
            s += str( jugador ) + '\n'
        return s

    def agrega (self, unJugador):
        self.__lista.append( unJugador )

    def test (self):
        archivo = open( 'Jugadores.csv', encoding = 'utf-8' )
        reader = csv.reader( archivo, delimiter = ';' )
        next( reader )
        for fila in reader:
            unJugador = Jugador( fila[0], fila[1], fila[2], fila[3], fila[4] )
            self.agrega( unJugador )
        archivo.close()

    def getObjeto (self, i):
        return self.__lista[ i ]
