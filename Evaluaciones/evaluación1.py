#CONS
PRECIO_TECLADO = 10000
PRECIO_RATON = 5000
PRECIO_PENDRIVE = 15000
COMISION = 10/100
DESCUENTOS = 21/100

#1 Entradas

teclados_vendidos = int(input('Ingrese cantidad de teclados vendidos: '))
ratones_vendidos = int(input('Ingrese cantidad de ratones vendidos: '))
pendrive_vendidos = int(input('Ingrese cantidad de pendrive vendidos: '))
sueldo_minimo = int(input('Ingrese el sueldo mínimo'))

#2 Calculo de precio de costo

costo_teclado = PRECIO_TECLADO / (1 + 25/100)
costo_raton = PRECIO_RATON / (1 + 30/100)
costo_pendrive= PRECIO_PENDRIVE / (1 + 50/100)

#3 Calculo de comisiones por trabajador

comision_teclado = teclados_vendidos * costo_teclado * COMISION
comision_raton = ratones_vendidos * costo_raton * COMISION
comision_pendrive = pendrive_vendidos * costo_pendrive * COMISION

#4 Calculo de sueldo bruto por trabajador

sueldo_bruto_teclado = sueldo_minimo + comision_teclado
sueldo_bruto_raton = sueldo_minimo + comision_raton
sueldo_bruto_pendrive = sueldo_minimo + comision_pendrive

#5 Calculo de sueldos liquido por trabajador

sueldo_liquido_teclado = sueldo_bruto_teclado * (1 - DESCUENTOS)
sueldo_liquido_raton = sueldo_bruto_raton * (1 - DESCUENTOS)
sueldo_liquido_pendrive = sueldo_bruto_pendrive * (1 - DESCUENTOS)


#6 Calculo de utilidades de la empresa
#Sub-calculo de sueldos

sueldos = sueldo_bruto_teclado + sueldo_bruto_raton + sueldo_bruto_pendrive

#Sub-calculo ganancias por ventas
ganancias_ventas = (PRECIO_TECLADO - costo_teclado) * teclados_vendidos + (PRECIO_RATON - costo_raton) * ratones_vendidos + (PRECIO_PENDRIVE - costo_pendrive) * pendrive_vendidos

utilidades_empresa = ganancias_ventas - sueldos

#1 Salidas

print('Trabajador de teclados\tSueldo bruto {0}\tSueldo líquido {1}'.format(round(sueldo_bruto_teclado), round(sueldo_liquido_teclado)))
print('Trabajador de ratones\tSueldo bruto {0}\tSueldo líquido {1}'.format(round(sueldo_bruto_raton), round(sueldo_liquido_raton)))
print('Trabajador de pendrive\tSueldo bruto {0}\tSueldo líquido {1}'.format(round(sueldo_bruto_pendrive), round(sueldo_liquido_pendrive)))
print('Las utilidades de la empresa son',round(utilidades_empresa))