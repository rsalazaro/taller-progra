# CONSTANTES

LIM_INF = 1
LIM_SUP = 3
FIN = 4

INGRESAR_PRODUCTO = 1
LISTAR_PRODUCTOS = 2
LISTAR_PRODUCTOS_BAJO_STOCK = 3

# Indices lista productos_bodega

CODIGO = 0
NOMBRE = 1
PRECIO_VENTA = 2
PRECIO_COSTO = 3
CANTIDAD_BODEGA = 4
STOCK_CRITICO = 5


# Lista para guardar los productos


productos_bodega = []

def ingresarProducto():
    
    codigo = input('Ingrese código del producto: ')
    
    codigos = obtenerCodigos()
    
    # Verificar que el código sea único
    while codigo in codigos:
        print('Error, el código del producto ingresado ya se encuentra ocupado')
        codigo = input('Ingrese código del producto: ')
    nombre = input('Ingrese el nombre del producto: ')
    
    precio_venta = int(input('Ingrese precio venta del producto: '))
    
    # Verificar que el precio de venta no sea negativo
    while precio_venta < 0:
        print('Error, el precio de venta no puede ser menor a 0')
        precio_venta = int(input('Ingrese precio venta del producto: '))
    
    precio_costo = int(input('Ingrese el precio de costo del producto: '))
    
    # Verificar que el precio de costo no sea negativo ni mayor al precio de venta
    while precio_costo > precio_venta:
        print('Error, el precio de costo no puede ser menor a 0 ni mayor al precio de venta')
        precio_costo = int(input('Ingrese el precio de costo del producto: '))
        
    cantidad_bodega = int(input('Ingrese la cantidad en bodega: '))
    
    # Verificar que la cantidad en bodega no sea negativa
    while cantidad_bodega < 0:
        print('Error, la cantidad en bodega no puede ser menor a 0')
        cantidad_bodega = int(input('Ingrese la cantidad en bodega: '))
    
    stock_critico = int(input('Ingrese la cantidad de stock crítico: '))
    
    # Verificar que el stock crítico no sea negativo
    
    while stock_critico < 0:
        print('Error, el stock crítico no puede ser menor a 0')
        stock_critico = int(input('Ingrese la cantidad de stock crítico: '))
        
    productos_bodega.append([codigo, nombre, precio_venta, precio_costo, cantidad_bodega, stock_critico])
    
    print('Producto ingresado con éxito!!')
        
def listarProductos():
    
    print('%-10s%-10s%-15s%-10s' %('CÓDIGO', 'NOMBRE', 'PRECIO VENTA', 'CANTIDAD'))
    for producto in productos_bodega: # 
        print('%-10s%-10s$%-15s%-10s' %(producto[CODIGO], producto[NOMBRE], producto[PRECIO_VENTA], producto[CANTIDAD_BODEGA]))
    
def listarProductosBajoStock():
    print('%-10s%-10s%-15s%-20s%-10s' %('CÓDIGO', 'NOMBRE', 'PRECIO COSTO', 'CANTIDAD NECESARIA', 'MONTO NECESARIO'))
    for producto in productos_bodega:
        
        if producto[CANTIDAD_BODEGA] < producto[STOCK_CRITICO]:
            cantidad_necesaria = producto[STOCK_CRITICO] - producto[CANTIDAD_BODEGA]
            monto_necesario = cantidad_necesaria * producto[PRECIO_COSTO]
            print('%-10s%-10s$%-15s%-20s$%-10s' %(producto[CODIGO], producto[NOMBRE], producto[PRECIO_COSTO], cantidad_necesaria, monto_necesario))
            
def obtenerCodigos():
    codigos = []
    for producto in productos_bodega:
        codigos.append(producto[CODIGO])
        
    return codigos

def menu_opciones():
    opciones_menu = ['[1] Ingresar producto', '[2] Listar productos bodega', '[3] Listar productos bajo stock', '[4] Salir']
    for opcion_menu in opciones_menu:
        print(opcion_menu)
        
    opcion = int(input('Ingrese una opción del menú: '))
    
    while opcion != FIN and (opcion < LIM_INF or opcion > LIM_SUP):
        print('Error, opción ingresada no válida')
        opcion = int(input('Ingrese una opción del menú: '))
        
    return opcion

# Programa principal

opcion = menu_opciones()

while opcion != FIN:
    
    if opcion == INGRESAR_PRODUCTO:
        ingresarProducto()
    elif opcion == LISTAR_PRODUCTOS:
        print('-'*60)
        print('Productos en bodega')
        print('-'*60)
        listarProductos()
        print('-'*60)
    elif opcion == LISTAR_PRODUCTOS_BAJO_STOCK:
        print('-'*60)
        print('Productos bajo stock crítico')
        print('-'*60)
        listarProductosBajoStock()
        print('-'*60)
        
    opcion = menu_opciones()