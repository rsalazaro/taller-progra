# Constantes

NOTA_APROBACION = 4.0
CANTIDAD_NOTAS = 3

# Entradas
nota_1 = float(input('Ingrese nota 1: '))
if nota_1 >= 1.0 and nota_1 <= 7.0:
    nota_2 = float(input('Ingrese nota 2: '))
    if nota_2 >= 1.0 and nota_2 <= 7.0:
        nota_3 = float(input('Ingrese nota 3: '))
        if nota_3 >= 1.0 and nota_3 <= 7.0:
            # Proceso
            # Calcular un promedio de 3 notas

            promedio = (nota_1 + nota_2 + nota_3) / CANTIDAD_NOTAS

            if promedio >= NOTA_APROBACION:
                print('El alumno ha aprobado la asignatura con nota %.2f' %promedio)
            else:
                print('El alumno ha reprobado la asignatura con nota %.2f' %promedio)
        else:
            print('La nota 3 no es una nota válida')
    else:
        print('La nota 2 no es una nota válida')
else:
    print('La nota 1 no es una nota válida')

