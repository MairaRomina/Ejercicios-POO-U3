from zope.interface import Interface


class IAparato(Interface):

    def agregarAparato(Auto):
        pass

    def insertarAparato(Auto, pos):
        pass

    def MostrarAparato(indice):
        pass