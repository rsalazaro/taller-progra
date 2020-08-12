# Sanguchería "Donde el profesor"
# Ayudar al encargado a registrar el pedido de los clientes

# Definir una carta | definir un método para agregar la compra de un cliente que sea sencilla
# Agregar la opción de agregar pedido de cliente
# Imprimir una boleta, con el total del pedido del cliente

# Indices de la lista carta son

NOMBRE = 0
PRECIO = 1
CODIGO = 2

# Indices de la lista pedidoCliente

NOMBRE_PEDIDO = 0
CANTIDAD = 1
SUBTOTAL = 3

# Constantes para el menú de opciones

LIM_INF = 1
LIM_SUP = 5
FIN = 6

MOSTRAR_CARTA = 1
AGREGAR_PEDIDO = 2
MOSTRAR_PEDIDO = 3
ELIMINAR_PRODUCTO_PEDIDO = 4
EDITAR_PRODUCTO_PEDIDO = 5

PJE_PROPINA = 10/100

carta = [
    ['Completo', 1000, 2020],
    ['Churrasco italiano', 2500, 2021],
    ['Ave mayo', 2000, 2022],
    ['Hamburguesa', 2300, 2023]
]

pedidoCliente = []

# NOMBRE CANTIDAD TOTAL

# Funciones

def imprimirCarta(carta):
    print('%-30s%-10s%-10s' %('NOMBRE', 'PRECIO', 'CÓDIGO'))
    print('************************************************')
    for sandwich in carta:
        print('%-30s%-10s%-10s' %(sandwich[NOMBRE], sandwich[PRECIO], sandwich[CODIGO]))
    print('************************************************')

def agregarPedido(carta, codigo, pedidoCliente):
    indice = buscarCodigo(carta, codigo)
    
    if indice != -1:
        cantidad = int(input('Ingrese la cantidad del producto %s: ' %carta[indice][NOMBRE]))
        
        while cantidad < 1:
            print('Error, la cantidad no puede ser menor a 1')
            cantidad = int(input('Ingrese la cantidad del producto %s: ' %carta[indice][NOMBRE]))
        pedidoCliente.append([carta[indice][NOMBRE], cantidad, carta[indice][CODIGO], carta[indice][PRECIO]*cantidad])
        return 'Pedido agregado con éxito'  
    else:
        return 'Código ingresado no válido'
    
def eliminarProductoPedido(pedidoCliente, codigo):
    indice = buscarCodigo(pedidoCliente, codigo)
    
    if indice != -1:
        pedidoCliente.pop(indice)
        return 'Producto eliminado exitosamente'
    else:
        return 'Producto no encontrado'

def editarCantidadProducto(pedidoCliente, codigo, carta):
    indice = buscarCodigo(pedidoCliente, codigo)
    
    if indice != -1:
        cantidad = int(input('Ingrese la cantidad a eliminar: '))
        
        while cantidad < 0 or cantidad > pedidoCliente[indice][CANTIDAD]:
            print('Error, la cantidad ingresada no es válida')
            cantidad = int(input('Ingrese la cantidad a eliminar: '))
        
        pedidoCliente[indice][CANTIDAD] -= cantidad
        pedidoCliente[indice][SUBTOTAL] = carta[buscarCodigo(carta, codigo)][PRECIO] * pedidoCliente[indice][CANTIDAD]
        
        return 'Producto editado con éxito'
    
    return 'Producto no encontrado'
        
def buscarCodigo(carta, codigo):
    indice = -1
    for i in range(len(carta)): 
        if carta[i][CODIGO] == codigo:
            indice = i
    return indice


def imprimirBoleta(pedidoCliente):
    total = 0
    print('%-30s%-10s%-10s' %('NOMBRE', 'CANTIDAD', 'TOTAL'))
    for sandwich in pedidoCliente:
        print('%-30s%-10s%-10s' %(sandwich[NOMBRE], sandwich[CANTIDAD], sandwich[SUBTOTAL]))
        total += sandwich[SUBTOTAL]
    propina = round(total*PJE_PROPINA)
    print('Propina %.0f %%: %d' %(PJE_PROPINA*100, propina))
    print('Total a pagar:', total+propina)

def menu_opciones():
    
    opcion = int(input('[1]Imprimir carta\n[2]Agregar pedido\n[3]Ver parcial\n[4]Eliminar producto del pedido\n[5]Editar cantidad producto del pedido\n[6]Finalizar\n ---> :'))
    
    while opcion != FIN and (opcion < LIM_INF or opcion > LIM_SUP):
        print('Error, opción no válida')
        opcion = int(input('[1]Imprimir carta\n[2]Agregar pedido\n[3]Ver parcial\n[4]Finalizar'))    
    return opcion

# Programa principal

opcion = menu_opciones()

# Ciclo principal

while opcion != FIN:
    
    if opcion == MOSTRAR_CARTA:
        imprimirCarta(carta)
    elif opcion == AGREGAR_PEDIDO:
        codigo = int(input('Ingresar código del pedido: '))
        print(agregarPedido(carta, codigo, pedidoCliente))
    elif opcion == MOSTRAR_PEDIDO:
        imprimirBoleta(pedidoCliente)
    elif opcion == ELIMINAR_PRODUCTO_PEDIDO:
        codigo = int(input('Ingresar código del pedido: '))
        print(eliminarProductoPedido(pedidoCliente, codigo))
    elif opcion == EDITAR_PRODUCTO_PEDIDO:
        codigo = int(input('Ingresar código del pedido: '))
        print(editarCantidadProducto(pedidoCliente, codigo, carta))
    opcion = menu_opciones()
    
imprimirBoleta(pedidoCliente)