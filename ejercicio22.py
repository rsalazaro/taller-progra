#Una tienda vende bicicletas con un aumento del 50% sobre el precio de costo. Esta empresa paga a cada vendedor 2 sueldos mínimos mensuales, más un bono que se calcula como el monto total de la comisión del 15% sobre el precio de costo de todas las bicicletas vendidas por la tienda durante el mes, eso sí, dividida igualmente entre todos los vendedores. Escriba un algoritmo que solicite el número de vendedores de la tienda, el valor del sueldo mínimo, el precio de costo de cada tipo de bicicleta, el número de bicicletas vendidas de cada tipo y calcule el sueldo final de cada vendedor y las utilidades que obtuvo la tienda.

# Entradas

num_vendedores = int(input('Ingrese el número de vendedores: '))
sueldo_minimo = int(input('Ingrese el sueldo mínimo de los trabajadores: '))
costo_bici = int(input('Ingrese el precio de costo de una bicicleta: '))
num_bici_vendidas = int(input('Ingrese el número de bicicletas vendidas: '))

# Proceso

# El precio de venta de una bicicleta es del 50% sobre el precio de costo
precio_venta_bici = costo_bici * 1.5
# El bono del trabajador corresponde a una comisión del 15% sobre el costo de todas las bicis
# vendidas en el mes sobre la cantidad de vendedores
bono_vendedor = 0.15 * costo_bici * num_bici_vendidas / num_vendedores
# EL sueldo del vendedor es 2 veces el sueldo mínimo + el bono descrito anteriormente
sueldo_vendedor = sueldo_minimo * 2 + bono_vendedor
# Las utilidades de la empresa corresponde ganacias - costos, en donde las gananacias son
# la cantidad de bicicletas vendidas por el precio de venta y los costos corresponden
# al costo total de las bicicletas + los sueldos de los trabajadores
ganancias = precio_venta_bici * num_bici_vendidas
costos = costo_bici * num_bici_vendidas + sueldo_vendedor*num_vendedores
utilidades = ganancias - costos

# Salida
print('El sueldo de cada vendedor es',round(sueldo_vendedor),'las utilidades de la empresa es', round(utilidades))