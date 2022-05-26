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
            unRamo = Ramo('chico')
        elif cant == 4:
            unRamo = Ramo('mediano')
        elif cant == 6: 
            unRamo = Ramo('grande')
        
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
    
    """ def listar (self, manFlor):
        lista = [ 0 for i in range( 10 )]
        for i in range( len( self.__lista ) ):
            listaRamo = self.__lista[i].getListaRamo() """

    def masPedidas(self, mf):
        listaR = [ 0 for i in range( 10 )]
        for ramo in self.__lista:
            listaFlores = ramo.getListaRamo()
            for flor in listaFlores:
                n = int(flor.getNumero())
                listaR[n - 1] += 1
        i = 0
        while max(listaR) != 0 and i < 5:
            m = listaR.index(max(listaR))
            listaR[m] = 0
            flor = mf.buscaFlor(m + 1)
            print(flor.getNombre())
            i += 1

    def masVendidas(self, t):
        for ramo in self.__lista:
            if ramo.getTamaño() == t:
                listaFlores = ramo.getListaRamo()
                for flor in listaFlores:
                    nombre = flor.getNombre()
                    print(nombre)
        

