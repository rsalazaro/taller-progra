numero = int(input('Ingrese un número positivo de 4 dígitos: '))

if numero > 0:
    if numero < 10000:
        suma_digitos = numero % 10
        # Recuerden que //= es lo mismo que numero = numero //
        numero //= 10
        suma_digitos += numero % 10
        numero //= 10
        suma_digitos += numero % 10 + numero//10
        
        if suma_digitos % 2 == 0:
            print('La suma de los dígitos del número es par')
        else:
            print('La suma de los dígitos del número es impar')
    else:
        print('El número tienes más de 4 digitos')
else:
    print('El número es negativo')