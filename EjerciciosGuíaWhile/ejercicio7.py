# Ejercicio 7 según enunciado

FIN = 0
#AGENDA
NUM_RODRIGO = 9977
NUM_JUAN = 8877
NUM_ROBERTO = 7755
NUM_KARYN = 1122
NUM_SOLANGE = 2233

num_celular = int(input('Ingrese número de celular [%d para finalizar]: ' %FIN))

while num_celular != FIN:

    # Verificar si el número ingresado corresponde a alguno de la agenda
    if num_celular == NUM_RODRIGO:
        print('El número ingresado corresponde al número de celular de Rodrigo')
    elif num_celular == NUM_JUAN:
        print('El número ingresado corresponde al número de celular de Juan')
    elif num_celular == NUM_ROBERTO:
        print('El número ingresado corresponde al número de celular de Roberto')
    elif num_celular == NUM_KARYN:
        print('El número ingresado corresponde al número de celular de Karyn')
    elif num_celular == NUM_SOLANGE:
        print('El número ingresado corresponde al número de celular de Solange')
    else:
        print('Número ingresado desconocido')

    # Solicitar nuevamente el número de celular
    num_celular = int(input('Ingrese número de celular [%d para finalizar]: ' %FIN))

