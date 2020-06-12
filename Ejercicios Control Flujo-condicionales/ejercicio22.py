palabra1 = input('Ingrese primera palabra: ')
palabra2 = input('Ingrese segunda palabra: ')

if len(palabra1) > len(palabra2):
    print('La palabra 1 es más larga que la palabra 2')
elif len(palabra2) > len(palabra1):
    print('La palabra 2 es más larga que la palabra 1')
else:
    print('Las palabras ingresadas tienen el mismo tamaño')