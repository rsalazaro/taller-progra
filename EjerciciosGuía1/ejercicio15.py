#Escriba un algoritmo que solicite una temperatura en grados Fahrenheit y calcule el valor correspondiente a grados Celsius, utilizando la fórmula: C/5 = (F – 32)/9.

# Entradas

fahrenheit = float(input('Ingrese grados Celsius: '))

# Proceso
# C/5 = (F – 32)/9
# Despejar C --> C = (F - 32)/9 * 5
celsius = (fahrenheit - 32)/9 * 5

# Salidas

print(str(fahrenheit)+'°F','son '+str(celsius)+' °C')