# CONSTANTES

dd_actual = 20
mm_actual = 5
aaaa_actual = 2020



edad = 0

# Planificación: 
# Mi edad se puede calcular como año actual - año de nacimiento siempre y cuando:
# 1) Mi mes de nacimiento sea menor al mes actual, por ejemplo si nací en febrero y estamos a mayo
# ya cumplí años
# 2) En el caso de que estemos en el mismo mes, tengo que preguntar si el día de mi nacimiento 
# es menor o igual al día actual
# Si lo anterior no se cumple, entoNnces la edad se debe calcular como año actual - año nacimiento - 1

# Validación de datos : para simplificar el ejercicio, tomaremos en consideración
# que todos los meses pueden tener entre 1 y 31 días


dd_nacimiento = int(input('Ingrese día de nacimiento: '))

if dd_nacimiento > 0 and dd_nacimiento < 32:
    mm_nacimiento = int(input('Ingrese mes de nacimiento: '))
    if mm_nacimiento > 0 and mm_nacimiento < 13:
        aaaa_nacimiento = int(input('Ingrese año de nacimiento: '))
        # Vamos a considerar que una persona no puede tener más de 200 años
        if aaaa_nacimiento > aaaa_actual - 200 and aaaa_nacimiento <= aaaa_actual:
            if mm_nacimiento < mm_actual:
                edad = aaaa_actual - aaaa_nacimiento
            elif mm_nacimiento == mm_actual:
                if dd_nacimiento < dd_actual:
                    edad = aaaa_actual - aaaa_nacimiento
                else:
                    edad = aaaa_actual - aaaa_nacimiento - 1
            else:
                edad = aaaa_actual - aaaa_nacimiento - 1
            print('La edad de la persona es', edad)
        else:
            print('Año de nacimiento no válido')
    else:
        print('Mes de nacimiento no válido')
else:
    print('Día de nacimiento no válido')


