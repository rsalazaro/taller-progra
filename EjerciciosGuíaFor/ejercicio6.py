FIN = 0

ruts = ['111-1', '222-2', '333-3', '444-4', '555-5']
celulares = [8888,7777,6666,5555,4444]

# Utilizaremos la lógica de los indices del ejercicio anterior parar realizar este ejercicio

#Pedir el número de celular
num_celular = int(input('Ingrese un número de celular [%d para finalizar]: ' %FIN))
#Validemos que el número de celular no sea negativo
while num_celular < 0:
    print('Error, número de celular ingreasdo no válido')
    num_celular = int(input('Ingrese un número de celular [%d para finalizar]: ' %FIN))

# Apliquemos lo aprendido en cuanto a while

while num_celular != FIN:
    # Definamos un contador que nos servirá para saber si recorrimos toda la lista y no encontramos el número ingresado
    cont_numeros = 0
    # Definamos un indice para acceder al elemento N de la lista ruts según la lista celulares
    indice = 0

    for celular in celulares:
        if num_celular == celular:
            print('El numero %d corresponde al compañero de rut %s' %(num_celular, ruts[indice]))
        else:
            # Si no lo encontró, incrementemos el contador en 1
            cont_numeros = cont_numeros + 1
        
        # Incrementemos en indice para acceder al siguiente elemento de la lista ruts
        indice = indice + 1
    
    # Si el contador de números es igual al largo de la lista, entonces no encontramos el número, por ende debemos imprimir número desconocido

    if cont_numeros == len(celulares):
        print('Número desconocido')
    
    # Volvamos a pedir el número y a validar el número ingresado
    
    num_celular = int(input('Ingrese un número de celular [%d para finalizar]: ' %FIN))
    #Validemos que el número de celular no sea negativo
    while num_celular < 0:
        print('Error, número de celular ingreasdo no válido')
        num_celular = int(input('Ingrese un número de celular [%d para finalizar]: ' %FIN))

