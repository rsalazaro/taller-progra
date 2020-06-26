FIN = 0
numero = int(input('Ingrese un número [%d para finalizar]: ' %FIN))

while numero != FIN:
    # Verificar si el número es par o impar
    if numero % 2 == 0:
        print('Es Par')
    else:
        print('Es Impar')
    # Solicitar nuevamente el número
    numero = int(input('Ingrese un número [%d para finalizar]: ' %FIN))

print('Lo siento, aún no se ponen de acuerdo')