vocales = 'aeiou'

s = input('Ingrese una letra: ')

# Verificamos que el usuario haya ingresado solo 1 carácter
if len(s) == 1:
    # Verificamos que la letra pertenezca al alfabeto
    if s.isalpha():
        if s in vocales or s in vocales.upper():
            print('La letra ingresada es una vocal')
        else:
            print('La letra ingresada es una consonante')
    else:
        print('El carácter ingresado no es una letra')
else:
    print('Debe ingresar solo 1 carácter')


