FIN = 6
LIM_INF = 0
LIM_SUP = 5
DESC_NVIDIA = 10/100
DESC_AMD = 20/100


marcas = ['NVIDIA', 'NVIDIA', 'NVIDIA', 'AMD', 'AMD']
modelo = ['GTX710', 'GTX1050TI', 'GTX1650TIS', 'RX5000XT', 'RX5700']
precios = [60000, 80000, 230000, 290000, 430000]


''' 60000*2 // 20% * 2 12000    1 2
80000*3 // 20% * 3 16000        3 3
280000*4 // 20% * 4 56000 5     5 4'''  

def menu():
    
    print('[0] NVIDIA GTX710\n[1] NVIDIA GTX1050TI\n[2] NVIDIA GTX1650TIS\n[3] AMD RX5000XT\n[4] AMD RX5700\n[6]Fin')

    opcion = int(input('Ingrese tarjeta que desea comprar: '))
    while opcion != FIN and (opcion < LIM_INF or opcion > LIM_SUP):
        print('Error, la opción ingresada no es válida')
        opcion = int(input('Ingrese tarjeta que desea comprar: '))

    return opcion

def calcularSubTotal(opcion, cantidad):
    return precios[opcion]*cantidad

def calcularDescuentoMarca(opcion, cantidad):

    if marcas[opcion] == 'NVIDIA':
        return precios[opcion] * DESC_NVIDIA * cantidad
    else:
        return precios[opcion] * DESC_AMD * cantidad

# Programa principal

opcion = menu()

subTotal = 0 # Acumulador
descuentoMarcas = 0 # Acumulador
descuentoTotal = 0 

while opcion != FIN:

    cantidad = int(input('Ingrese cantidad del producto: '))

    while cantidad < 1:
        print('Error, la cantidad no puede ser menor o igual a 0')
        cantidad = int(input('Ingrese cantidad del producto: '))

    subTotal += calcularSubTotal(opcion, cantidad)
    descuentoMarcas += calcularDescuentoMarca(opcion, cantidad)

    print('Subtotal: ',subTotal)
    print('Descuento marcas: ',descuentoMarcas)

    opcion = menu()

totalAPagar = subTotal-descuentoMarcas
descuentoTienda = 0
if totalAPagar >= 750000:
    descuentoTienda = 10/100
else:
    descuentoTienda = 5/100


# SALIDAS
print('El total a pagar, con los descuentos finales es de: ', round(totalAPagar*(1-descuentoTienda)))
print('El total que debió haber pagado sin ofertas es de: ', subTotal)
print('Descuentos por marcas:', descuentoMarcas)
print('Descuento por tienda:', totalAPagar*descuentoTienda)



