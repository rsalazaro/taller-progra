x1 = int(input('Ingrese punto x1: '))
x2 = int(input('Ingrese punto x2: '))
y1 = int(input('Ingrese punto y1: '))
y2 = int(input('Ingrese punto y2: '))
z1 = int(input('Ingrese punto z1: '))
z2 = int(input('Ingrese punto z2: '))

# Según el enunciado, la distancia se calcula como valor mayor - valor menor, por lo tanto
# primero tenemos que conocer cual de los dos valores es el mayor
# Luego, aplicaremos lo aprendido, comparando si la distancia del siguiente par de valores es mayor
# a la mayor registrada

if x1 > x2:
    mayor_distancia = x1 - x2
else:
    mayor_distancia = x2 - x1

if y1 > y2:
    if y1 - y2 > mayor_distancia:
        mayor_distancia = y1 - y2
else:
    if y2 - y1 > mayor_distancia:
        mayor_distancia = y2 - y1

if z1 > z2:
    if z1 - z2 > mayor_distancia:
        mayor_distancia = z1 - z2
else:
    if z2 - z1 > mayor_distancia:
        mayor_distancia = z2 - z1

print('La mayor distancia es', mayor_distancia)
