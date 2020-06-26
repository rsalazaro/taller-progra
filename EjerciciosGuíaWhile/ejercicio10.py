FIN = 0
LIM_INF = 1
LIM_SUP = 10

numero = int(input('Ingrese un número entre 1 y 10 [%d para finalizar]: ' %FIN))

# Verificar que el número ingresado esté dentro del rango 1 y 10 y además, que no sea 0

while numero != FIN and (numero < LIM_INF or numero > LIM_SUP):
    print('Error, debe ingresar un número entre %d y %d' %(LIM_INF,LIM_SUP))
    numero = int(input('Ingrese un número entre %d y %d [%d para finalizar]: ' %(LIM_INF, LIM_SUP, FIN)))

# Se realiza el ciclo para que se siga imprimiendo la tabla hasta que el usuario termine
while numero != FIN :

    # Se imprime tabla según enunciado

    print('X\tX^2\tX^3\tX^4\tX^5')
    while numero > 0:
        print(numero,'\t',numero**2,'\t',numero**3,'\t',numero**4,'\t',numero**5)
        numero = numero - 1
        
    # Solicitamos nuevamente el número

    numero = int(input('Ingrese un número entre 1 y 10 [%d para finalizar]: ' %FIN))
    # Verificamos nuevamente que el número este dentro del rango permitod [1 y 1']
    while numero != FIN and (numero < LIM_INF or numero > LIM_SUP):
        print('Error, debe ingresar un número entre %d y %d' %(LIM_INF, LIM_SUP))
        numero = int(input('Ingrese un número entre %d y %d [%d para finalizar]: ' %(LIM_INF, LIM_SUP, FIN)))
