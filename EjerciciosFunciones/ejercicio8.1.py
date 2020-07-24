NOMBRE = 0
SUELDO = 1
SEXO = 2
FIN = 7

def promedioSueldos():
    acum_sueldos = 0
    cont_sueldos = 0

    for empleado in lista_empleados:
        acum_sueldos += empleado[SUELDO]
        cont_sueldos += 1
    
    return round(acum_sueldos / cont_sueldos)

def sueldoMin():
    sueldoMenor = lista_empleados[0][SUELDO]
    n = len(lista_empleados)

    for i in range(1, n):
        if lista_empleados[i][SUELDO] < sueldoMenor:
            sueldoMenor = lista_empleados[i][SUELDO]

    print('El sueldo menor es de', sueldoMenor)
    print('Los empleados que obtuvieron el sueldo menor son: ')

    for empleado in lista_empleados:
        if empleado[SUELDO] == sueldoMenor:
            print(empleado[NOMBRE])
    

def sueldoMay():
    sueldoMayor = lista_empleados[0][SUELDO]
    n = len(lista_empleados)

    for i in range(1, n):
        if lista_empleados[i][SUELDO] > sueldoMayor:
            sueldoMayor = lista_empleados[i][SUELDO]
    
    print('El sueldo mayor es de', sueldoMayor)
    print('Los empleados que obtuvieron el sueldo mayor son: ')

    for empleado in lista_empleados:
        if empleado[SUELDO] == sueldoMayor:
            print(empleado[NOMBRE])

def gananMenosDe(valorComp):

    cont_ganan_menos = 0
    for empleado in lista_empleados:
        if empleado[SUELDO] < valorComp:
            cont_ganan_menos += 1

    print('La cantidad de empleados que ganan menos de %d es %d' %(valorComp, cont_ganan_menos))
    print('Y estos empleados son: ')
    for empleado in lista_empleados:
        if empleado[SUELDO] < valorComp:
            print(empleado[NOMBRE], empleado[SUELDO])

def gananMasDe(valorComp):
    cont_ganan_mas = 0
    for empleado in lista_empleados:
        if empleado[SUELDO] > valorComp:
            cont_ganan_mas += 1

    print('La cantidad de empleados que ganan menos de %d es %d' %(valorComp, cont_ganan_mas))
    print('Y estos empleados son: ')
    for empleado in lista_empleados:
        if empleado[SUELDO] > valorComp:
            print(empleado[NOMBRE], empleado[SUELDO])

def gananEntre(valorInf, valorSup):
    cont_ganan_entre = 0
    for empleado in lista_empleados:
        if empleado[SUELDO] >= valorInf and empleado[SUELDO] <= valorSup:
            cont_ganan_entre += 1

    print('La cantidad de empleados que ganan entre %d y %d es %d' %(valorInf, valorSup, cont_ganan_entre))
    print('Y estos empleados son: ')
    for empleado in lista_empleados:
        if empleado[SUELDO] >= valorInf and empleado[SUELDO] <= valorSup:
            print(empleado[NOMBRE], empleado[SUELDO])

def menu():
    print('''
[1] Sueldo promedio de los empleados de una empresa
[2] El sueldo más bajo y quien o quienes lo obtuvieron
[3] El sueldo más alto y quien o quienes lo obtuvieron
[4] La cantidad de empleados que gananan menos de 500.000 y quien o quienes lo obtuvieron 
[5] La cantidad de empleados que ganan más de 600.000 y quien o quienes lo obtuvieron
[6] La cantidad de empleados que ganan entre 350000 y 750000 y quien o quienes lo obtuvieron
[7] Salir
''')
    opcion = int(input('Ingrese opción: '))
    
    while opcion != FIN and (opcion < 1 or opcion > 6):
        print('Error, la opción registrada no es válida')
        opcion = int(input('Ingrese opción: '))
        
    return opcion

lista_empleados = [
    ['Rodrigo', 250000, 'Hombre'],
    ['Alejandro', 350000, 'Hombre'],
    ['Javier', 750000, 'Hombre'],
    ['Karyn', 650000, 'Mujer'],
    ['Jimena', 150000, 'Mujer']
]

# Programa principal

opcion = menu()

while opcion != FIN:
    if opcion == 1:
        print('El promedio de los empleados es', promedioSueldos())
    elif opcion == 2:
        sueldoMin()
    elif opcion == 3:
        sueldoMay()
    elif opcion == 4:
        gananMenosDe(500000)
    elif opcion == 5:
        gananMasDe(600000)
    else:
        gananEntre(350000, 750000)
        
    opcion = menu()




