TARIFA1 = 110
TARIFA2 = 150
TARIFA3 = 250
TARIFA4 = 550

consumo = int(input('Ingrese consumo: '))

if consumo > 0:
    if consumo > 1000:
        pago = 100*TARIFA1 + 400*TARIFA2 + 500*TARIFA3 + (consumo-1000)*TARIFA4
    else:
        if consumo > 500:
            pago = 100*TARIFA1 + 400*TARIFA2 + (consumo - 500)*TARIFA3
        else:
            if consumo > 100:
                pago = 100*TARIFA1 + (consumo - 100)*TARIFA2
            else:
                pago = consumo * TARIFA1
    print('Se debe pagar un total de $', pago)
    
else:
    print('Consumo no válida')


