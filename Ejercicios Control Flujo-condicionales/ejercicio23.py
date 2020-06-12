import random
# 3 puntos al ganador
# 1 punto por empatar
# 0 puntos por perder

# Imaginemos el escenario:
# 3 equipos, A,B y C
# Cada equipo juega 1 partido de local y 1 de visita
# Partido 1: Equipo A vs Equipo B, en donde Equipo A juega de local y Equipo B de visita
# Partido 2: Equipo B vs Equipo C, en donde Equipo B juega de local y Equipo C de visita
# Partido 3: Equipo C vs Equipo A, en donde Equipo C juega de local y Equipo A de visita

# Para simplificar el ejercicio, dejaremos la validación de goles > 0 de lado

# Se declaran 3 variables para almacenar los puntos de cada equipo
puntos_equipo_a = 0
puntos_equipo_b = 0
puntos_equipo_c = 0

# Para mejor lectura, vamos a declarar 6 variables que contengan los goles de cada equipo 
# en calidad local y de visita

goles_equipo_a_local = 0
goles_equipo_a_visita = 0

goles_equipo_b_local = 0
goles_equipo_b_visita = 0

goles_equipo_c_local = 0
goles_equipo_c_visita = 0


# Ahora, solicitaremos los resultados en términos de goles de cada partido
print('Ingrese los resultados del partido 1: Equipo A vs Equipo B, con Equipo A de local')
goles_equipo_a_local = int(input('Ingrese los goles del Equipo A: '))
goles_equipo_b_visita = int(input('Ingrese los goles del Equipo B: '))

# Calculamos 
if goles_equipo_a_local > goles_equipo_b_visita:
    puntos_equipo_a = 3
elif goles_equipo_b_visita > goles_equipo_a_local:
    puntos_equipo_b = 3
else:
    puntos_equipo_a = 1
    puntos_equipo_b = 1

print('Ingrese los resultados del partido 2: Equipo B vs Equipo C, con Equipo B de local')
goles_equipo_b_local = int(input('Ingrese los goles del Equipo B: '))
goles_equipo_c_visita = int(input('Ingrese los goles del Equipo C: '))

if goles_equipo_b_local > goles_equipo_c_visita:
    puntos_equipo_b += 3
elif goles_equipo_c_visita > goles_equipo_b_local:
    puntos_equipo_c += 3
else:
    puntos_equipo_b += 1
    puntos_equipo_c += 1

print('Ingrese los resultados del partido 3: Equipo C vs Equipo A, con Equipo C de local')
goles_equipo_c_local = int(input('Ingrese los goles del Equipo C: '))
goles_equipo_a_visita = int(input('Ingrese los goles del Equipo A: '))

if goles_equipo_c_local > goles_equipo_a_visita:
    puntos_equipo_c += 3
elif goles_equipo_a_visita > goles_equipo_c_local:
    puntos_equipo_a += 3
else:
    puntos_equipo_c += 1
    puntos_equipo_a += 1

# Por enunciado, sabemos que el equipo con más puntos pasa a la siguiente ronda
# En caso de que sea un doble o triple empate, hay que aplicar las reglas
# Como esta parte es compleja, se separará el procedimiento en etapas

# Etapa 1: Encontar la mayor cantidad de puntos

mayor = puntos_equipo_a

if puntos_equipo_b > mayor:
    mayor = puntos_equipo_b
    if puntos_equipo_c > mayor:
        mayor = puntos_equipo_c
else:
    if puntos_equipo_c > mayor:
        mayor = puntos_equipo_c

# Etapa 2, verificar cuantos mayores existen
cantidad_mayores = 0
if mayor == puntos_equipo_a:
    cantidad_mayores += 1
if mayor == puntos_equipo_b:
    cantidad_mayores += 1
if mayor == puntos_equipo_c:
    cantidad_mayores += 1

# Imprimiremos la tabla final de resultados para verificar que los calculos estén correctos
goles_equipo_a = goles_equipo_a_local + goles_equipo_a_visita
goles_equipo_b = goles_equipo_b_local + goles_equipo_b_visita
goles_equipo_c = goles_equipo_c_local + goles_equipo_c_visita
print('Equipo A\tPuntos: {0}\tCantidad de goles realizados: {1}\tGoles visita: {2}'.format(puntos_equipo_a, goles_equipo_a, goles_equipo_a_visita))
print('Equipo B\tPuntos: {0}\tCantidad de goles realizados: {1}\tGoles visita: {2}'.format(puntos_equipo_b, goles_equipo_b, goles_equipo_b_visita))
print('Equipo C\tPuntos: {0}\tCantidad de goles realizados: {1}\tGoles visita: {2}'.format(puntos_equipo_c, goles_equipo_c, goles_equipo_c_visita))

# Etapa 3, si existe 1 mayor, indicar el equipo que ganó



if cantidad_mayores == 1:
    if mayor == puntos_equipo_a:
        print('El equipo A pasó a la siguiente ronda por mayoría de puntos, con', puntos_equipo_a,'puntos')
    elif mayor == puntos_equipo_b:
        print('El equipo B pasó a la siguiente ronda por mayoría de puntos, con', puntos_equipo_b,'puntos')
    else:
        print('El equipo C pasó a la siguiente ronda por mayoría de puntos, con', puntos_equipo_c,'puntos')
