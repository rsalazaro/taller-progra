#Escriba un algoritmo que dado dos números enteros, los almacene en dos variables y luego intercambie el contenido de esas variables mostrando sus valores intercambiados.

# Entradas

numero1 = int(input('Ingrese número 1: '))
numero2 = int(input('Ingrese número 2: '))

# Proceso

temporal = numero1
numero1 = numero2
numero2 = temporal

# Salidas

print(numero1, numero2)