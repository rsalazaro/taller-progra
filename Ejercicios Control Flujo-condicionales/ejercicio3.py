# Entradas

hora = int(input('Ingrese la hora: '))

# Proceso
# Aplicar lo aprendido con respecto a verificación de datos, en este caso, una hora no puede ser negativa ni mayor que 23
# Analizar los rangos descritos en el enunciado

# Salidas

#Este if verifica que la hora sea válida rango [0:23]
if hora >= 0 and hora <= 23:
    # Este if verifica que la hora esté dentro del rango [5:12]
    if hora >= 5 and hora <= 12:
        print('Buenos días')
    # Este elif verifica que la hora esté dentro del rango [13:20]
    elif hora >=13 and hora <= 20:
        print('Buenas tardes')
    # Este else se ejecuta cuando la hora está dentro del rango [21:4]
    else:
        print('Buenas noches')
else:
    print('Hora no válida')