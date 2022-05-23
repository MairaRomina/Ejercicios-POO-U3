from claseRamo import Ramo

class ManejadorR:
    __lista = [] #si solo incializo la lista aca se vuelve variable de clase

    def __init__ (self):
        self.__lista = [] #tengo que colocar esto para evitar eso

    def __str__ (self):
        s = ""
        for ramo in self.__lista:
            s += str( ramo ) + '\n'
        return s
    
    def registraVenta (self, cant, manFlor):
        if cant == 1:
            unRamo = Ramo('Chico')
        elif cant == 4:
            unRamo = Ramo('Mediano')
        elif cant == 6: 
            unRamo = Ramo('Grande')
        
        for i in range( manFlor.getCantidad() ):
            objeto = manFlor.getObjeto(i)
            print(objeto.getId(), '*', objeto.getNombre(), '*', objeto.getColor())

        while cant > 0:
            num = int(input('Ingrese el numero de flor: '))
            """ flor = manFlor.getObjeto( num - 1 ) """
            flor = manFlor.buscaFlor( num )
            unRamo.agregaFlor( flor ) 
            cant -= 1
        self.__lista.append( unRamo )
    
    def listar (self, manFlor):
        lista = [ 0 for i in range( 10 )]
        for i in range( len( self.__lista ) ):
            listaRamo = self.__lista[i].getListaRamo()
        

