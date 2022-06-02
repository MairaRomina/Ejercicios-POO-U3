from claseManCalefactor import ManCalefactor

if __name__ == '__main__':
    # diccionario = dict( {'marca': 'Soler y Palau', 'Modelo': 'TL-10N',
    #  'marca': 'Rowenta Instant Comfort Compact', 'modelo': 'SO2330F2',
    #  'marca': 'DeLonghi', 'Modelo': 'HSX4315E',
    #  'marca': 'RCA', 'Modelo': 'RC-H3'} )

    cantidad = int(input('Ingrese la cantidad de componentes del arreglo: '))
    arreglo = ManCalefactor( cantidad )
    arreglo.cargaCalefactor()
    #print(arreglo)

    costoG = int(input('Ingrese el costo por m3: '))
    cantG = int(input('Ingrese la cantidad que se estima consumir en m3: '))
    costoE = int(input('Ingrese el costo de el kilowatt/h: '))
    cantE = int(input('Ingrese la cantidad que se estima consumir por hora: '))
    # arreglo.cargar( costoG, cantG, costoE, cantE )
    arreglo.calcular( costoG, cantG, costoE, cantE )
    print('***************************************************************************')
    #print(arreglo)
    arreglo.calularTodos( costoG, cantG, costoE, cantE)