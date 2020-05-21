# Entradas

valor1 = int(input('Ingrese valor 1: '))
mayor = menor = valor1
pos_mayor = pos_menor = 1
# Proceso 
valor2 = int(input('Ingrese valor 2: '))
if valor2 > mayor:
    mayor = valor2
    pos_mayor = 2
elif valor2 < menor:
    menor = valor2
    pos_menor = 2
valor3 = int(input('Ingrese valor 3: '))
if valor3 > mayor:
    mayor = valor3
    pos_mayor = 3
elif valor3 < menor:
    menor = valor3
    pos_menor = 3
valor4 = int(input('Ingrese valor 4: '))
if valor4 > mayor:
    mayor = valor4
    pos_menor = 4
elif valor4 < menor:
    menor = valor4
    pos_menor = 4
valor5 = int(input('Ingrese valor 5: '))
if valor5 > mayor:
    mayor = valor5
    pos_mayor = 5
elif valor5 < menor:
    menor = valor5
    pos_menor = 5

# Salidas

print('El mayor es {0} y se ingresó en la posición {1}\nEl menor es {2} y se ingresó en la posición {3}'.format(mayor, pos_mayor, menor, pos_menor))