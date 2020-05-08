#Escriba un algoritmo que solicite las coordenadas de dos puntos cartesianos y calcule la distancia entre esos puntos, según la fórmula:

# Entradas

x1 = float(input('Ingrese coordenda x del punto 1: '))
y1 = float(input('Ingrese coordenda y del punto 1: '))
x2 = float(input('Ingrese coordenda x del punto 2: '))
y2 = float(input('Ingrese coordenda y del punto 2: '))

# Proceso

distancia = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

# Salidas

print('La distancia entre los dos puntos es', distancia)