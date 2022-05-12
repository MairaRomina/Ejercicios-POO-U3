import csv
from claseFlor import Flor
import numpy as np

class ManejadorF:
    __cantidad: 0
    __dimension: 0
    __incremento: 5

    def __init__ (self, dimension, incremento = 5):
        self.__arreglo = np.empty( dimension, dtype = Flor )
        self.__cantidad = 0
        self.__dimension = dimension
    
    def __str__ (self):
        s = ""
        for flor in self.__arreglo:
            s += str( flor ) + "\n"
        return s
    
    def agregarFlor(self, unaFlor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize( self.__dimension )
        self.__arreglo[ self.__cantidad ] = unaFlor
        self.__cantidad += 1

    def testFlor (self):
        archivo = open( 'Flores.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        for fila in reader:
            num = int( fila[0] )
            nom = fila[1]
            color = fila[2]
            des = fila[3]
            unaFlor = Flor( num, nom, color, des )
            self.agregarFlor( unaFlor )
        archivo.close()

    #def mostrar (self):
    #    print( str( self.__arreglo ) )

    def getArreglo( self ):
        return self.__arreglo
    
    def getNombre (self, ind):
        return self.__arreglo[ind]