a = int(input('Ingrese valor a: '))
b = int(input('Ingrese valor b: '))
c = int(input('Ingrese valor c: '))

# verificar el orden del intervalo
if a < b:
    # Caso que el intervalo sea [a:b] --> a cota inferior, b cota superior
    if c >= a and c <= b:
        print(c,'está en el intervalo {0}:{1}'.format(a,b))
    else:
        print(c,'no está en el intervalo {0}:{1}'.format(a,b))
else:
    # Caso que el intervalo sea [b:a] --> b cota inferior, a cota superior
    if c >= b and c <= a:
        print(c,'está en el intervalo {0}:{1}'.format(b,a))
    else:
        print(c,'no está en el intervalo {0}:{1}'.format(b,a))
