VALOR_HORA_EXTRA = 20000
DESCUENTO = 20/100

rut_empleado = input('Ingrese rut del trabajador [1.111.111-1]: ')
sueldo_base = int(input('Ingrese sueldo base: '))
antiguedad = int(input('Ingrese la cantidad de años que lleva en la empresa el trabajador: '))
horas_extras = int(input('Ingrese la cantidad de horas extras que trabajó: '))

# Variables necesarias

monto_primeras10 = 0
monto_siguientes20 = 0
porcentaje_segun_antiguedad = 0
monto_horas_restantes = 0
bono = 0

# Si el trabajador realizó horas extras

if horas_extras > 0:
    # Calcular el porcentaje que le corresponde según la antiguedad en la empresa
    if antiguedad < 10:
        porcentaje_segun_antiguedad = 50/100
    elif antiguedad < 20:
        porcentaje_segun_antiguedad = 75/100
    else:
        porcentaje_segun_antiguedad = 100/100
        
    # Calcular el pago de horas extras
    
    if horas_extras > 30:
        monto_horas_restantes = 2*(horas_extras - 30)*(VALOR_HORA_EXTRA)
        monto_primeras10 = 10*VALOR_HORA_EXTRA
        monto_siguientes20 = round(20*VALOR_HORA_EXTRA*(1+porcentaje_segun_antiguedad))
    else:
        if horas_extras > 10:
            monto_primeras10 = 10*VALOR_HORA_EXTRA
            monto_siguientes20 = round((horas_extras - 10)*VALOR_HORA_EXTRA*(1+porcentaje_segun_antiguedad))
        else:
            monto_primeras10 = horas_extras*VALOR_HORA_EXTRA
            
# Calcular bonos

if antiguedad > 15:
    bono = 300000
elif antiguedad > 10:
    bono = 200000
elif antiguedad > 5:
    bono = 100000

# Calcular el sueldo bruto

sueldo_bruto = sueldo_base + monto_primeras10 + monto_siguientes20 + monto_horas_restantes + bono

# Calcular el sueldo líquido

sueldo_liquido = round(sueldo_bruto*(1-DESCUENTO))

print('Rut del empleado:', rut_empleado)
print('{0:50}= $ {1:-5d}'.format('Sueldo base',sueldo_base))
if monto_primeras10 > 0:
    msg = 'Monto por pimeras 10 horas extra'
    print('{0:50}= $ {1:-5d}'.format(msg,monto_primeras10))
if monto_siguientes20 > 0:
    if horas_extras > 20:
        msg = 'Monto por 20 horas extra al %'+str(porcentaje_segun_antiguedad*100)
        print('{0:50}= $ {1:-5d}'.format(msg,monto_siguientes20))
    else:
        msg = 'Monto por'+str(horas_extras - 10)+'horas extra al %'+str(porcentaje_segun_antiguedad*100)
        print('{0:50}= $ {1:-5d}'.format(msg,monto_siguientes20))
if monto_horas_restantes > 0:
    msg: 'Monto por'+str(horas_extras - 30)+'horas extra restantes al %100'
    print('{0:50}= $ {1:-5d}'.format(msg,monto_horas_restantes))
if bono > 0:
    msg = 'Monto por bono de antiguedad'
    print('{0:50}= $ {1:-5d}'.format(msg,bono))

print('\n{0:50}= $ {1:-5d}'.format('Monto sueldo bruto',sueldo_bruto))
print('{0:50}= $-{1:-5d}'.format('Descuento por salud y previsión',round(sueldo_bruto*DESCUENTO)))
print('\n{0:50}= $ {1:-5d}'.format('Monto sueldo liquido',sueldo_liquido))
