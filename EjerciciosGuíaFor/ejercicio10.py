NOTA_APROBACION = 4

ruts = ['1111-1', '2222-2', '3333-3', '4444-4', '5555-5']

# Notas alumnos

alumno_1 = [3.1,4.1,5.7,2.5,5.5]
alumno_2 = [4.4,3.1,5.0,6.8,7.0]
alumno_3 = [1.0,2.0,3.0,4.0,5.0]
alumno_4 = [1.0,2.0,3.0,4.0,5.0]
alumno_5 = [5.5,4.5,7.0,3.3,4.9]

# Lista de promedios
promedios = []

# Variables necesarias para conocer el mayor promedio y quienes lo obtuvieron
mayor_promedio = 0 # ¿Puedes adivinar por qué se inicializa la variable en 0?
mayores_promedios = []

# Variables necesarias para conocer el menor promedio y quienes lo obtuvieron
menor_promedio = 8 # ¿Puedes adivinar por qué se inicializa la variable en 8?
menores_promedios = []

# Calculemos cada promedio utilizando sum() y len()

promedios.append(sum(alumno_1)/len(alumno_1))
promedios.append(sum(alumno_2)/len(alumno_2))
promedios.append(sum(alumno_3)/len(alumno_3))
promedios.append(sum(alumno_4)/len(alumno_4))
promedios.append(sum(alumno_5)/len(alumno_5))

# Recorramos la lista promedios para encontrar el mayor promedio y menor promedio y quienes lo obtuvieron

indice = 0
aprobados = 0
for promedio in promedios:

    # Búsqueda de los mayores y menores
    if promedio > mayor_promedio:
        mayores_promedios = []
        mayores_promedios.append(ruts[indice])
        mayor_promedio = promedio
    elif promedio == mayor_promedio:
        mayores_promedios.append(ruts[indice])
    else:
        if promedio < menor_promedio:
            menores_promedios = []
            menores_promedios.append(ruts[indice])
            menor_promedio = promedio
        elif promedio == menor_promedio:
            menores_promedios.append(ruts[indice])
    
    # Contamos cuantos aprobaron 
    if promedio >= NOTA_APROBACION:
        aprobados = aprobados + 1

    indice = indice + 1

print('Mayor promedio %f y lo obtuvieron %s' %(mayor_promedio, mayores_promedios))
print('Menor promedio %f y lo obtuvieron %s' %(menor_promedio, menores_promedios))
print('Aprobados %d\nReprobados %d' %(aprobados, len(ruts)-aprobados))

# Desafio, en vez de usar una lista por cada alumno, utilice una lista notas alumnos que contendrá las 5 notas de cada alumno, es decir, una lista de listas
# Ejemplo
# notas_alumnos = [[notas_alumno1],[notas_alumno2],[],[]...[notas_alumnoN]]

