FIN = 4
LIM_INF = 1
LIM_SUP = 3

# (1) Definir las listas

lista_nombres = ['Rodrigo', 'Karyn', 'Javier']
lista_apellidos = ['Salazar', 'Didier', 'Nuñez']
lista_edades = [24, 24, 32]
lista_sexos = ['Hombre', 'Mujer', 'Hombre']
lista_deportes = ['Tenis', 'Voley', 'Futbol']

# Definir un menú de opciones
menu_opciones = ['1: Cantidad de hombres y mujers del club', '2: Los Mayores del club', '3: Promedio de edad de los que juegan Voley', '4: Salir']

for opcion in menu_opciones:
    print(opcion)

# (2) Datos de entrada y validación de datos de entrada

# Solicitar opción del menú
opcion = int(input('Ingrese una opción: '))

# Validar opcion
while opcion != FIN and (opcion < LIM_INF or opcion > LIM_SUP):
    print('Error, opción ingresada no válida')
    opcion = int(input('Ingrese una opción: '))

# (3) Crear el ciclo principal

while opcion != FIN:

    # Como es un ciclo iterativo, importante inicializar todas las variables antes de realizar los calculos

    contador_hombres = 0 # Un contador para contar hombres que juegan Voley
    contador_mujeres = 0 # Un contador para contar mujeres que juegan Voley
    edad_mayor = 0 # Recordemos que para buscar un mayor, debemos crear una variable que contendrá dicho número e inicializarla con el menor valor posible
    suma_edades = 0 # Un acumulador para acumular las edades de los socios del club
    contador_voley = 0 # Un contador para contar los socios que juegan Voley
    # Comenzar a programar la lógica del problema
    
    # (4) Opción 1, contar hombres y mujeres que juegan Voley
    if opcion == 1:
        
        indice = 0 # Recordemos el uso del indice para moverme entre las listas correlativas
        for deporte in lista_deportes:
            # Verificar si juega Voley
            if deporte == 'Voley':
                # Verificar si es hombre
                if lista_sexos[indice] == 'Hombre':
                    contador_hombres = contador_hombres + 1
                # Si no es hombre, es mujer
                else:
                    contador_mujeres = contador_mujeres + 1
            
            # Incrementar el contador

            indice = indice + 1

        # Luego de reccorer la lista deportes, imprimir lo solicitado

        print('Existen %d hombres y %d mujeres que juegan Voley' %(contador_hombres, contador_mujeres))
        print('Y ellos son: ')

        # Recorre nuevamente la lista deporte para imprimir los datos de cada socio que juega Voley
        indice = 0
        for deporte in lista_deportes:
            if deporte == 'Voley':
                print('%s %s %s %s' %(lista_apellidos[indice], lista_nombres[indice], lista_edades[indice], lista_sexos[indice]))
            indice = indice + 1

    # (5) Opción 2, mostrar los que tienen la edad mayor
    elif opcion == 2:
        # Recorrer la lista edades
        for edad in lista_edades:
            if edad > edad_mayor:
                edad_mayor = edad
         # Una vez encontrado la edad mayor, recorrer la lista edades nuevamente parar imprimir lo solicitado
        print('La edad mayor es', edad_mayor)        
        print('Los socios que tienen la edad mayor son: ')
        indice = 0
        for edad in lista_edades:
            if edad == edad_mayor:
                print('%s %s %s %s' %(lista_apellidos[indice], lista_nombres[indice], lista_sexos[indice], lista_deportes[indice]))
            indice = indice + 1

    # (6) Opción 3, mostrar el promedio de edades de los socios del club
    else:
        # Recorrer la lista deportes para conocer a los socios que juegan Voley
        indice = 0
        for deporte in lista_deportes:
            if deporte == 'Voley':
                suma_edades = suma_edades + lista_edades[indice] # Acumular la edad del socio que juega Voley
                contador_voley = contador_voley + 1 # Contar los que juegan Voley
            indice = indice + 1
        
        # Imprimir el promedio de edades 
        print('El promedio de edad de los socios del club es de',round(suma_edades/contador_voley))

    # Volver a solitar los datos

    opcion = int(input('Ingrese una opción: '))

    # Validar opcion
    while opcion != FIN and (opcion < LIM_INF or opcion > LIM_SUP):
        print('Error, opción ingresada no válida')
        opcion = int(input('Ingrese una opción: '))