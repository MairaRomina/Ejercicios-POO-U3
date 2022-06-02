from claseCalefactor import Calefactor
import csv
from claseElectrico import Electrico
from claseGas import Gas
import numpy as np

class ManCalefactor:
    __cantidad = 0
    __dimension = 0
    __incremento = 10

    def __init__ (self, dimension ):
        self.__arreglo = np.empty( dimension, dtype = Calefactor )
        self.__cantidad = 0
        self.__incremento = 10
        self.__dimension = dimension
    
    def __str__(self):
        s = "\n***** Calefactores*****\n"
        for calefactor in self.__arreglo:
            s += str( calefactor ) + '\n'
        return s

    def agregar (self, unCalefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize( self.__dimension )
        self.__arreglo[ self.__cantidad ] = unCalefactor
        self.__cantidad += 1
    
    def cargaCalefactor (self):
        archivo = open( 'calefactor-a-gas.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        next( reader )
        for fila in reader:
            unCalefactor = Gas( fila[0], fila[1], fila[2], int(fila[3]) )
            self.agregar( unCalefactor )
        archivo.close()

        archivo = open( 'calefactor-electrico.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        next( reader )
        for fila in reader:
            unCalefactor = Electrico( fila[0], fila[1], int(fila[2]) )
            self.agregar( unCalefactor )
        archivo.close()
    
    def calcular (self, costoG, cantG, costoE, cantE):
        minG = 999999999999
        minE = 999999999999
        auxG = 0
        auxE = 0
        for calefactor in self.__arreglo:
            if isinstance(calefactor, Gas):
                consumoG = calefactor.calcularConsumo(costoG, cantG)
                if consumoG < minG:
                    minG = consumoG
                    auxG = calefactor

            elif isinstance(calefactor, Electrico):
                consumoE = calefactor.calcularConsumo(costoE, cantE)
                if consumoE < minE:
                    minE = consumoE
                    auxE = calefactor
        print('el menor de gas es ', str(auxG), 'con un consumo de', minG)
        print('el menor de electrico es ', str(auxE), 'con un consumo de', minE)

    def calularTodos (self, costoG, cantG, costoE, cantE):
        minG = 999999999999
        minE = 999999999999
        auxG = 0
        auxE = 0
        for calefactor in self.__arreglo:
            if isinstance(calefactor, Gas):
                consumoG = calefactor.calcularConsumo(costoG, cantG)
                if consumoG < minG:
                    minG = consumoG
                    auxG = calefactor

            elif isinstance(calefactor, Electrico):
                consumoE = calefactor.calcularConsumo(costoE, cantE)
                if consumoE < minE:
                    minE = consumoE
                    auxE = calefactor

        if minG < minE:
            print('el menor de todos es a gas ', str(auxG), 'con un consumo de', minG)
        else:
            print('el menor de todos es electrico', str(auxE), 'con un consumo de', minE)
        #hacer lo mismo que con la funcion de arriba y comparar los minimos de gas y electrico al final
                

