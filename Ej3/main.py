from claseManEquipo import ManEquipo
from claseManContrato import ManContrato
from claseManJugador import ManJugador

if __name__ == '__main__':
    arreglo = ManEquipo() #punto 1
    lista = ManJugador()
    arreglo.test()
    lista.test()
    # print( arreglo )
    # print( lista )

    contrato = ManContrato()
    contrato.test( arreglo, lista ) #punto 2
    print( contrato )

    """ print('************* Jugadores contratados *************')
    dni = input('Ingrese el DNI: ')
    contrato.mostrarContrato( dni ) """

    """ print('************* contratos que vencen en 6 meses *************')
    nom = input('Ingrese el nombre del equipo: ')
    contrato.consultar( nom )

    print('************* Importe total por contrato *************')
    nom = input('Ingrese el nombre del equipo: ')
    contrato.calcular( nom ) """

    contrato.cargarCsv()

