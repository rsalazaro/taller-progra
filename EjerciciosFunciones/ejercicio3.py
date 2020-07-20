""" Crear una funcion que calcule el promedio de los datos de una lista
La función debe recibir como parámetros una lista de datos
La funcion debe retornar el promedio """

# Dos formas de hacer este ejercicio 

def promedio_forma_1(lista_datos):
    suma_datos = 0 # Variable acumuladora de datos
    contador_datos = 0 # Variable contador de datos

    for dato in lista_datos:
        suma_datos = suma_datos + dato
        contador_datos = contador_datos + 1
    
    promedio = suma_datos / contador_datos

    return promedio

def promedio_forma_2(lista_datos):
    return (sum(lista_datos) / len(lista_datos))


# Programa principal 

lista = [1,2,3,4,5,6,7,8,9,10] # El primedio debería ser 5,5

print('Promedio utilizando la forma 1: ', promedio_forma_1(lista))
print('Promedio utilizando la forma 2: ', promedio_forma_2(lista))

