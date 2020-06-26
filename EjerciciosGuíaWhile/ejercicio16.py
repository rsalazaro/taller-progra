FIN = 7
LIM_INF = 1
LIM_SUP = 6

SIMPLE = 5000
SIMPLE_SUPERIOR = 5500
MATRIMONIAL = 7000
MATRIMONIAL_SUPERIOR = 7500
DOBLE = 8000
DOBLE_SUPERIOR = 8500

#1) Ingreso de datos
opcion_menu = int(input('Ingrese un número del menú de opciones[%d para finalizar]: ' %FIN))
#2) Validación de datos
while opcion_menu != FIN and (opcion_menu < LIM_INF or opcion_menu > LIM_SUP):
    print('Error, el número ingresado no se encuentra en el rango [%d a %d]' %(LIM_INF, LIM_SUP))
    numero = int(input('Ingrese un número del menú de opciones[%d para finalizar]: ' %FIN))

#3) Realizar el ciclo

while opcion_menu != FIN:
    
    #4) Programar la lógica del enunciado

    # Solicitar el número de noches
    
    num_noches = int(input('Ingrese cantidad de noches que se quedará la persona: '))
    while num_noches <= 0:
        print('Error, no puede ingresar un número de noches menores a 0')
        num_noches = int(input('Ingrese cantidad de noches que se quedará la persona: '))
        
    if opcion_menu == 1:
        precio_pagar = SIMPLE*num_noches*1.19
    elif opcion_menu == 2:
        precio_pagar = SIMPLE_SUPERIOR*num_noches*1.19
    elif opcion_menu == 3:
        precio_pagar = MATRIMONIAL*num_noches*1.19
    elif opcion_menu == 4:
        precio_pagar = MATRIMONIAL_SUPERIOR*num_noches*1.19
    elif opcion_menu == 5:
        precio_pagar = DOBLE*num_noches*1.19
    else:
        precio_pagar = DOBLE_SUPERIOR*num_noches*1.19
        
    print('El precio total a pagar es de', round(precio_pagar))
    
    #5) Volver a pedir el ingreso de los datos
    opcion_menu = int(input('Ingrese un número del menú de opciones[%d para finalizar]: ' %FIN))
    #2) Validación de datos
    while opcion_menu != FIN and (opcion_menu < LIM_INF or opcion_menu > LIM_SUP):
        print('Error, el número ingresado no se encuentra en el rango [%d a %d]' %(LIM_INF, LIM_SUP))
        numero = int(input('Ingrese un número del menú de opciones[%d para finalizar]: ' %FIN))