#Etapa 4, si existen 2 mayores, buscarlos y realizar el procedimiento FIFA para encontrar al que pasa
elif cantidad_mayores == 2:
    # Estas variables son necesarias para simplificar los cálculos
    

    equipo_mayor_1 = 0
    equipo_mayor_2 = 0
    goles_equipo_mayor_1 = 0
    goles_equipo_mayor_2 = 0
    goles_visita_equipo_mayor_1 = 0
    goles_visita_equipo_mayor_2 = 0

    # Aplicando la etapa 4
    if mayor == puntos_equipo_a:
        equipo_mayor_1 = 'Equipo A'
        goles_equipo_mayor_1 = goles_equipo_a
        goles_visita_equipo_mayor_1 = goles_equipo_a_visita
    if mayor == puntos_equipo_b:
        if equipo_mayor_1 == 0:
            equipo_mayor_1 = 'Equipo B'
            goles_equipo_mayor_1 = goles_equipo_b
            goles_visita_equipo_mayor_1 = goles_equipo_b_visita
        else:
            equipo_mayor_2 = 'Equipo B'
            goles_equipo_mayor_2 = goles_equipo_b
            goles_visita_equipo_mayor_2 = goles_equipo_b_visita
    if mayor == puntos_equipo_c:
        equipo_mayor_2 = 'Equipo C'
        goles_equipo_mayor_2 = goles_equipo_c
        goles_visita_equipo_mayor_2 = goles_equipo_c_visita

    # Etapa 5, ya teniendo los 2 equipos mayores, ver cual pasa aplicando el reglamento FIFA
    # Paso 1 FIFA: mator cantidad de goles
    if goles_equipo_mayor_1 > goles_equipo_mayor_2:
        print('El',equipo_mayor_1,'pasó a la siguiente ronda por mayor diferencia de goles:', goles_equipo_mayor_1,'vs', goles_equipo_mayor_2)
    elif goles_equipo_mayor_2 > goles_equipo_mayor_1:
        print('El',equipo_mayor_2,'pasó a la siguiente ronda por mayor diferencia de goles:', goles_equipo_mayor_2,'vs', goles_equipo_mayor_1)
    else:
        #Paso 2 FIFA: pasa el que tiene más goles de visita
        if goles_visita_equipo_mayor_1 > goles_visita_equipo_mayor_2:
            print('El',equipo_mayor_1,'pasó a la siguiente ronda por mayor cantidad de goles visita:', goles_visita_equipo_mayor_1,'vs', goles_visita_equipo_mayor_2)
        elif goles_visita_equipo_mayor_2 > goles_visita_equipo_mayor_1:
            print('El',equipo_mayor_2,'pasó a la siguiente ronda por mayor cantidad de goles visita:', goles_visita_equipo_mayor_2,'vs', goles_visita_equipo_mayor_1)
        else:
            #Paso 3 FIFA: Sorteo. Por simplicidad, imaginemos el lanzamiento de una moneda
            # 1 pasa el equipo A, 2 Pasa el equipo B
            moneda = random.randint(1,2)
            if moneda == 1:
                print('El',equipo_mayor_1,'pasó a la siguiente ronda por lanzamiento de moneda')
            else:
                print('El',equipo_mayor_2,'pasó a la siguiente ronda por lanzamiento de moneda')

else:
    # Como todos son igules, solo hay que aplicar el reglamente FIFA
    # Paso 1 FIFA: mayor cantidad de goles

    if goles_equipo_a > goles_equipo_b and goles_equipo_a > goles_equipo_c:
        print('El Equipo A pasa a la siguiente ronda por mayor cantidad de goles', goles_equipo_a, 'vs', goles_equipo_b,goles_equipo_c)
    elif goles_equipo_b > goles_equipo_a and goles_equipo_b > goles_equipo_c:
        print('El Equipo B pasa a la siguiente ronda por mayor cantidad de goles', goles_equipo_b, 'vs', goles_equipo_a,goles_equipo_c)
    elif goles_equipo_c > goles_equipo_a and goles_equipo_c > goles_equipo_b:
        print('El Equipo C pasa a la siguiente ronda por mayor cantidad de goles', goles_equipo_c, 'vs', goles_equipo_a,goles_equipo_b)
    else:
        # Paso 2 FIFA: mayor cantidad de goles visita
        if goles_equipo_a_visita > goles_equipo_b_visita and goles_equipo_a_visita > goles_equipo_c_visita:
            print('El Equipo A pasa a la siguiente ronda por mayor cantidad de goles', goles_equipo_a_visita, 'vs', goles_equipo_b_visita,goles_equipo_c_visita)
        elif goles_equipo_b_visita > goles_equipo_a_visita and goles_equipo_b_visita > goles_equipo_c_visita:
            print('El Equipo B pasa a la siguiente ronda por mayor cantidad de goles', goles_equipo_b_visita, 'vs', goles_equipo_a_visita,goles_equipo_c_visita)
        elif goles_equipo_c_visita > goles_equipo_a_visita and goles_equipo_c_visita > goles_equipo_b_visita:
            print('El Equipo C pasa a la siguiente ronda por mayor cantidad de goles', goles_equipo_c_visita, 'vs', goles_equipo_a_visita,goles_equipo_b_visita)
        else:
            # Paso 3 FIFA: Sorteo: Por simplicidad, tirar un dado de 6 caras, donde 1y2 gana A, 3y4 gana b, 5y6 gana c
            dado = random.randint(1,6)

            if dado == 1 or dado == 2:
                print('El Equipo A pasa a la siguiente ronda por lanzamiento de dado')
            elif dado == 3 or dado == 4:
                print('El Equipo B pasa a la siguiente ronda por lanzamiento de dado')
            else:
                print('El Equipo C pasa a la siguiente ronda por lanzamiento de dado')
