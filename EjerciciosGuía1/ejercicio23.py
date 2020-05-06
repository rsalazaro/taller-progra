#Escribir un algoritmo que solicite las dimensiones de un baño rectangular (largo, ancho y alto) y calcule en metros cuadrados la cantidad de cerámica que se deben colocar en todas las paredes del baño.

#Entradas

largo = float(input('Ingrese largo: '))
ancho = float(input('Ingrese ancho: '))
alto = float(input('Ingrese alto: '))

#Proceso
#Baño rectangular --> cubrir una superficie --> área --> área de un rectángulo --> base*altura
#2 tipos de paredes --> largo*alto y ancho*alto

cantidad_ceramica = 2*largo*alto + 2*ancho*alto

#Salidas

print('La cantidad necesaria de cerámica es de', cantidad_ceramica, 'm2')