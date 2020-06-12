numero = abs(int(input('Ingrese un número de 4 dígitos: ')))

#Validar que el número no tenga más de 4 dígitos
if numero < 9999:
    uni = numero % 10
    dec = (numero // 10) % 10
    cen = (numero // 100) % 10
    mil = (numero // 1000) % 10

    # Todos los números de 1 dígito son palíndromos
    if numero>=0 and numero<10:
        print('El número es palíndromo')
    # Verificar si un número de 2 dígitos es palíndromo
    elif numero > 9 and numero < 100:
        if uni == dec:
            print('El número es palíndromo')
        else:
            print('El número no es palíndromo')
    # Verificar si un número de 3 dígitos es palíndromo
    elif numero > 99 and numero < 1000:
        if uni == cen:
            print('El número es palíndromo')
        else:
            print('El número no es palíndromo')

    # Verificar si un número de 4 dígitos es palíndromo
    else:
        if uni == mil and dec == cen:
            print('El número es palíndromo')
        else:
            print('El número no es palíndromo')
else:
    print('Número no válido')