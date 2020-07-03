FIN = 4

numeros_1 = [1,2,3,4,5,6,7,8,9]
numeros_2 = [9,8,7,6,5,4,3,2,1]

# Aprovecharemos el uso de las listas para imprimir las operaciones
operaciones = ['1: suma de listas', '2: resta de listas', '3: multiplicación de listas']

for operacion in operaciones:
    print(operacion)

# Solicitar datos

opcion_menu = int(input('Ingrese una opción del menú [%d para finalizar]: ' %FIN))

# Validemos la opción ingresada

while opcion_menu != FIN and (opcion_menu != 1 and opcion_menu != 2 and opcion_menu != 3):
    print('Error, operación ingresada no válida')
    opcion_menu = int(input('Ingrese una opción del menú: '))



while opcion_menu != FIN:
    # Consideremos que las operaciones suma, resta y multiplicación del listas se pueden realizar si ambas listas tienen el mismo tamaño
    if len(numeros_1) == len(numeros_2):
        # Tomaremos el tamaño de una de las listas para crear la lista resultante
        n = len(numeros_1)
        for i in range(n):
        # Según la opción del usuario, cambiaremos el operando según corresponda
            if opcion_menu == 1:
                print(numeros_1[i] + numeros_2[i], end=' ')
            elif opcion_menu == 2:
                print(numeros_1[i] - numeros_2[i], end=' ')
            else:
                print(numeros_1[i] * numeros_2[i], end=' ')
    else:
        print('No se pueden realizar las operaciones sobre listas de distinto tamaño')
    
    # Solicitaremos al usuario ingresar una operación nuevamente
 
    opcion_menu = int(input('\nIngrese una opción del menú [%d para finalizar]: ' %FIN))

    # Validemos la opción ingresada

    while opcion_menu != FIN and (opcion_menu != 1 and opcion_menu != 2 and opcion_menu != 3):
        print('Error, operación ingresada no válida')
        opcion_menu = int(input('Ingrese una opción del menú [%d para finalizar]: ' %FIN))
