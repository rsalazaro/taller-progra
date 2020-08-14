# Listas

# Sirve para almacenar elementos de forma ordenada

# Los elementos están separados por , --> lista = [1,2,3] : lista de 3 elementos
# El primer elemento de la lista está en la posición 0
# El último elemento en la lista está en la posición N-1, donde N es el largo de la lista

# Ejemplo: lista_elementos = ['rodrigo', 24, True, [1, False], 6.1]
    # Esta lista contiene 5 elementos
        # El primer elemento: lista_elemetos[0]     = 'rodrigo', es del tipo "str"
        # El segundo elemento: lista_elemetos[1]    = 24, es del tipo "int"
        # El tercer elemento: lista_elementos[2]    = True, es del tipo "boolean"
        # El cuarto elemento: lista_elementos[3]    = [1, False], es del tipo "list", y tiene 2 elementos 1 y False
        # El quinto elemento: lista_elementos[4] o lista_elementos[-1] = 6.1 y es del tipo "float"

# Utilidad
# La función len(lista) retorna el largo de la lista (cantidad de objetos de la lista)
# La función sum(lista) retorna la sumatoria de los elementos de la lista (deben ser números)


# Orden
# La función lista.sort() permite ordenar los elementos de una lista
    # Por defecto, lista.sort() ordena de forma ascendente: 1, 2, 3, 4 ....
    # Para ordenar de forma inversa, aplicar lista.sort(reverse = True): ... 4, 3, 2, 1
    # Para ordenar por otro factor, utilziar lista.sort(key = factor), donde factor es una función

# Búsqueda
# La función lista.count(x) retorna la cantidad de elementos "x" que existen en la lista
    # En el caso de no existir x, retorna 0
    # [1,2,3,1].count(1)  --> retorna 2
# La función lista.index(x), retorna la posición en que se encuentra el elemento "x" en la lista
    # En el caso de no existir x, aparece un error
    # Retorna siempre la primera coincidencia
    # [1,2,3,1].index(2) --> retorna 1

# Eliminar elementos
# La función lista.remove(x), remueve el primer valor = "x" en la lista. Recuerden que solo elimina el primer valor
# La función lista.pop(), remueve el último valor de la lista y además, retorna ese valor
# La función lista.pop(x), remueve el valor en la posición x de la lista y además, retorna ese valor
# La función del lista[x], remueve el valor de la posición x de la lista

# Añadir elementos
# La función lista.append(x), añade un elemento x al final de la lista
# La función lista.insert(i,x), añade un elemento x en la posición i de la lista
# La función lista.extend(lista2), permite añadir todos los elementos de la lista2 a la lista1

# Algoritmos útiles sobre listas

# (1) Buscar el índice de un elemento en la lista
# Descripción: Retorna el indice de un elemento "x" en la lista. Si no lo encuentra, retorna -1
# def buscarPosicionElemento(lista, elemento):
#     indice = -1
#     for i in range(len(lista)):
#         if lista[i] == elemento:
#             indice = i
#             break
#     return indice

# (2) Eliminar un elmento
# Descripción: Elimina un elemento x en la lista y retorna un mensaje
# def eliminarElemento(lista, elemento):
#     indice = buscarPosicionElemento(lista, elemento)

#     # Si encontró el elemento en la lista, indice tiene un valor != 1
#     if indice != -1:
#         elementoEliminado = lista.pop(indice)
#         return f'Se ha eliminado el elemento {elementoEliminado} de la lista'

#     return f'Elemento {elemento} no encontrado en la lista'

# (3) Editar un elemento
# Descripción, permite editar el valor de un elemento
# def editarElemento(lista, antiguoElemento, nuevoElemento):
#     indice = buscarPosicionElemento(lista, antiguoElemento)

#     if indice != -1:
#         lista[indice] = nuevoElemento
#         return f'Se ha actualizado {antiguoElemento} por {nuevoElemento}'
    
#     return f'No se ha encontrado el elemento {antiguoElemento}'