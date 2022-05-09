class Carrera:
    __codigo: int
    __nombre: str
    __duracion: str
    __titulo: str
    __tipo: str

    def __init__ (self, cod, nom, dur, tit, tipo):
        self.__codigo = cod
        self.__nombre = nom
        self.__duracion = dur
        self.__titulo = tit
        self.__tipo = tipo

    def __str__ (self):
        return ('Codigo: {} Nombre: {} Duracion: {} Titulo: {} Tipo: {}'.format( self.__codigo, self.__nombre, self.__duracion, self.__titulo, self.__tipo ))

    def getCodigo (self):
        return self.__codigo

    def getNombre (self):
        return self.__nombre
    
    def getDuracion (self):
        return self.__duracion

    def getTitulo (self):
        return self.__titulo

    def getTipo (self):
        return self.__tipo