
lista = {}

while True:

    alimento = str(input('Introduzce el alimento que ha consumido en el día: '))
    cantidad = int(input('Introduzce que cantidad que ha consumido del alimento(en gramos): '))
    fin = int(input('¿Quiere registrar otro alimento(Si[1]/No[0]): '))
    lista[alimento] = cantidad
    if fin == 1:
        alimento = input('Introduzce el alimento que ha consumido en el día: ')
        cantidad = int(input('Introduzce que cantidad que ha consumido del alimento(en gramos): '))
        fin = int(input('¿Quiere registrar otro alimento(Si[1]/No[0]): '))
        lista[alimento] = cantidad

    elif fin == 0:
        for i in lista:
            print('Resumen del comsumo diario: ','\n', alimento[0],': ', cantidad, 'gramo/s.', )
        break

        
    

  
