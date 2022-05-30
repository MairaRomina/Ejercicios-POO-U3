import csv
from claseEquipo import Equipo
import numpy as np

class ManEquipo:
    __cantidad = 0
    __dimension = 4
    __incremento = 4

    def __init__ (self):
        self.__arreglo = np.empty(self.__dimension, dtype = Equipo)
        self.__cantidad = 0
        self.__dimension = 4
        self.__incremento = 4

    def __str__ (self):
        s = ""
        for equipo in self.__arreglo:
            s += str( equipo ) + '\n'
        return s

    def agrega (self, unEquipo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad] = unEquipo
        self.__cantidad += 1

    def test (self):
        archivo = open( 'Equipos.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        # self.__dimension = int(next( reader )[0])
        # self.__cantidad = self.__dimension
        next( reader )
        for fila in reader:
            unEquipo = Equipo( fila[0], fila[1] )
            self.agrega( unEquipo )
        archivo.close()

    def getObjeto (self, i):
        return self.__arreglo[ i ]