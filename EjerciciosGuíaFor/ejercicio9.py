ARICA = 0
IQUIQUE = 1
ANTOFAGASTA = 2
CALAMA = 3
TOCOPILLA = 4

# Distancias de una ciudad a la otra en orden 
distanciasA = [0,309,720,600,535]
distanciasI = [309,0,420,380,230]
distanciasA = [720,420,0,220,190]
distanciasC = [600,380,220,0,160]
distanciasT = [532,230,190,160,0]
ciudades = ['Arica', 'Iquique', 'Antofagasta', 'Calama', 'Tocopilla']

print('[0]Arica\n[1]Iquique\n[2]Antofagasta\n[3]Calama\n[4]Tocopilla')

# Solicitar origen
origen = int(input('Ingrese la ciudad de origen: '))
# Validar ciudad de origen
while origen < ARICA or origen > TOCOPILLA:
    print('Error, ciudad de origen no válida')
    origen = int(input('Ingrese la ciudad de origen: '))
# Solicitar destino
destino = int(input('Ingrese la ciudad de destino [%d para finalizar]: ' %origen))
# Validar destino
while destino < ARICA or destino > TOCOPILLA:
    print('Error, ciudad de desntino no válida')
    destino = int(input('Ingrese la ciudad de destino [%d para finalizar]: ' %origen))

while origen != destino:

    # Para el calculo de las distancias, ocuparemos el "destino" como índice
    if origen == ARICA:
        distancia = distanciasA[destino]
    elif origen == IQUIQUE:
        distancia = distanciasI[destino]
    elif origen == ANTOFAGASTA:
        distancia = distanciasA[destino]
    elif origen == CALAMA:
        distancia = distanciasC[destino]
    else:
        distancia = distanciasT[destino]

    print('La distancia entre %s y %s es %d' %(ciudades[origen], ciudades[destino], distancia))

    # Volver a solicitar los datos

    # Solicitar origen
    origen = int(input('Ingrese la ciudad de origen: '))
    # Validar ciudad de origen
    while origen < ARICA or origen > TOCOPILLA:
        print('Error, ciudad de origen no válida')
        origen = int(input('Ingrese la ciudad de origen: '))
    # Solicitar destino
    destino = int(input('Ingrese la ciudad de destino [%d para finalizar]: ' %origen))
    # Validar destino
    while destino < ARICA or destino > TOCOPILLA:
        print('Error, ciudad de desntino no válida')
        destino = int(input('Ingrese la ciudad de destino [%d para finalizar]: ' %origen))







