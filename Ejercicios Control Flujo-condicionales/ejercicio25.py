SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
EXPONENCIACION = 5


respuesta = 'si'
while respuesta.lower() == 'si':
    operacion = int(input('Ingrese alguna operación [1:Suma][2:Resta][3:Multiplicación][4:Division][5:Expoenciación]: '))
    
    if operacion >= 1 and operacion <= 5:
        valorA = int(input('Ingrese el valor A: '))
        valorB = int(input('Ingrese el valor B: '))
        if operacion == SUMA:
            print('{0}+{1}={2}'.format(valorA,valorB,valorA+valorB))
        elif operacion == RESTA:
            print('{0}-{1}={2}'.format(valorA,valorB,valorA-valorB))
        elif operacion == MULTIPLICACION:
            print('{0}*{1}={2}'.format(valorA,valorB,valorA*valorB))
        elif operacion == DIVISION:
            if valorB != 0:
                print('{0}/{1}={2}'.format(valorA,valorB,valorA/valorB))
            else:
                print('No se puede realizar una división por 0')
        else:
            print('{0}^{1}={2}'.format(valorA,valorB,valorA**valorB))
        respuesta = input('Desea seguir realizando operaciones: Si o No')
        
    else:
        print('Por favor, ingrese una operación válida')
        
