# Ahora aplicaremos lo aprendido en el ejercicio anterior

numeros = [123,11,22,432,12343,2]

# Recuerden que esto se lee, por cada número en la lista números
for numero in numeros:
    num_aux = numero # Crearemos esta variable auxiliar que la usaremos para la impresión de más adelante

    # Ahora aplicaremos el algoritmo para descomponer un número en dígitos, para luego sumarlos aplicando acumuladores
    
    suma_digitos = 0 # Este es el acumulador que me irá sumando cada dígito del número, ahora tienen que pensar, por qué el acumulador está en esta posición del código: Respuesta, está en esta parte del código por que cada vez que el número cambie, tengo que reiniciar el contador, antes de empezar a sumar cada dígito del número
    while numero != 0:
        suma_digitos = suma_digitos + numero % 10
        numero = numero // 10
    
    # Ahora que tenemos la suma de los dígitos del número, hay que verificar si la suma es par o impar

    if suma_digitos % 2 == 0:
        print('La suma de los dígitos del número',num_aux,'es par')
    else:
        print('La suma de los dígitos del número',num_aux,'es impar')




