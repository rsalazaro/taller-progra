""" 
    Crear una función que retorne el mayor valor de una lista de datos
    Está garantizado que la lista de datos contiene números mayores a 0
    La función debe recibir como parámetro la lista de datos
    La función debe retornar el valor mayor 
"""

def valorMayor(lista_datos):
    mayor = 0 # Recordemos que para buscar un mayor, deberemos crear una variable "mayor" que se inicialice con el "menor valor posible"

    for dato in lista_datos:
        if dato > mayor:
            mayor = dato
    
    return mayor

# Programa principal 

lista = [2,1,2,7,9,10,1,4,33,12,8] # En este ejemplo, el valor mayor es 33

print('El valor mayor es', valorMayor(lista))

# En la variante 4.1, realizaremos el mismo ejercicio pero considerando que la lista contiene números negativos


