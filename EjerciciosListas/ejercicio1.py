# Reservar asiento de una sala de cine
# Para reservar, indicar el nombre de la persona y su asiento en la sala


# Los asientos de una sala está determinado por un aforo de N
# Los asientos están enumerados de 1 a N
# Presentar un menú de opciones
# [1] Reservar asientos
# [2] Mostrar asientos ocupados
# [3] Mostrar asientos desocupados
# [4] Finalizar


# Si el asiento ya está ocupado, enviar mensaje pidiendo que ingrese otro asiento
# Si la sala está llena, mandar un mensaje de "sala llena"

sala_cine = []

NOMBRE = 0
NRO_ASIENTO = 1
AFORO_SALA_CINE = 10
INICIO_ASIENTO = 1
FIN = 4
LIM_INF_OPC = 1
LIM_SUP_OPC = 3


def reservar_asiento():
    
    asiento = ingresarAsiento()
    
    if asiento != -1:
        nombre_persona = input('Ingrese nombre de la persona: ')
        sala_cine.append([nombre_persona, asiento])
        print('Reserva de asiento exitosa!!!')

def ordenarListaPorAsientos(asiento):
    return asiento[NRO_ASIENTO]

def imprimirAsientos():
    sala_cine.sort(key = ordenarListaPorAsientos, reverse=True)
    print('Asientos de la sala de cine ocupados')
    for asiento in sala_cine:
        print(asiento[NOMBRE], asiento[NRO_ASIENTO])

def asientoOcupado(asiento_persona):
    for asiento in sala_cine:
        if asiento[NRO_ASIENTO] == asiento_persona:
            return True
    return False

def ingresarAsiento():
    fin = -1
    
    asiento = int(input(f'Ingrese asiento de la persona {INICIO_ASIENTO}-{AFORO_SALA_CINE} {fin} para volver al menú: '))
    
    if asiento != -1:
        while asientoOcupado(asiento):
            print('Error, el asiento ya ha sido ocupado, favor ingresar otro')
            asiento = int(input(f'Ingrese asiento de la persona {INICIO_ASIENTO}-{AFORO_SALA_CINE} {fin} para volver al menú: '))
        
        while asiento != FIN and (asiento < INICIO_ASIENTO or asiento > AFORO_SALA_CINE):
            print('Error, asiento ingresado no válido')
            asiento = int(input(f'Ingrese asiento de la persona {INICIO_ASIENTO}-{AFORO_SALA_CINE} {fin} para volver al menú: '))
            while asientoOcupado(asiento):
                print('Error, el asiento ya ha sido ocupado, favor ingresar otro')
                asiento = int(input(f'Ingrese asiento de la persona {INICIO_ASIENTO}-{AFORO_SALA_CINE} {fin} para volver al menú: '))
            
    return asiento

def mostrarAsientosOcupados():
    print('Asientos ocupados: ')
    for asiento in sala_cine:
        print(asiento[NRO_ASIENTO])


def mostrarAsientosDesocupados():
    print('Asientos desocupados')
    
    asientos_ocupados = []
    
    for asiento in sala_cine:
        asientos_ocupados.append(asiento[NRO_ASIENTO])
    
    for i in range(1, AFORO_SALA_CINE+1):
        if not (i in asientos_ocupados):
            print(i)
            

def menu_opciones():
    opcion = int(input('[1]Reservar asiento\n[2]Mostrar asientos ocupados\n[3]Mostar asientos desocupados\n[4]Salir\n-->:'))
    
    while opcion != FIN and (opcion < LIM_INF_OPC or opcion > LIM_SUP_OPC):
        print('Error, opción no válida')
        opcion = int(input('[1]Reservar asiento\n[2]Mostrar asientos ocupados\n[3]Mostar asientos desocupados\n[4]Salir\n-->:'))
    return opcion


# Ciclo principal

opcion = menu_opciones()

while opcion != FIN:
    
    if opcion == 1:
        reservar_asiento()
    elif opcion == 2:
        mostrarAsientosOcupados()
    elif opcion == 3:
        mostrarAsientosDesocupados()
    
    opcion = menu_opciones()

imprimirAsientos()