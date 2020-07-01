# Utilizaremos constantes para definir los múltiplos

MULTIPLO_1 = 3
MULTIPLO_2 = 8

numeros = [2,4,8,10,1,2,24,64,20,123,3]

for numero in numeros:
    # Verifiquemos que el número sea múltiplo de MUL1 y MUL2 al mismo tiempo (es por eso el uso del and)
    if numero % MULTIPLO_1 == 0 and numero % MULTIPLO_2 == 0:
        print('El número %d es múltiplo de %d y %d a la vez' %(numero, MULTIPLO_1, MULTIPLO_2))
    else:
        print('El número %d no es múltiplo de %d y %d a la vez' %(numero, MULTIPLO_1, MULTIPLO_2))

