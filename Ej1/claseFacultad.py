from claseCarrera import Carrera

class Facultad:
    __codigo: str
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    __carreras = [] #composicion 

    def __init__ (self, cod, nom, dire, lo, tel):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dire
        self.__localidad = lo
        self.__telefono = tel
        #atributos de la clase carrera
        self.__carreras = []
    
    def __str__(self):
        cadena = '\n{:3} {:5} {:50} {:40} {:20} \n'.format( self.__codigo, self.__nombre, self.__direccion, self.__localidad, self.__telefono )
        for carrera in self.__carreras:
            cadena += str( carrera )
        return cadena
    
    # def agregarCarrera( self, cod, nom, dur, titu, tipo):
    #     unaCarrera = Carrera( cod, nom, dur, titu, tipo )
    #     self.__carreras.append( unaCarrera )
    
    def agregarCarrera( self, unaCarrera ):
        self.__carreras.append( unaCarrera )
        
    def getIdF (self):
        return self.__codigo
    
    def getNombreF (self):
        return self.__nombre
    
    def getLista (self):
        return self.__carreras
    
    def getLocalidad (self):
        return self.__localidad
         
    

