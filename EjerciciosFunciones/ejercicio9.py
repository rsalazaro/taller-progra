#Construya un programa que gestione la venta de productos de un almacén.
#El programa debe presentar un menú que permita:
#1) Ingresar un nuevo producto para vender (código producto, precio y cantidad),
#2) Eliminar un producto,
#3) Modificar la cantidad de un producto determinado,
#4) Modificar el precio de un producto determinado y
#5) Finalizar.
# Utilice 3 listas para almacenar el código, la cantidad y el precio del producto.

FIN = 5
LIM_INF = 1
LIM_SUP = 4

def menu():
    
    print('''
1) Ingresar un nuevo producto para vender (código producto, precio y cantidad),
2) Eliminar un producto,
3) Modificar la cantidad de un producto determinado,
4) Modificar el precio de un producto determinado y
5) Finalizar.
''')
    
    opcion = int(input('Ingrese una opción del menú: '))
    
    while opcion != FIN and (opcion < LIM_INF or opcion > LIM_SUP):
        print('Error, la opción ingresedad no es válida')
        opcion = int(input('Ingrese una opción del menú: '))
    
    return opcion

def ingresarProducto():
    codigo = int(input('Ingrese código del producto: '))
    
    if codigo in lista_codigos:
        print('Error, el código del producto ya está registrado')
    else:
        cantidad = int(input('Ingrese la cantidad del producto: '))
        while cantidad < 0:
            print('Error, no puede ingresar una cantidad menor a 0')
            cantidad = int(input('Ingrese la cantidad del producto: '))
            
        precio = int(input('Ingrese precio del producto: '))
        while precio < 0:
            print('Error, el precio no puede ser menor a 0')
            precio = int(input('Ingrese precio del producto: '))
        
        lista_codigos.append(codigo)
        lista_cantidades.append(cantidad)
        lista_precios.append(precio)
        
        print('Producto agregado con éxito')

def buscarCodProd(codigoProd):
    n = len(lista_codigos)
    indice = -1
    for i in range(n):
        if lista_codigos[i] == codigoProd:
            indice = i
            break
    return indice

def eliminarProducto(codigoProd):
    n = len(lista_codigos)
    indice = buscarCodProd(codigoProd)
    if indice != -1:
        for i in range(indice, n-1):
            lista_codigos[i] = lista_codigos[i+1]
            lista_cantidades[i] = lista_cantidades[i+1]
            lista_precios[i] = lista_precios[i+1]
        lista_codigos.pop()
        lista_cantidades.pop()
        lista_precios.pop()
    else:
        print('Código no encontrado')

def modificarCantidad(codigoProd, nuevaCantidad):
    indice = buscarCodProd(codigoProd)
    
    if indice != -1:
        lista_cantidades[indice] = nuevaCantidad
    else:
        print('Código no encontrado')

def modificarPrecio(codigoProd, nuevoPrecio):
    indice = buscarCodProd(codigoProd)
    
    if indice != -1:
        lista_precios[indice] = nuevoPrecio
    else:
        print('Código no encontrado')

def imprimirDatos():
    print('Productos')
    print('Códigos:',lista_codigos)
    print('Cantidades:',lista_cantidades)
    print('Precios:',lista_precios)
    
# Programa principal

lista_codigos = [1]
lista_cantidades = [1]
lista_precios = [2000]

opcion = menu()

# Ciclo principal

while opcion != FIN:
    if opcion == 1:
        ingresarProducto()
    elif opcion == 2:
        codigo = int(input('Ingrese código del producto que desea eliminar %s: ' %lista_codigos))
        eliminarProducto(codigo)
    elif opcion == 3:
        codigo = int(input('Ingrese código del producto que desea modificar cantidad %s: ' %lista_codigos))
        cantidad = int(input('Ingrese la cantidad del producto a modificar: '))
        while cantidad < 0:
            print('Error, no puede ingresar una cantidad menor a 0')
            cantidad = int(input('Ingrese la cantidad del producto: '))
        modificarCantidad(codigo, cantidad)
        print(lista_cantidades)
    else:
        codigo = int(input('Ingrese código del producto que desea modificar precio %s: ' %lista_codigos))
        precio = int(input('Ingrese precio del producto a modificar: '))
        while precio < 0:
            print('Error, el precio no puede ser menor a 0')
            precio = int(input('Ingrese precio del producto: '))
        modificarPrecio(codigo, precio)
    imprimirDatos()
    opcion = menu()