from claseCarrera import Carrera

class Facultad:
    __codigo: str
    __nombre: str
    __direccion: str
    __localidad: str
    __telefono: str
    __carreras = None #composicion 

    def __init__ (self, cod, nom, dire, lo, tel, lista):
        self.__codigo = cod
        self.__nombre = nom
        self.__direccion = dire
        self.__localidad = lo
        self.__telefono = tel
        #atributos de la clase carrera
        codigo = Carrera.getCodigo()
        nombre = Carrera.getNombre()
        duracion = Carrera.getDuracion()
        titulo = Carrera.getTitulo()
        tipo = Carrera.getTipo()
        self.__carreras = Carrera( codigo, nombre, duracion, titulo, tipo ) #creo el objeto carrera dentro del objeto facultad
    
    def __str__ (self):
        cadena ='{} Facultad: \n'.format( self.__codigo ) 
        cadena += 'Nombre: {} Direccion: {} Localidad: {} Telefono: {}'.format( self.__nombre, self.__direccion, self.__localidad, self.__telefono )
        cadena += str( self.__carreras ) 
        return cadena 
        
         
    
