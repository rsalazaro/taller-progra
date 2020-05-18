# Entradas

valor1 = int(input('Ingrese valor 1: '))
mayor = menor = valor1

# Proceso 
valor2 = int(input('Ingrese valor 2: '))
if valor2 > mayor:
    mayor = valor2
elif valor2 < menor:
    menor = valor2
valor3 = int(input('Ingrese valor 3: '))
if valor3 > mayor:
    mayor = valor3
elif valor3 < menor:
    menor = valor3
valor4 = int(input('Ingrese valor 4: '))
if valor4 > mayor:
    mayor = valor4
elif valor4 < menor:
    menor = valor4
valor5 = int(input('Ingrese valor 5: '))
if valor5 > mayor:
    mayor = valor5
elif valor5 < menor:
    menor = valor5

# Salidas

print('El mayor es {0}\nEl menor es {1}'.format(mayor, menor))