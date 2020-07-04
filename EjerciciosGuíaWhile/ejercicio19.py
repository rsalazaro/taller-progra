# Ubicación de ciudades (n° de kilómetro en la que se encuentra)

KMARICA = 0
KMIQUIQUE = 400
KMANTOFAGASTA = 730
KMCALAMA = 600
KMTOCOPILLA = 540

ARICA = 0
IQUIQUE = 1
ANTOFAGASTA = 2
CALAMA = 3
TOCOPILLA = 4


print('Arica[%d] Iquique[%d] Antofagasta[%d] Calama[%d] Tocopilla[%d]' %(ARICA, IQUIQUE, ANTOFAGASTA, CALAMA, TOCOPILLA))
origen = int(input('Ingrese ciudad de origen: '))
while origen != ARICA and origen != IQUIQUE and origen != ANTOFAGASTA and origen != CALAMA and origen != TOCOPILLA:
    print('Error, Origen nó válido')
    origen = int(input('Ingrese ciudad de origen: '))
destino = int(input('Ingrese ciudad de destino: '))
while destino != ARICA and destino != IQUIQUE and destino != ANTOFAGASTA and destino != CALAMA and destino != TOCOPILLA:
    print('Error, Destino nó válido')
    destino = int(input('Ingrese ciudad de destino: '))

while origen != destino:

    # Calculamos la distancia 
    distancia = 0
    if origen == ARICA:
        if destino == IQUIQUE:
            distancia = KMIQUIQUE
        elif destino == ANTOFAGASTA:
            distancia = KMANTOFAGASTA
        elif destino == CALAMA:
            distancia = KMCALAMA
        else:
            distancia = KMTOCOPILLA
    elif origen == IQUIQUE:
        if destino == ARICA:
            distancia = abs(KMIQUIQUE-KMARICA)
        elif destino == ANTOFAGASTA:
            distancia = abs(KMIQUIQUE-KMANTOFAGASTA)
        elif destino == CALAMA:
            distancia = abs(KMIQUIQUE-KMCALAMA)
        else:
            distancia = abs(KMIQUIQUE-KMTOCOPILLA)
    elif origen == ANTOFAGASTA:
        if destino == ARICA:
            distancia = abs(KMANTOFAGASTA-KMARICA)
        elif destino == IQUIQUE:
            distancia = abs(KMIQUIQUE-KMANTOFAGASTA)
        elif destino == CALAMA:
            distancia = abs(KMANTOFAGASTA-KMCALAMA)
        else:
            distancia = abs(KMANTOFAGASTA-KMTOCOPILLA)
    elif origen == CALAMA:
        if destino == ARICA:
            distancia = abs(KMCALAMA-KMARICA)
        elif destino == ANTOFAGASTA:
            distancia = abs(KMCALAMA-KMANTOFAGASTA)
        elif destino == IQUIQUE:
            distancia = abs(KMIQUIQUE-KMCALAMA)
        else:
            distancia = abs(KMCALAMA-KMTOCOPILLA)
    else:
        if destino == ARICA:
            distancia = abs(KMTOCOPILLA-KMARICA)
        elif destino == ANTOFAGASTA:
            distancia = abs(KMTOCOPILLA-KMANTOFAGASTA)
        elif destino == CALAMA:
            distancia = abs(KMTOCOPILLA-KMCALAMA)
        else:
            distancia = abs(KMIQUIQUE-KMTOCOPILLA)
    print('La distancia entre',origen,'y',destino,'es',distancia)

    # Solicitamos ingresar el origen y el destino nuevamente

    origen = int(input('Ingrese ciudad de origen: '))
    while origen != ARICA and origen != IQUIQUE and origen != ANTOFAGASTA and origen != CALAMA and origen != TOCOPILLA:
        print('Error, Origen nó válido')
        origen = int(input('Ingrese ciudad de origen: '))
    destino = int(input('Ingrese ciudad de destino: '))
    while destino != ARICA and destino != IQUIQUE and destino != ANTOFAGASTA and destino != CALAMA and destino != TOCOPILLA:
        print('Error, Destino nó válido')
        destino = int(input('Ingrese ciudad de destino: '))
