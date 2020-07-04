# 17. Permita calcular el promedio de un alumno sabiendo que se ingresa por alumno la nota de 6 materias y su
# número de rut (0 para finalizar). No se sabe la cantidad de alumnos. Imprimir: “El alumno cuyo rut es xxxxxxxx,
# obtuvo de promedio un 5,7 por lo que aprobó la asignatura” (o reprobó según la nota).

# Uso de constante
FIN = 0
# Inicializar con vacío (sin elementos) una lista para los números de rut y otra lista para los promedios de notas.
alumnos_ruts = []
alumnos_promedios = [] 

print('ENTRADA DE INFORMACIÓN:')
# Solicitar el número de rut para un primer alumno.
numero_rut = str(input(f'\nIngrese el número de rut ({FIN} para finalizar): '))
# Repetir n veces el bloque de instrucciones dentro de while (línea 15) mientras número de rut sea distinto a 0.
while numero_rut != str(FIN):
    # Inicializar con valor 0 la variable suma_notas.
    suma_notas = 0
    # Agregar el número de rut del alumno a la lista alumnos_ruts.
    alumnos_ruts.append(numero_rut)
    # Repetir 6 veces el bloque de instrucciones dentro de for (línea 21) para las notas.
    for i in range(6):
        # Solicitar una nota del alumno.
        nota = float(input(f'Ingrese la nota {i+1} del alumno {numero_rut}: '))
        # Repetir n veces el bloque de instrucciones dentro del while mientras nota sea menor que 1 o mayor que 7. 
        while nota < 1 or nota > 7:
            print(f'La nota ingresada {nota} está afuera del rango permitido. Inténtelo de nuevo.')
            nota = float(input(f'Ingrese la nota {i+1} del alumno {numero_rut}: ')) # Última instrucción de for. Repetir bucle.
        # Sumar la nota al valor de suma_notas.
        suma_notas += nota
    # Calcular el promedio de notas del alumno.
    promedio_notas = round(suma_notas / 6, 2)
    # Agregar el promedio de notas del alumno a la lista alumnos_promedios.
    alumnos_promedios.append(promedio_notas)
    # Solicitar el número de rut para un nuevo alumno.
    numero_rut = str(input(f'\nIngrese el número de rut ({FIN} para finalizar): ')) # Última instrucción de while. Repetir bucle.
    
print('\nSALIDA DE INFORMACIÓN:\n')
# Repetir como veces el n° de elementos de la lista alumnos_ruts el bloque de instrucciones dentro de for (línea 39) para evaluar cada promedio.
for i in range(len(alumnos_ruts)):
    if alumnos_promedios[i] >= 3.95:
        print(f'~ El alumno cuyo rut es {alumnos_ruts[i]}, obtuvo de promedio un {alumnos_promedios[i]} por lo que aprobó la asignatura.')
    else:
        print(f'~ El alumno cuyo rut es {alumnos_ruts[i]}, obtuvo de promedio un {alumnos_promedios[i]} por lo que reprobó la asignatura.')
