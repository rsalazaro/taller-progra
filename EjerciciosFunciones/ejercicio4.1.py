""" 
    Crear una función que retorne el mayor valor de una lista de datos
    La función debe recibir como parámetro la lista de datos
    La función debe retornar el valor mayor 
"""

def valorMayor(lista_datos):
    mayor = lista_datos[0] # Inicializamos el valor mayor con el primer valor de la lista
        
    for i in range(1,len(lista_datos)): # Como ya "visitamos" el primer valor de la lista, comenzamos desde el siguiente valor
        if lista_datos[i] > mayor:
            mayor = lista_datos[i]
    
    return mayor
        
lista = [-1, -5, -3, -88, -2, 0]

print('El valor mayor es', valorMayor(lista))

# ¿Qué ocurre si le pasamos una "lista vacía" como parámetro a la función?