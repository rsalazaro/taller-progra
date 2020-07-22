''' 
    Crear un programa que calcule
        Sueldo promedio de los empleados de una empresa
        El sueldo más bajo
        El sueldo más alto
        La cantidad de empleados que gananan menos de 500.000 
        La cantidad de empleados que ganan más de 600.000
        La cantidad de empleados que ganan entre 350.000 y 750.000 (incluidos)
    Defina una lista sueldo empleados
'''

def promedioSueldos(sueldos_empleados):
    suma_sueldos = 0 # Acumulador
    contador_sueldos = 0 # Contador
    
    for sueldo in sueldos_empleados:
        #suma_sueldos = suma_sueldos + sueldo
        #contador_sueldos = contador_sueldos + 1
        suma_sueldos += sueldo
        contador_sueldos += 1
        
    promedio = suma_sueldos / contador_sueldos
    
    return promedio


def sueldoMin(sueldos_empleados):
    n = len(sueldos_empleados)
    sueldoMenor = sueldos_empleados[0]
    
    for i in range(n):
        if sueldos_empleados[i] < sueldoMenor:
            sueldoMenor = sueldos_empleados[i]
            
    return sueldoMenor
        
def sueldoMay(sueldos_empleados):
    sueldoMayor = 0
    
    for sueldo in sueldos_empleados:
        if sueldo > sueldoMayor:
            sueldoMayor = sueldo
            
    return sueldoMayor

def gananMenosDe(sueldos_empleados, valorComp):
    cont_ganan_menos = 0
    
    for sueldo in sueldos_empleados:
        if sueldo < valorComp:
            cont_ganan_menos += 1
            
    return cont_ganan_menos
    
def gananMasDe(sueldos_empleados, valorComp):
    cont_ganan_mas = 0
    
    for sueldo in sueldos_empleados:
        if sueldo > valorComp:
            cont_ganan_mas += 1
            
    return cont_ganan_mas

def gananEntre(sueldos_empleados, valorInf, valorSup):
    cont_ganan_entre = 0
    
    for sueldo in sueldos_empleados:
        if sueldo >= valorInf and sueldo <= valorSup:
            cont_ganan_entre += 1
    
    return cont_ganan_entre

# Programa principal

sueldos = [340000, 650000, 510000, 1450000, 350000, 450000, 750000]

print('El promedio de los empleados es', round(promedioSueldos(sueldos)))
print('El sueldo más bajo', sueldoMin(sueldos))
print('El sueldo más alto', sueldoMay(sueldos))
print('La cantidad de empleados que ganan menos de 500.0000', gananMenosDe(sueldos, 500000))
print('La cantidad de empleados que ganan más de 600.000 es', gananMasDe(sueldos, 600000))
print('La cantidad de empleados que ganan entre 350.000 y 750.000 es', gananEntre(sueldos, 350000, 750000))

