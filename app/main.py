'''Crear un programa al cual se le ingrese una temperatura en farenheit y la transforme a Celcius
Ademas, que imprima lo siguiente: Si la temperatura transformada es mayor que 100, que esta caliente,
si es menor que 0, que esta frio
'''
op=0
val=0



while op==0:
    op = 0
    val = 0
    temperatura = input('Ingrese una temperatura: ')
    nueva=(int(temperatura)-32)/1.8

    if nueva > 100:
        print(str(temperatura)+'F equivalen a '+str(nueva)+'C')
        print('La temperatura es caliente')
    elif nueva <= 0:
        print(str(temperatura) + 'F equivalen a '+str(nueva)+'C')
        print('La temperatura es fria')
    else:
        print(str(temperatura) + 'F equivalen a ' + str(nueva) + 'C')
    print('La temperatura es normal')

    while val == 0:
        opVal = int(input('Presione 0 para salir, 1 para ingresar otra temperatura: \n'))
        val=1
        if opVal != 1 and opVal != 0:
            print('Ha ingresado una opcion invalida, por favor seleccione una opcion recomendada: \n')
            val =0
        elif opVal == 0:
            op = 1




