import numpy as np
import csv
from datetime import date, timedelta
from claseContrato import Contrato

class ManContrato:
    __cantidad = 0
    __dimension = 4
    __incremento = 8

    def __init__ (self):
        self.__arreglo = np.empty(self.__dimension, dtype = Contrato)
        self.__cantidad = 0
        self.__dimension = 4
        self.__incremento = 8

    def __str__ (self):
        s = ""
        for contrato in self.__arreglo:
            s += str( contrato ) + '\n'
        return s

    def agrega (self, unContrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[ self.__cantidad ] = unContrato
        self.__cantidad += 1

    def test (self, manE, manJ):
        contrato1 = Contrato( date(2022, 5, 27), date(2023, 5, 27), 30000000, manE.getObjeto( 0 ), manJ.getObjeto( 0 ) ) 
        contrato2 = Contrato( date.today(), date(2022, 11, 28), 30000000, manE.getObjeto( 0 ), manJ.getObjeto( 1 ) )
        contrato3 = Contrato( date(2022, 5, 29), date(2023, 5, 29), 30000000, manE.getObjeto( 1 ), manJ.getObjeto( 2 ) )
        contrato4 = Contrato( date(2022, 5, 30), date(2023, 5, 30), 30000000, manE.getObjeto( 1 ), manJ.getObjeto( 3 ) )
        self.agrega( contrato1 ) ; self.agrega( contrato2 ) ; self.agrega( contrato3 ) ; self.agrega( contrato4 )

    def mostrarContrato (self, dni):
        for contrato in self.__arreglo:
            if contrato.getJugador().getDni() == dni:
                print('*************')
                print('Jugador:',contrato.getJugador().getNombre())
                print('Nombre del equipo: ',contrato.getEquipo().getNombre())
                print('Fecha de finalizacion: ',contrato.getFinal())

    def consultar (self, nom):
        i = 0
        while i < self.__cantidad:
            if nom == self.__arreglo[i].getEquipo().getNombre():
                #print(self.__arreglo[i].getEquipo().getNombre())
                hoy = date.today()
                fecha = self.__arreglo[i].getFinal() - hoy 
                #print(hoy)
                #print(fecha)
                #6 meses son 180 dias
                calculo = fecha // timedelta(days = 30)
                #print(calculo)
                if calculo == 6:
                    print(self.__arreglo[i].getJugador())
            i += 1

    def calcular (self, nom):
        i = 0
        while i < self.__cantidad:
            if nom == self.__arreglo[i].getEquipo().getNombre():
                #print(self.__arreglo[i].getEquipo().getNombre())
                hoy = date.today()
                fecha = self.__arreglo[i].getFinal() - self.__arreglo[i].getInicio() 
                #print(hoy)
                #print(fecha)
                calculo = fecha // timedelta(days=30)
                #print(calculo)
                importe = calculo * self.__arreglo[i].getPago()
                print(self.__arreglo[i].getJugador().getNombre())
                print(importe)
            i += 1

    """ def cargarCsv (self):
        for i in range(self.__cantidad):
            with open('Contratos.csv', 'w', newline = '') as csvfile:
                #fieldnames = ['DNI del jugador', 'Nombre del equipo', 'fecha de inicio', 'fecha de fin', 'pago mensual']
                writer = csv.writer(csvfile, dialect = 'excel')
                
                #writer.writeheader()
                writer.writerows(self.__arreglo[i]) """
#contrato.getJugador().getDni(), contrato.getEquipo().getNombre(), contrato.getInicio(), contrato.getFinal(), contrato.getPago()

    def cargarCsv (self):
        myFile = open('Contratos.csv', 'w', newline = '')
        writer = csv.writer(myFile, dialect = 'excel', delimiter = ';')
        for contrato in self.__arreglo:
            writer.writerow({contrato.getJugador().getDni():1, contrato.getEquipo().getNombre():2, contrato.getInicio():3, contrato.getFinal():4, contrato.getPago():5})