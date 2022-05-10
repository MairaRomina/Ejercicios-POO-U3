import csv
from claseFacultad import Facultad

class Manejador:
    __lista = []

    def __init__ (self):
        self.__lista = []

    def __str__ (self):
        s = ""
        for facultad in self.__lista:
            s += str( facultad ) + '\n'
        return s
    
    def agregar (self, unaFacultad):
        self.__lista.append( unaFacultad ) #agrega un objeto facultad a la lista manejador

    def test (self):
        archivo = open( 'Facultades.csv')
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            if bandera:
                facu = fila
                bandera = not bandera
                listaCarrera = []
            else:
                if fila[0] == facu[0]: #corte de control por el id de facultad
                    listaCarrera.append( fila ) #agrega una carrera a la lista de carreras que esta adentro del objeto facultad
                else:
                    unaFacultad = Facultad( facu[0], facu[1], facu[2], facu[3], facu[4], listaCarrera ) #creo la facultad con la lista de carreras, pero solo son filas sin especificar nada de clase carrera
                    self.agregar( unaFacultad )
                    facu = fila
                    listaCarrera = []
        archivo.close()
