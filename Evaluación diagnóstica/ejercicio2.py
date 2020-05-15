# Constantes
PORCENTAJE_BONO = 5/100

# Entradas

sueldo_minimo = int(input('Ingrese sueldo mínimo: '))
utilidades_empresa = int(input('Ingrese utilidades de la empresa: '))
cantidad_trabajadores = int(input('Ingrese cantidad de trabajadores: '))
edad_empleado = int(input('Ingrese la edad del trabajador: '))

# Proceso

bono_operaciones = PORCENTAJE_BONO * utilidades_empresa / cantidad_trabajadores
bono_edad = sueldo_minimo * edad_empleado / 100
sueldo_final = sueldo_minimo * 5 + bono_operaciones + bono_edad

# Salidas

print('El sueldo final del trabajador es de $', round(sueldo_final))