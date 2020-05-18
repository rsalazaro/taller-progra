# Entradas

numero = int(input('Ingrese un número: '))
# Proceso 
# Un número es par si es divisible por 2 

# Salidas

# Recordar que 0 es considerado un número par, sin embargo
# hay que respetar el enunciado
if numero == 0:
    print('Lo siento aún no se ponen de acuerdo.')
elif numero%2 == 0:
    print('El número es par')
else:
    print('El número es impar')