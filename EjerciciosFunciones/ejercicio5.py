""" 
    Crear una función que retorne el menor valor de una lista de datos
    La función debe recibir como parámetro la lista de datos
    La función debe retornar el valor menor 
"""

def valorMenor(lista_datos):
    menor = lista_datos[0] # Inicializamos el valor menor con el primer valor de la lista
        
    for i in range(1,len(lista_datos)): # Como ya "visitamos" el primer valor de la lista, comenzamos desde el siguiente valor
        if lista_datos[i] < menor:
            menor = lista_datos[i]
    
    return menor

# Programa principal

lista = [1,2,3,-1,3,-2,2] # El valor menor es -2

print('El valor menor es', valorMenor(lista))
