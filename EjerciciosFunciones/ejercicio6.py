""" 
    Crear un programa que, mediante funciones:
        Calcule el promedio de notas de un alumno
        Calcule la nota mayor de ese alumno
        Calcule la nota menor de ese alumno
    Defina las notas del alumno en una lista 

"""

def promedioNotas(lista_notas):
    suma_notas = 0
    contador_notas = 0
    
    for nota in lista_notas:
        suma_notas = suma_notas + nota
        contador_notas = contador_notas + 1
        
    promedio_notas = suma_notas / contador_notas
    
    return promedio_notas

def notaMayor(lista_notas):
    mayor_nota = 1
    
    for nota in lista_notas:
        if nota > mayor_nota:
            mayor_nota = nota
            
    return mayor_nota


def notaMenor(lista_notas):
    menor_nota = lista_notas[0]
    
    m = len(lista_notas)
    for i in range(1,m):
        if lista_notas[i] < menor_nota:
            menor_nota = lista_notas[i]
            
    return menor_nota


# Programa principal

notas = [3,1,7]

print('EL promedio de notas del alumno es', promedioNotas(notas))
print('La mayor nota del alumno es', notaMayor(notas))
print('La menor nota del alumno es', notaMenor(notas))