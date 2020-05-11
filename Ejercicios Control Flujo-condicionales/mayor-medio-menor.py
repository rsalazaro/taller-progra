# Dado 3 números, imprimir el mayor, el de al medio y el menor

# Entradas

a = int(input('Ingrese número 1: '))
b = int(input('Ingrese número 2: '))
c = int(input('Ingrese número 3: '))

# Análisis 
#abc --> a:mayor, b:medio, c:menor
#acb --> a:mayor, c:medio, b:menor
#bac
#bca
#cab
#cba --> c:mayor, b:medio, a:menor

# Proceso / Salidas
if a>=b and b>=c:
    print('Mayor: {0}\nMedio: {1}\nMenor: {2}'.format(a,b,c))
elif a>=b and c>=b:
    print('Mayor: {0}\nMedio: {1}\nMenor: {2}'.format(a,c,b))
elif b>=a and a>=c:
    print('Mayor: {0}\nMedio: {1}\nMenor: {2}'.format(b,a,c))
elif b>=c and c>=a:
    print('Mayor: {0}\nMedio: {1}\nMenor: {2}'.format(b,c,a))
elif c>=a and a>=b:
    print('Mayor: {0}\nMedio: {1}\nMenor: {2}'.format(c,a,b))
else:
    print('Mayor: {0}\nMedio: {1}\nMenor: {2}'.format(c,b,a))

