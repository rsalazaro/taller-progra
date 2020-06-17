# Constantes

ACADEMICO = 1
FUNCIONARIO = 2
AUXILIAR = 3

PORC_SALUD = 7/100
PORC_PREV = 10/100    

# Validar datos de entrada
sueldo = int(input('Ingrese el sueldo del trabajador: '))
if sueldo > 0:
    antiguedad = int(input('Ingrese la antiguedad que lleva en la empresa: '))
    if antiguedad >= 0 and antiguedad <= 70:
        estamento = int(input('Ingrese el estamento al que pertenece el trabajador\n[1]Académico\n[2]Funcionario\n[3]Auxiliar\n:'))
        if estamento > 0 and estamento < 4:
            
            # Calculo del bono
            
            bono = 0
            
            if antiguedad <= 5:
                bono = sueldo * 0.1
            elif antiguedad <= 10:
                if estamento == ACADEMICO or estamento == FUNCIONARIO:
                    bono = sueldo * 0.15
                else:
                    bono = sueldo * 0.05
            else:
                if estamento == ACADEMICO:
                    bono = sueldo * 0.25
                elif estamento == FUNCIONARIO:
                    bono = sueldo * 0.3
                else:
                    bono = sueldo * 0.2
            
            # Calculo de los descuentos
            
            descuento_salud = sueldo * PORC_SALUD
            descuento_prevision = sueldo * PORC_PREV
            
            # Calculo del sueldo líquido
            sueldo_liquido = sueldo + bono - descuento_salud - descuento_prevision
            
            # Salidas
            
            print('Al trabajador le corresponde un bono de:',round(bono))
            print('Descuentos por salud:',round(descuento_salud))
            print('Descuentos por previsión:',round(descuento_prevision))
            print('Suldo líquido del trabajador:',round(sueldo_liquido))
            
        else:
            print('Estamento no válido')
    else:
        print('Antiguedad no válida')
else:
    print('Sueldo no válido')