FIN = 0
LIM_INF = 1
LIM_SUP = 1000

# Reglas
# Números a la IZQ restan, Números a la DER suman
# Los números V, L y D no pueden restar
# Solo pueden haber 3 números romanos consecutivos


numero = int(input('Ingrese un número entre %d y %d [%d para finalizar]: ' %(LIM_INF, LIM_SUP, FIN)))
while numero != FIN and (numero < LIM_INF or numero > LIM_SUP):
    print('Error, el número ingresado no está en el rango [%d a %d]' %(LIM_INF, LIM_SUP))
    numero = int(input('Ingrese un número entre %d y %d [%d para finalizar]: ' %(LIM_INF, LIM_SUP, FIN)))

while numero != FIN:

    # Transformar el número decimal a romano
    numeroRomano = ''

    # Se crea un número auxiliar para no perder el número al momento de imprimir
    numeroAux = numero

    UNO = 'I'
    CINCO = 'V'
    DIEZ = 'X'

    # El contandor lo utilizamos para realizar el cambio de unidades a decenas y centenas en romano
    cont = 0
    while cont < 3:
        digito = numeroAux % 10
        print(numeroRomano)
        # Implementamos el patrón de formación de números romanos
        if digito < 4:
            numeroRomano = UNO*digito + numeroRomano
        elif digito == 4:
            numeroRomano = UNO+CINCO + numeroRomano # Aquí el error, puse el operador += en vez de =
        elif digito == 5:
            numeroRomano = CINCO + numeroRomano
        elif digito > 5 and digito < 9:
            numeroRomano = CINCO+UNO*(digito-5) + numeroRomano
        elif digito == 9:
            numeroRomano = UNO+DIEZ + numeroRomano
        
        # Cambiamos el valor de unidad a decena
        # Transformaremos I en X, V en L y X en C
        if cont == 0:
            UNO = 'X'
            CINCO = 'L'
            DIEZ = 'C'
        # Cambiamos el valor de decena a centena
        # Transformaremos X en C, L en D, C en M
        else:
            UNO = 'C'
            CINCO = 'D'
            DIEZ = 'M'

        numeroAux = numeroAux // 10
        cont += 1

    # Imprimir el número
    print('El número',numero, 'en romano es',numeroRomano)

    numero = int(input('Ingrese un número entre %d y %d [%d para finalizar]: ' %(LIM_INF, LIM_SUP, FIN)))
    while numero != FIN and (numero < LIM_INF or numero > LIM_SUP):
        print('Error, el número ingresado no está en el rango [%d a %d]' %(LIM_INF, LIM_SUP))
        numero = int(input('Ingrese un número entre %d y %d [%d para finalizar]: ' %(LIM_INF, LIM_SUP, FIN)))
    