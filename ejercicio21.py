#Considere que un vendedor gana X% de la venta de un producto que cuesta $Y. Escriba un algoritmo que calcule la cantidad de unidades de ese producto que debe vender para ganar una cantidad $Z de dinero. Puede utilizar la función round() de Python para redondear a pesos.
import math

#Entradas

x = float(input('Ingrese porcentaje de ganancia del producto [0:100]: '))
y = int(input('Ingrese precio del producto: '))
z = int(input('Cantidad de dinero por ganar: '))

#Proceso

# z = 3000
# y = 1000
# x = 10% --> 0.1
# cantidad_unidades = 30

cantidad_unidades = z / ((x/100)*y)

# Salidas 
# math.ceil redondea hacia arriba y es necesario en este ejercicio ya que si necesita vender
# 3.1 unidades, en estricto rigor, tendrá que vender 4 unidades para alcanzar
# la meta
print('La cantidad de productos a vender es de', math.ceil(cantidad_unidades))