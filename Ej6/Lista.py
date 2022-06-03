from zope.interface import implementer

from ClaseNodo import Nodo
from IAparato import IAparato
from ClaseTelevisor import Televisor
from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa


@implementer(IAparato)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__ (self):
        self.__comienzo = None
        self.__actual = None

    def __iter__ (self):
        return self

    def __next__ (self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def agregarAparato (self, artefacto):
        nodo = Nodo(artefacto)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarAparato (self, unArtefacto, indice):
        aux = self.__comienzo
        bandera = False
        c = 0
        if indice <= self.__tope:
            if c == indice:
                if self.__comienzo is None:
                    nuevoNodo = Nodo( unArtefacto )
                    nuevoNodo.setSiguiente( self.__comienzo )
                    self.__actual = nuevoNodo
                    self.__tope += 1
                else:
                    nuevoNodo = Nodo( unArtefacto )
                    nuevoNodo.setSiguiente( self.__comienzo )
                    aux.setSiguiente( aux.getSiguiente() )
                    self.__comienzo = nuevoNodo
                    self.__actual = nuevoNodo
                    self.__tope += 1
            else:
                ant = aux
                while aux is not None and bandera is False:
                    if c == indice:
                        bandera = True
                    else:
                        c += 1
                        ant = aux
                        aux = aux.getSiguiente()
                if c == indice:
                    nuevoNodo = Nodo( unArtefacto )
                    ant.setSiguiente( nuevoNodo )
                    nuevoNodo.setSiguiente( aux )
                    self.__tope += 1
        else:
            raise Exception('El índice no es válido')
        
    def insertarPila (self, unArtefacto):
        nodo = Nodo( unArtefacto ) 
        nodo.setSiguiente( self.__comienzo )
        self.__comienzo = nodo 

    def MostrarAparato (self, indice): #le agregue self, esta mal si lo en la interface no lo agrega ? 
        aux = self.__comienzo 
        bandera = True 
        i = 0
        while aux != None and bandera:
            if i == indice:
                bandera = not bandera
            else:
                i += 1
                aux = aux.getSiguiente()
        if i == indice:
            if isinstance( aux.getDato(), Televisor ):
                print('------------------- OBJETO ENCONTRADO -------------------')
                print('El objeto almacenado en esa posicion es de tipo Televisor')
                print(aux.getDato())
            elif isinstance( aux.getDato(), Heladera ):
                print('------------------- OBJETO ENCONTRADO -------------------')
                print('El objeto almacenado en esa posicion es de tipo Heladera')
                print(aux.getDato())
            elif isinstance( aux.getDato(), Lavarropa ):
                print('------------------- OBJETO ENCONTRADO -------------------')
                print('El objeto almacenado en esa posicion es de tipo Lavarropa')
                print(aux.getDato())
        else:
            print('No se encontro ningun artefacto en dicha posicion')

    def buscarMarca (self): #inciso 4
        aux = self.__comienzo  
        contT = 0
        contH = 0
        contL = 0
        # print(aux.getDato().getMarca())
        while aux != None:
            if aux.getDato().getMarca() == 'Phillips':
                if isinstance( aux.getDato(), Televisor ):
                    contT += 1
                elif isinstance( aux.getDato(), Heladera ):
                    contH += 1
                elif isinstance( aux.getDato(), Lavarropa ):
                    contL += 1    
            aux = aux.getSiguiente()
        print('Cantidad por marca Phillips: Teles: {} Heladeras: {} Lavarropas: {}'.format( contT, contH, contL ))

    def  listar (self): 
        importe = 0
        aux = self.__comienzo  #inciso 6
        while aux != None:
            print('Marca ',aux.getDato().getMarca())
            print('Pais de fabricacion ',aux.getDato().getPais())
            importe = aux.getDato().calcularImporteTotal()
            print('Importe ', importe)
            #print(aux.getDato())
            aux = aux.getSiguiente()

    def buscaTipoLavarropa (self): #inciso 5
        aux = self.__comienzo 
        while aux != None:
            if isinstance( aux.getDato(), Lavarropa ):
                if aux.getDato().getTipo() == 'Superior':
                    print('Marca de lavarropas con carga Superiror: ')
                    print(aux.getDato().getMarca())
            aux = aux.getSiguiente()

    def mostrarTodaLista (self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux = aux.getSiguiente()

    def toJSON(self):
        return dict( __class__ = self.__class__.__name__, Nodos = [Lista.toJSON() for Lista in self] )
