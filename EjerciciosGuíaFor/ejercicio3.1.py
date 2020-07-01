numeros = [2,4,8,10,1,2,24,64,20,123,3]

multiplo = int(input('Ingrese un número para buscar sus múltiplos en la lista números: '))

# Verifiquemos que el número ingresado no sea 0, para no tener problemas
# P1: ¿Puedes explicar por qué el 0 causa problemas?

while multiplo == 0:
    print('Error, no puede ingresar el número 0')
    multiplo = int(input('Ingrese un número para buscar sus múltiplos en la lista números: '))

for numero in numeros:
    # Verifiquemos que el número de la lista sea múltiplo del número ingresado por el usuario
    if numero % multiplo == 0:
        print('El número %d es múltiplo de %d' %(numero, multiplo) ) # Para imprimir dos variables, debemos ponerlas entre (), separadas por ,
    else:
        print('El número %d no es múltiplo de %d' %(numero, multiplo))


