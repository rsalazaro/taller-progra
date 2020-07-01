horas = [5,4,7,7,12,12,20,20,23,5]
minutos = [30,29,40,20,0,30,15,40,15,29]

''' 
Para este ejercicio, utilizaremos el uso de los indices de las listas
    Recordemos: lista = ['Rodrigo', 24, 'Profesor'] es un conjunto de elementos ordenados 
        en donde 'Rodrigo', se encuentra en la posición 0, 
        en donde 24, se encuentra en la posición 1,
        en donde 'Profesor', se encuentra en la posición 2
    A estas posiciones les llamaremos "indices"
    Luego, si quiero acceder a 'Profesor', debería escribir lista[2] 
'''

# Aplicando lo anteriormente mencionado

# Esta variable indice la utilizaremos para acceder al elemento N de la lista minutos
indice = 0
for hora in horas:
    if hora >= 5 and hora < 12:
        if hora == 5 and minutos[indice] < 30:
            print('[%d:%d] Buenas noches' %(hora, minutos[indice]))
        else:
            print('[%d:%d] Buenos días' %(hora, minutos[indice]))
    elif hora >= 12 and hora <= 20:
        if hora == 12 and minutos[indice] == 0:
            print('[%d:%d] Buenos días' %(hora, minutos[indice]))
        elif hora == 20 and minutos[indice] > 15:
            print('[%d:%d] Buenas noches' %(hora, minutos[indice]))
        else:
            print('[%d:%d] Buenas tardes' %(hora, minutos[indice]))
    else:
        print('[%d:%d] Buenas noches' %(hora, minutos[indice]))
    

    # Antes de pasar a la siguiente hora en nuestra lista horas, debo incrementar el indice, para acceder al siguiente elemento de mi lista minutos
    indice = indice + 1

# Desafío, verifique que las horas y los minutos de ambas listas sean horas y minutos válidos (horas entre 0 y 24; minutos entre 0 y 60)
# Respuesta del desafío en 5.1