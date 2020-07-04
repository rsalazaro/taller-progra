# Se tiene en listas el rut y las 5 notas obtenidas por cada alumno de programación básica. Construya un programa que calcule
# su promedio, lo almacene en una lista de promedios y recorra la lista de promedios indicando cuál fue el mejor promedio y
# quienes lo obtuvieron, cuál fue el peor promedio y quienes lo obtuvieron, cuántos alumnos reprobaron y cuántos alumnos aprobaron.

ruts = ['17.553.718-K', '8.678.665-9', '5.678.778-6', '14.445.677-7', '6.789.765-4', '3.456.654-3', '4.455.443-3']
notas = [[4.4, 5.4, 7, 3.4, 5.8], [2.4, 4, 6.1, 3, 5.2], [4.8, 5, 6.3, 3, 2.3], [4.4, 5, 6.2, 3, 4.3], [2.4, 4, 6.1, 3, 5.2], [4.4, 5, 6.2, 3, 4.3], [2.4, 4, 6.1, 3, 5.2]]
promedios = []

mejor_promedio = 0
peor_promedio = 7
aprobados = reprobados = 0

mejores = []
peores = []

for i in range(len(notas)):
    suma = 0
    for nota in notas[i]:
        suma = suma + nota
        
    promedio = round(suma / len(notas[i]), 2)
    
    if promedio >= 3.95:
        aprobados += 1
    else:
        reprobados += 1
    
    promedios.append(promedio)
    
for i in range(len(promedios)):
    if promedios[i] > mejor_promedio:
        mejor_promedio = promedios[i]
        mejores = []
        mejores.append(ruts[i])
    elif promedios[i] == mejor_promedio:
        mejores.append(ruts[i])
    
    if promedios[i] < peor_promedio:
        peor_promedio = promedios[i]
        peores = []
        peores.append(ruts[i])
    elif promedios[i] == peor_promedio:
        peores.append(ruts[i])

print('SALIDA DE INFORMACIÓN:\n')
print(f'~ El mejor promedio fue de {mejor_promedio}, y lo obtuvieron {mejores}.')
print(f'~ El peor promedio fue de {peor_promedio}, y lo obtuvieron {peores}.')
print(f'~ {aprobados} alumnos aprobaron y {reprobados} alumnos reprobaron.')
