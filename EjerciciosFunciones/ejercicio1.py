""" 
    Crear una función que salude al usario por su nombre
    La función debe recibir como parámetro el nombre de la persona
    La función debe retornar una cadena de carácteres indicando: "Hola " + nombre_persona 
"""

def saludar(nombre_persona):
    return "Hola " + nombre_persona

# Programa principal 

nombre = input('Ingrese su nombre: ')

print(saludar(nombre))