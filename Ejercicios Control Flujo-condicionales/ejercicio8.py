a = int(input('Ingrese valor 1: '))
b = int(input('Ingrese valor 2: '))
if a > b:
    # Intercambio de variable
    aux = a
    a = b
    b = aux
c = int(input('Ingrese valor 3: '))
if b > c:
    aux = b
    b = c
    c = aux
    if a > b:
        aux = a
        a = b
        b = aux
d = int(input('Ingrese valor 4: '))
if c > d:
    aux = c
    c = d
    d = aux
    if b > c:
        aux = b
    b = c
    c = aux
    if a > b:
        aux = a
        a = b
        b = aux

print(a,b,c,d)
