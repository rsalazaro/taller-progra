digitos = '1234567890'
letrasMin = 'abcdefghijklmnñopqrstuvwxyz'
letrasMay = letrasMin.upper()

s = input('Ingrese un carácter: ')

# Validación de datos de entrada, forzaremos a que el usuario ingrese un solo carácter
# Recordar que la función len() retorna el largo de un 'objeto', en este caso, len(s)
# retorna el largo de el dato ingresado por el usuario
# Un ejemplo: len('Rodrigo') retorna el valor 7


if len(s) > 0 and len(s) < 2:
    if s in digitos:
        print('El carácter ingresado es un dígito')
    elif s in letrasMay or s in letrasMin:
        print('El carácter ingresado es una letra')
    else:
        print('El carácter ingresado no es ni un dígito ni una letra')
else:
    print('Debe ingresar solo un carácter, ni más no menos')

# Otra forma de realizar el ejercicio es utilizando la función isdigit() y isalpha()
# isdigit() retorna True o False dependiendo si el valor a evaluar es un dígito o no
# mientras que isalpha retorna True o False si el valor a evaliar es una letra del alfabeto o no
# Para ocupar ambas funciones, debemos anteponer la variable o dato a evaluar seguido de un punto
# Por ejemplo:
# '1'.isdigit() --> retorna True
# 'A'.isalpha() --> retorna False
# letra = 'b' 
# letra.isdigit() --> retorna False
# numeros = '1234'
# numeros.isdigit() --> retorna True

# if len(s) > 0 and len(s) < 2:
#     if s.isdigit():
#         print('El carácter ingresado es un dígito')
#     elif s.isalpha()
#         print('El carácter ingresado es una letra')
#     else:
#         print('El carácter ingresado no es ni un dígito ni una letra')
# else:
#     print('Debe ingresar solo un carácter, ni más no menos')