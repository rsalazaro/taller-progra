#Escribir un algoritmo que solicite la edad de una persona en años y calcule la cantidad de segundos que ha vivido.

# Entradas

edad = int(input('Ingrese la edad de la persona: '))

# Proceso
# 1 min --> 60 seg
# 1 hora --> 60 min
# 1 dia --> 24 horas
# 1 año --> 365 dias

segundos = 60*60*24*365*edad

# Salidas

print('La persona ha vivido ',segundos, 'segundos')