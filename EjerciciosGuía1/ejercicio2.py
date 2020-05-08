#Escribir un algoritmo que solicite tres números y calcule las medias aritmética y geométrica

# Entradas

numero1 = float(input('Ingrese número 1: '))
numero2 = float(input('Ingrese número 2: '))
numero3 = float(input('Ingrese número 3: '))

# Proceso

promedio = (numero1 + numero2 + numero3)/3
media_geometrica = (numero1*numero2*numero3)**(1/3)

# Salida

print('El promedio es',promedio)
print('La media geométrica es',media_geometrica)
