FIN = 0
LIM_INF = 1
LIM_SUP = 6


resultado = int(input('Ingrese el resultado del lanzamiento del dado de 6 caras [%d para finalizar]: ' %FIN))

while resultado != FIN and (resultado < LIM_INF or resultado > LIM_SUP):
    print('Error, resultado del lanzamiento no válido, recuerde que un dado de 6 caras [%d a %d]' %(LIM_INF, LIM_SUP))
    resultado = int(input('Ingrese el resultado del lanzamiento del dado de 6 caras [%d para finalizar]: ' %FIN))

while resultado != FIN:

    # Calcular lado opuesto

    lado_opuesto = 7 - resultado

    print('EL lado opuesto del dado lanzado es', lado_opuesto)

    # Solicitar nuevamente el resultado del lanzamiento del dado

    resultado = int(input('Ingrese el resultado del lanzamiento del dado de 6 caras [%d para finalizar]: ' %FIN))

    while resultado != FIN and (resultado < LIM_INF or resultado > LIM_SUP):
        print('Error, resultado del lanzamiento no válido, recuerde que un dado de 6 caras [%d a %d]' %(LIM_INF, LIM_SUP))
        resultado = int(input('Ingrese el resultado del lanzamiento del dado de 6 caras [%d para finalizar]: ' %FIN))