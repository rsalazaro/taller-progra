""" 
    Crear una función que indique si una persona es mayor de edad o menor de edad
    La función debe recibir como parámetro la edad de la persona
    La función debe retornar True si la edad de la persona es mayor o igual a 18
    La función debe retornar False si la edad de la persona es menor a 18 
    Al finalizar, imprimier "Eres mayor de edad" o "Eres menor de edad" según el caso
"""

def esMayorEdad(edad_persona):
    if edad_persona >= 18:
        return True
    else:
        return False


# Programa principal 

edad = int(input('Ingrese su edad: '))

if esMayorEdad(edad):
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')