#Escribir un algoritmo que solicite las medidas de los lados de un rectángulo y calcule su área, perímetro y el largo de su diagonal.

# Entradas

base = float(input('Ingrese base del rectángulo: '))
altura = float(input('Ingrese altura del rectángulo: '))

# Proceso

perimetro = 2*base + 2*altura
area = base*altura
diagonal = ((base)**2+(altura)**2)**(1/2)

# Salidas

print('Perímetro: {0}\nÁrea: {1}\nDiagonal: {2}'.format(perimetro, area, diagonal))