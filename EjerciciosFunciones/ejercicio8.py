''' 
    Crear un programa que calcule
        Sueldo promedio de los empleados de una empresa
        El sueldo más bajo y quien o quienes lo obtuvieron
        El sueldo más alto y quien o quienes lo obtuvieron
        La cantidad de empleados que gananan menos de 500.000 y quien o quienes lo obtuvieron 
        La cantidad de empleados que ganan más de 600.000 y quien o quienes lo obtuvieron
    Defina una lista sueldo empleados
    Defina una lista de nombres de empleados
    Recuerde que ambas listas son correlativas
'''

FIN = 0

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

# Funciones parte 2

def imprimirEmpleadosSueldoMin(sueldos_empleados, lista_empleados):
    sueldoMenor = sueldoMin(sueldos_empleados)
    n = len(sueldos_empleados)
    
    print('Los empleados que obtuvieron el sueldo %d son:' %sueldoMenor)
    for i in range(n):
        if sueldos_empleados[i] == sueldoMenor:
            print(i+1,':',lista_empleados[i])
            
def imprimirEmpleadosSueldoMay(sueldos_empleados, lista_empleados):
    sueldoMayor = sueldoMay(sueldos_empleados)
    n = len(sueldos_empleados)
    
    print('Los empleados que obtuvieron el sueldo %d son:' %sueldoMayor)
    for i in range(n):
        if sueldos_empleados[i] == sueldoMayor:
            print(i+1,':',lista_empleados[i])

def imprimirGananMenosDe(sueldos_empleados, lista_empleados, valorComp):
    n = len(sueldos_empleados)
    
    print('Los empleados que ganan menos de %d son:' %valorComp)
    for i in range(n):
        if sueldos_empleados[i] < valorComp:
            print(i+1,':',lista_empleados[i])
    
def imprimirGananMasDe(sueldos_empleados, lista_empleados, valorComp):
    n = len(sueldos_empleados)
    
    print('Los empleados que ganan más de %d son:' %valorComp)
    for i in range(n):
        if sueldos_empleados[i] > valorComp:
            print(i+1,':',lista_empleados[i], '$',sueldos_empleados[i])
            
def imprimirGananEntre(sueldos_empleados, lista_empleados, valorInf, valorSup):
    n = len(sueldos_empleados)
    
    print('Los empleados que ganan entre %d y %d son:' %(valorInf, valorSup))
    for i in range(n):
        if sueldos_empleados[i] >= valorInf and sueldos_empleados[i] <= valorSup:
            print(i+1,':',lista_empleados[i], '$',sueldos_empleados[i])
            
            
def menu():
    print('''
[1] Sueldo promedio de los empleados de una empresa
[2] El sueldo más bajo y quien o quienes lo obtuvieron
[3] El sueldo más alto y quien o quienes lo obtuvieron
[4] La cantidad de empleados que gananan menos de 500.000 y quien o quienes lo obtuvieron 
[5] La cantidad de empleados que ganan más de 600.000 y quien o quienes lo obtuvieron
[6] La cantidad de empleados que ganan entre 350000 y 750000 y quien o quienes lo obtuvieron
''')

    opcion = int(input('Ingrese opción: '))
    
    while opcion != FIN and (opcion < 1 or opcion > 6):
        print('Error, la opción registrada no es válida')
        opcion = int(input('Ingrese opción: '))
        
    return opcion
# Programa principal

opcion = menu()

sueldos = [340000, 650000, 340000, 340000, 350000, 450000, 750000]
empleados = ['Rodrigo', 'Karyn', 'Jimena', 'Hector', 'Patricia', 'Javier', 'Paula']

while opcion != FIN:
    if opcion == 1:
        print('El promedio de los empleados es', round(promedioSueldos(sueldos)))
    elif opcion == 2:
        print('El sueldo más bajo', sueldoMin(sueldos))
        imprimirEmpleadosSueldoMin(sueldos, empleados)
    elif opcion == 3:
        print('El sueldo más alto', sueldoMay(sueldos))
        imprimirEmpleadosSueldoMay(sueldos, empleados)        
    elif opcion == 4:
        print('La cantidad de empleados que ganan menos de 500.0000', gananMenosDe(sueldos, 500000))
        imprimirGananMenosDe(sueldos, empleados, 500000)
    elif opcion == 5:
        print('La cantidad de empleados que ganan más de 600.000 es', gananMasDe(sueldos, 600000))
        imprimirGananMasDe(sueldos, empleados, 600000)
    else:
        print('La cantidad de empleados que ganan entre 350.000 y 750.000 es', gananEntre(sueldos, 350000, 750000))
        imprimirGananEntre(sueldos, empleados, 350000, 750000)
        
    opcion = menu()
