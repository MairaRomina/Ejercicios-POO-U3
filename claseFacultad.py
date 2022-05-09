from claseCarrera import Carrera

class Facultad:
    __codigo: int
    __nom: str
    __direccion: str
    __localidad: str
    __telefono: str
    __carreras = None

    def __init__ (self, cod, nom, dir, lo, tel):
        self.__codigo = cod
        self.__nom = nom
        self.__direccion = dir
        self.__localidad = lo
        self.__telefono = tel
        #atributos de la clase carrera
        codigo = Carrera.getCodigo()
        nombre = Carrera.getNombre()
        duracion = Carrera.getDuracion()
        titulo = Carrera.getTitulo()
        tipo = Carrera.getTipo()
        __carreras = Carrera( codigo, nombre, duracion, titulo, tipo )
    
    def __str__ (self):
        return ('Codigo: {} Nombre: {} Direccion: {} Localidad: {} Telefono: {}'.format( self.__codigo, self.__nom, self.__direccion, self.__localidad, self.__telefono ))
    
