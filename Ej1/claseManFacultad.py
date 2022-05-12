import csv
from claseCarrera import Carrera
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

    # def test (self):
    #     archivo = open( 'Facultades.csv')
    #     reader = csv.reader( archivo, delimiter = ';' )
    #     bandera = True
    #     for fila in reader:
    #         if bandera:
    #             facu = fila
    #             bandera = not bandera
    #             listaCarrera = []
    #         else:
    #             if fila[0] == facu[0]: #corte de control por el id de facultad
    #                 listaCarrera.append( fila ) #agrega una carrera a la lista de carreras que esta adentro del objeto facultad
    #             else:
    #                 unaFacultad = Facultad( facu[0], facu[1], facu[2], facu[3], facu[4], listaCarrera ) #creo la facultad con la lista de carreras, pero solo son filas sin especificar nada de clase carrera
    #                 self.agregar( unaFacultad )
    #                 facu = fila
    #                 listaCarrera = []
    #     archivo.close()
    
    def test (self):
        archivo = open( 'Facultades.csv', encoding = 'utf-8' )
        reader = csv.reader( archivo, delimiter = ';' )
        fila = next( reader )
        bandera = True
        #print( 'Facultad' )
        while bandera:
            #print( fila ) 
            unaFacultad = Facultad( int(fila[0]), fila[1], fila[2], fila[3], fila[4] )
            self.agregar( unaFacultad )
            #print( 'Carreras:' )
            filaCarrera = next( reader )
            while bandera and fila[0] == filaCarrera[0]:
                #print( filaCarrera )
                try:
                    unaCarrera = Carrera( int(filaCarrera[0]), int(filaCarrera[1]), filaCarrera[2], filaCarrera[3], filaCarrera[4], filaCarrera[5] )
                    unaFacultad.agregarCarrera( unaCarrera )
                    filaCarrera = next( reader )
                except StopIteration:
                    bandera = False
            fila = filaCarrera
        archivo.close()
        
    def mostrar (self, ide):
        if self.__lista[ide - 1].getIdF() == ide:
            print(self.__lista[ide - 1].getNombreF())
            for carrera in self.__lista[ide - 1].getLista():
                print( '{:50} {}'.format( carrera.getNombre(), carrera.getDuracion() ) )
                
    def listarCarreras (self, nom):
        i = 0
        bandera = True
        while bandera and i < len( self.__lista ):
            for carrera in self.__lista[i].getLista():
                if carrera.getNombre() == nom:
                    bandera = False
                    print('Facultad: {} Localidad: {}'.format( self.__lista[i].getNombreF(), self.__lista[i].getLocalidad() ))
                    print('Codigo: {},{}'.format( self.__lista[i].getIdF(), carrera.getCodigoCarrera() ))
            i += 1
