# Variables necesarias para calcular los promedios
suma_pares = 0
suma_impares = 0
pares = 0
impares = 0

valor = int(input('Ingrese valor 1: '))
if valor > 0:
    if valor % 2 == 0:
        suma_pares += valor
        pares += 1
    else:
        suma_impares += valor
        impares += 1
    valor = int(input('Ingrese valor 2: '))
    if valor > 0:
        if valor % 2 == 0:
            suma_pares += valor
            pares += 1
        else:
            suma_impares += valor
            impares += 1
        valor = int(input('Ingrese valor 3: '))
        if valor > 0:
            if valor % 2 == 0:
                suma_pares += valor
                pares += 1
            else:
                suma_impares += valor
                impares += 1
            valor = int(input('Ingrese valor 4: '))
            if valor > 0:
                if valor % 2 == 0:
                    suma_pares += valor
                    pares += 1
                else:
                    suma_impares += valor
                    impares += 1
                valor = int(input('Ingrese valor 5: '))
                if valor > 0:
                    if valor % 2 == 0:
                        suma_pares += valor
                        pares += 1
                    else:
                        suma_impares += valor
                        impares += 1
                    if pares != 0:
                        print('Promedio pares:', suma_pares / pares)
                    else:
                        print('El promedio de pares es 0')
                    if impares != 0:
                        print('Promedio impares:', suma_impares / impares)
                    else:
                        print('El promedio de impares es 0')