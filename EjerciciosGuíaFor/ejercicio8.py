ruts = ['111-1', '222-2', '333-3', '444-4', '555-5']
años_antiguedad = [2,5,7,1,3]
sueldos = [1000000,1000000,1000000,1000000,1000000] # Es más fácil ver los resultados de incrementos con valores en potencias de 10
sueldos_aumentados = []
indice = 0

aumento_mayor = 0
aumento_menor = sum(sueldos)

mayores = []
menores = []

# Iteraremos sobre la lista de años, ya que dependiendo de los años de antiguedad de la persona se realiza el incremento de sueldo

for antiguedad in años_antiguedad:

    # Crearemos una variable aumento para almacenar el aumento que obtuvo el trabajador
    if antiguedad <= 2:
        aumento = round(sueldos[indice]*0.05)
    elif antiguedad <= 5:
        aumento = round(sueldos[indice]*0.08)
    else:
        aumento = round(sueldos[indice]*0.12)

    # Aplicaremos el algoritmo para encontrar mayores, pero agregaremos un pequeño detalle, guardarlos en una lista de mayores en el caso de que encontremos más de uno

    if aumento > aumento_mayor:
        # En el caso que el aumento sea mayor al mayor aumento registrado, hay que "vaciar" la lista mayores:
        aumento_mayor = aumento
            
        mayores = [] # Así podemos vaciar la lista
        mayores.append(ruts[indice]) # Luego, registraremos el rut del nuevo mayor
        
    elif aumento == aumento_mayor:
        # En el caso que el aumento sea igual al mayor aumento registrado, hay que incluirlo en la lista mayores
        mayores.append(ruts[indice])
    
    # Repetimos la lógica para el tema de los menores (en esta parte estuvo mi error, puse un else en vez de un if, lo que me ocasionaba que el menor no quedara registrado ya que quedaba en el mayor, en cambio con los dos if, el valor queda registrado como menor y mayor a la vez)
    if aumento < aumento_menor:
        menores = []
        menores.append(ruts[indice]) # Esta es una forma abreviada de vaciar y regitrar el nuevo menor
        aumento_menor = aumento
    elif aumento == aumento_menor:
        menores.append(ruts[indice])
        aumento_menor = aumento

    # Agregar el sueldo aumentado a la lista sueldos_aumentados para luego imprimir el promedio de aumento de sueldos
    sueldos_aumentados.append(aumento)

    # Recordemos aumentar el indice para ir acceder a los siguientes elementos de las listas ruts y sueldos
    indice = indice + 1
# Ahora, imprimiremos lo solicitado

print('El aumento mayor fue de $%d, y lo obtuvieron %s' %(aumento_mayor, mayores)) # %s para imprimir listas
print('El aumento menor fue de $%d, y lo obtuvieron %s' %(aumento_menor, menores))
print('El promedio de aumentos de sueldo fue de $%d' %(round(sum(sueldos_aumentados)/len(sueldos_aumentados)))) # Aprovechemos el uso de las operaciones [sum] y [len] sobre listas



