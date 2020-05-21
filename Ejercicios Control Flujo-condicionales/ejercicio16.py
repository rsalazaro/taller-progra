
lado1 = float(input('Ingreese lado 1: '))
if lado1 > 0:
    lado2 = float(input('Ingreese lado 2: '))
    if lado2 > 0:
        lado3 = float(input('Ingreese lado 3: '))
        if lado3 > 0:
            if lado1 > lado2:
                if lado1 > lado3:
                    mayor = lado1
                else:
                    mayor = lado3
            else:
                if lado2 > lado3:
                    mayor = lado2
                else:
                    mayor = lado3

            if (lado1 + lado2 + lado3) - mayor > mayor:
                # Indicar tipo de triángulo
                if lado1 == lado2 and lado1 == lado3:
                    print('Triángulo equilatero')
                elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
                    print('Triángulo isosceles')
                else:
                    print('Triángulo escaleno')
            else:
                print('No es triángulo')
        else:
            print('Lado 3 no válido')
    else:
        print('Lado 2 no válido')
else:
    print('Lado 1 no válido')

