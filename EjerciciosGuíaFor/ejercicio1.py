# Se tiene una lista con N elementos

numeros = [1,2,3,5,2,1,2,20,10,2]

# Recuerden que esto se lee, por cada _ en la lista _
# En este sentido, el primero _ es elemento y el segundo _ es la lista numeros

for elemento in numeros:
    # Verificar si el número es par
    if elemento % 2 == 0:
        print('El número', elemento,'es par')
    else:
        print('El número', elemento,'es impar')

# TIP: normalmente, se utilza un plural para las listas, y en el for se utiliza el singular
# Por ejemplo, el siguiente código se leería: Por cada número en la lista números, lo cual suena mejor que el caso anterior
''' 
for numero in numeros:
    Hacer algo 
'''
