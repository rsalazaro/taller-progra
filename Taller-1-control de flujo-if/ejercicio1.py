altitud = float(input('Ingrese altitud del avión comercial: '))

if altitud >= 5000:
    if altitud >= 5000 and altitud < 6000:
        print('El avión deberá fijar su velocidad en 400 km/hora')
    elif altitud >= 6000 and altitud < 9000:
        print('El avión deberá fijar su velocidad en 600 km/hora')
    elif altitud >= 9000 and altitud < 15000:
        print('El avión deberá fijar su velocidad en 800 km/hora')
    else:
        print('El avión deberá fijar su velocidad en 900 km/hora')
else:
    print('No se registra limite de velocidad para altitudes menores a 5000 metros')