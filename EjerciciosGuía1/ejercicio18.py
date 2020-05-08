#Escribir un algoritmo que calcule la(s) solución(es) de una ecuación de segundo grado dado los coeficientes a, b c. Sabiendo que:

# Entradas

a = float(input('Ingrese el coeficiente a: '))
b = float(input('Ingrese el coeficiente b: '))
c = float(input('Ingrese el coeficiente c: '))

# Proceso
# x^2 - 1 = 0
# (x + 1)(x - 1) = 0
# x1 = -1, x2 = 1
# x^2 + 1 = 0



x1 = (-b + (b**2 - 4*a*c)**(1/2))/2*a
x2 = (-b - (b**2 - 4*a*c)**(1/2))/2*a

# Salidas

print('Las solciones de la ecuación es', x1, x2)