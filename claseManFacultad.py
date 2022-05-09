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
        self.__lista.append( unaFacultad )

    def test (self):
        archivo = open( 'facultad.csv' )
        reader = csv.reader( archivo, delimiter = ';' )
        bandera = True
        for fila in reader:
            cod = int(fila[0])
            if bandera:
                bandera = not bandera
            elif len( cod ) == 1:
                nom = fila[1]
                dir = fila[2]
                lo = fila[3]
                tel = fila[4]
                unaFacultad = Facultad( cod, nom, dir, lo, tel )
                self.agregar( unaFacultad )
        archivo.close()

        reader = csv.reader()
        bandera = True
        for fila in reader:
            if bandera:
                facu = fila
                bandera = not bandera
                listaCarrera = []
            else:
                if fila[0] == facu[0]:
                    listaCarrera.append( fila )
                else:
                    nuevaFacultad( facu[0], facu[1], facu[2]..., listaCarrera )
                    self.__lista.append( nuevaFacultad )
                    facu = fila
                    listaCarrera = []