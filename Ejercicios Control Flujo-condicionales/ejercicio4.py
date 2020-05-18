# Entradas

hora = int(input('Ingrese la hora: '))

# Proceso
# Aplicar lo aprendido con respecto a verificación de datos, en este caso, 
# una hora no puede ser negativa ni mayor que 23 y los minutos deben estar en el rango [0:59]
# Analizar los rangos descritos en el enunciado para las horas
# Analizar los rangos descritos en el enunciado para los minutos

# Salidas

#Este if verifica que la hora sea válida en el rango [0:23]
if hora >= 0 and hora <= 23:
    minutos = int(input('Ingrese minutos: '))
    # Este if verifica que los minutos estén dentro del rango [0:59]
    if minutos >= 0 and minutos <= 59:
        # Este if verifica que la hora esté dentro del rango [5:12]
        if hora >= 5 and hora <= 12:
            # Ahora debemos tener cuidado con lo que nos dice el enunciado.
            # Si son las 5 pero aún no son las 5 30, aún es de noche, por lo que hay que imprimir buenas noches
            if hora == 5 and minutos < 30:
                print('Buenas noches')
            # Si son las 12 pero no son las 12:00, entones hay que imprimir buenas tardes
            elif hora == 12 and minutos != 0:
                print('Buenas tardes')
            else:
                print('Buenos días')
        # Este elif verifica que la hora esté dentro del rango [13:20]
        elif hora >=12 and hora <= 20:
            # Lo mismo ocurre a las 20, si son las 20 pero son pasadas las 20 15, entonces imprimir buenas noches
            if hora == 20 and minutos > 15:
                print('Buenas noches') 
            else:
                print('Buenas tardes')
        # Este else se ejecuta cuando la hora está dentro del rango [21:4]
        else:
            print('Buenas noches')
    else:
        print('Minutos no válidos')
else:
    print('Hora no válida')