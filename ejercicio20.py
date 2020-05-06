#Escribir un algoritmo que solicite el monto del sueldo mensual de un trabajador y el monto del reajuste en porcentaje que se le hará y calcule el nuevo monto de su sueldo.

# Entradas

sueldo_trabajador = int(input('Ingrese sueldo de trabajador: '))
reajuste_sueldo = float(input('Ingrese reajuste de sueldo [0:100]: '))

# Proceso
# Recordar que se considera reajuste a un incremento del sueldo
nuevo_sueldo = sueldo_trabajador + sueldo_trabajador*reajuste_sueldo/100

# Salidas

print('El nuevo sueldo del trabajador es', nuevo_sueldo)