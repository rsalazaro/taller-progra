# Constantes
INTERES = 3/100

# Entradas
cantidad_dinero = int(input('Ingrese la cantidad de dinero: '))

# Proceso

año_1 = round(cantidad_dinero*INTERES*1)
año_3 = round(cantidad_dinero*INTERES*3)
año_5 = round(cantidad_dinero*INTERES*5)

# Salidas

print('Dinero generado al año 1: ${0}\nDinero generado al año 2: ${1}\nDinero generado al año 3: ${2}'
        .format(año_1, año_3, año_5))