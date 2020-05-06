#Escribir un algoritmo que calcule la nota mínima que necesita obtener un alumno en el proyecto final de la asignatura Taller de Programación I. Recuerde que la nota final del curso Taller de Programación I deberá ser >= 4.0 y los porcentajes de las evaluaciones son: 10% de la nota de cada trabajo (6 trabajos), 10% de la nota por participación y 30% de la nota del proyecto final.

#Constantes
PT = 10/100 #PT = PONDERACION TRABAJOS
PONDERACION_PARTICIPACION = 10/100
PONDERACION_PROYECTO = 30/100

#Entradas
nTrabajo1 = float(input('Ingrese nota trabajo 1: '))
nTrabajo2 = float(input('Ingrese nota trabajo 2: '))
nTrabajo3 = float(input('Ingrese nota trabajo 3: '))
nTrabajo4 = float(input('Ingrese nota trabajo 4: '))
nTrabajo5 = float(input('Ingrese nota trabajo 5: '))
nTrabajo6 = float(input('Ingrese nota trabajo 6: '))
nParticipacion = float(input('Ingrese nota participación: '))

#Proceso
# Nota final >= 4.0
# nT1 --> nota trabajo 1; nP --> nota Participación; PP --> ponderación participación;
# nPro --> nota proyecto; Ppro --> ponderación proyecto
# nT1*PT +...+ nT6*PT + nP * PP + nPro * PPro >= 4
# nPro = (4 - nT1*Pt +...+ nT6*Pt) / Ppro

nota_acumulada = nTrabajo1*PT+nTrabajo2*PT+nTrabajo3*PT+nTrabajo4*PT+nTrabajo5*PT+nTrabajo6*PT + nParticipacion*PONDERACION_PARTICIPACION
nota_necesaria = (4.0 - nota_acumulada)/PONDERACION_PROYECTO
#Salidas

print('La nota necesaria para aprobar el ramo deberá ser un %.1f' %nota_necesaria)