fila_caballo = int(input('Ingrese la posición de la fila del caballo: '))
col_caballo = int(input('Ingrese la posición de la columna del caballo: '))

fila_torre = int(input('Ingrese la posición de la fila de la torre: '))
col_torre = int(input('Ingrese la posición de la columna de la torre: '))

# Validar filas y columnas:

if fila_caballo > 0 and col_caballo > 0 and fila_caballo < 9 and  col_caballo < 9:
    if fila_torre > 0 and col_torre > 0 and fila_torre < 9 and col_torre < 9:
        # Verificar que la torre y el caballo no compartan la misma posición
        if not (fila_caballo == fila_torre and col_caballo == col_torre):
            # Verificar si la torre captura al caballo simulando el movimiento de la torre
            if col_caballo == col_torre or fila_caballo == fila_torre:
                print('La torre captura al caballo')
            # Verificar si el caballo captura la torre, simulando el movimiento del caballo
            elif (
            (fila_torre == fila_caballo + 2 and col_torre == col_caballo + 1) or
            (fila_torre == fila_caballo + 1 and col_torre == col_caballo + 2) or
            (fila_torre == fila_caballo - 1 and col_torre == col_caballo + 2) or
            (fila_torre == fila_caballo - 2 and col_torre == col_caballo + 1) or
            (fila_torre == fila_caballo - 2 and col_torre == col_caballo - 1 )or
            (fila_torre == fila_caballo - 1 and col_torre == col_caballo - 2) or
            (fila_torre == fila_caballo + 1 and col_torre == col_caballo - 2) or
            (fila_torre == fila_caballo + 2 and col_torre == col_caballo - 1)):
                print('Caballo captura a torre')
            else:
                print('Ninguna de las dos piezas captura')
        else:
            print('Las piezas no pueden estar en el mismo lugar')
    else:
        print('Posiciones de la torre no válidas')
else:
    print('Posiciones del caballo no válidas')