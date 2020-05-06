#Escribir un algoritmo que solicite la cantidad de votos nulos, blancos y válidos de un proceso eleccionario y entregue los porcentajes obtenidos según los tipos de voto.

#Entradas
vNulo = int(input('Ingrese voto nulo: '))
vBlanco = int(input('Ingrese voto blanco: '))
vValido = int(input('Ingrese voto válido: '))

#Proceso

#10 nulos   --> 10/60 --> 0.17 * 100 --> 17%
#20 blancos --> 20/60 --> 0.33 * 100 --> 33.3%
#30 validos --> 30/60 --> 0.5 * 100 --> 50%
#total = 60

total_votos = vNulo + vBlanco + vValido

porcentaje_nulos = (vNulo / total_votos) * 100
porcentaje_blancos = (vBlanco / total_votos) * 100
porcentaje_validos = (vValido / total_votos) * 100

#Salidas

print('votos nulos: {0:.2f}%\nvotos blancos: {1:.2f}%\nvotos válidos {2:.2f}%'
      .format(porcentaje_nulos, porcentaje_blancos, porcentaje_validos))