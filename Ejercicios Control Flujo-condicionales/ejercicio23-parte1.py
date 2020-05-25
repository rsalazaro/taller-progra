# Salida --> El equipo que pasa a la siguiente ronda e indicar motivo,
# 1) paso por mayor puntaje
# 2) paso por mayor cantidad de goles realizados
# 3) pasó por mayor cantidad de goles de visita
# 4) pasó por sorteo

# Grupo AAA

# Equipo A
# Equipo B
# Equipo C

# Partido 1: Equipo A vs Equipo B
# goles_a_local y goles_b_vista
# quien gano, quien perdio, si hubo empate
# puntuacion_equipo_a = 3 si ganó, 0 si perdió y 1 si empato
# goles > goles_otro : 3 , 0, 1
# Partido 2: Equipo B vs Equipo C
# goles_b_lcoal y goles_equipo_v
# Partido 3: Equipo C vd Equipo A

print('Ingrese los resultados del partido 1: Equipo A vs Equipo B')
goles_equipo_a_local = int(input('Ingrese los goles del equipo A: '))
goles_equipo_b_visita = int(input('Ingrese los goles del equipo B: '))

puntos_equipo_a = 0
puntos_equipo_b = 0
puntos_equipo_c = 0

goles_equipo_a = 0
goles_equipo_b = 0
goles_equipo_c = 0

if goles_equipo_a_local > goles_equipo_b_visita:
    puntos_equipo_a = 3
elif goles_equipo_a_local < goles_equipo_b_visita:
    puntos_equipo_b = 3
else:
    puntos_equipo_a = 1
    puntos_equipo_b = 1


# Partido 2: Equipo B vs Equipo C

print('Ingrese los resultados del partido 2: Equipo B vs Equipo C')
goles_equipo_b_local = int(input('Ingrese los goles del equipo B: '))
goles_equipo_c_visita = int(input('Ingrese los goles del equipo C: '))

if goles_equipo_b_local > goles_equipo_c_visita:
    puntos_equipo_b += 3
elif goles_equipo_b_local < goles_equipo_c_visita:
    puntos_equipo_c = 3
else:
    puntos_equipo_b += 1
    puntos_equipo_c += 1


# Partido 3: Equipo C vs Equipo A

print('Ingrese los resultados del partido 3: Equipo C vs Equipo A')
goles_equipo_c_local = int(input('Ingrese los goles del equipo C: '))
goles_equipo_a_visita = int(input('Ingrese los goles del equipo A: '))

if goles_equipo_c_local > goles_equipo_a_visita:
    puntos_equipo_c += 3
elif goles_equipo_c_local < goles_equipo_a_visita:
    puntos_equipo_a += 3
else:
    puntos_equipo_c += 1
    puntos_equipo_a += 1

print('Tabla de puntuación fecha 2')
print('Equipo A ',puntos_equipo_a,'puntos')
print('Equipo B ',puntos_equipo_b,'puntos')
print('Equipo C ',puntos_equipo_c,'puntos')


# Según la FIFA, pasa a la siguiente ronda el equipo con mayor cantidad de puntaje

cantidad_equipos_mayorp = 0
mayor_puntaje = puntos_equipo_a

# Calcular el mayor puntaje

if puntos_equipo_b > mayor_puntaje:
    if puntos_equipo_b > puntos_equipo_c:
        mayor_puntaje = puntos_equipo_b
    else:
        mayor_puntaje = puntos_equipo_c
else:
    if puntos_equipo_c > puntos_equipo_a:
        mayor_puntaje = puntos_equipo_c
        
# Calcular la cantidad de equipos que logran el mayor puntaje

if mayor_puntaje == puntos_equipo_a:
    cantidad_equipos_mayorp += 1
if mayor_puntaje == puntos_equipo_b:
    cantidad_equipos_mayorp += 1
if mayor_puntaje == puntos_equipo_c:
    cantidad_equipos_mayorp += 1
    
print('Cantidad de equipos que alcanzaron la puntuación',mayor_puntaje,'son: ',cantidad_equipos_mayorp)

if cantidad_equipos_mayorp == 1:
    # Aplicar FIFA 1
    if mayor_puntaje == puntos_equipo_a:
        print('El equipo A pasó a la siguiente ronda por mayoría de puntos')
    elif mayor_puntaje == puntos_equipo_b:
        print('El equipo B pasó a la siguiente ronda por mayoría de puntos')
    else:
        print('El equipo C pasó a la siguiente ronda por mayoría de puntos')

elif cantidad_equipos_mayorp == 2:
    # ¿Qué se hace si hay 2 equipos con el mayor puntaje?
    # No sabemos cuales son los equipos que alcanzaron el mayor puntaje
    # Buscar estos equipos
    
    equipo_mayor1 = ''
    equipo_mayor2 = ''
    
    goles_equipo_mayor1 = 0
    goles_equipo_mayor2 = 0
    
    goles_visita_equipo_mayor1 = 0
    goles_visita_equipo_mayor2 = 0
    
    # Buscar los equipos
    
    if mayor_puntaje == puntos_equipo_a:
        equipo_mayor1 = 'Equipo A'
        goles_equipo_mayor1 = goles_equipo_a_local + goles_equipo_a_visita
        goles_visita_equipo_mayor1 = goles_equipo_a_visita
    if mayor_puntaje == puntos_equipo_b:
        if equipo_mayor1 == '':
            equipo_mayor1 = 'Equipo B'
            goles_equipo_mayor1 = goles_equipo_b_local + goles_equipo_b_visita
            goles_visita_equipo_mayor1 = goles_equipo_b_visita
        else:
            equipo_mayor2 = 'Equipo B'
            goles_equipo_mayor2 = goles_equipo_b_local + goles_equipo_b_visita
            goles_visita_equipo_mayor = goles_equipo_b_visita
    if mayor_puntaje == puntos_equipo_c:
        equipo_mayor2 = 'Equipo C'
        goles_equipo_mayor2 = goles_equipo_c_local + goles_equipo_c_visita
        goles_visita_equipo_mayor = goles_equipo_c_visita
    
    print('Equipo mayor 1', equipo_mayor1, 'goles equipo mayor 1', goles_equipo_mayor1)
    print('Equipo mayor 2', equipo_mayor2, 'goles equipo mayor 2', goles_equipo_mayor2)
    
    # Aplicar FIFA 2