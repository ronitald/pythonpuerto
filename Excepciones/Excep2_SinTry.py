import math

while True:
    a = input('Ingrese el valor de A: ')
    b = input('Ingrese el valor de B: ')
    c = input('Ingrese el valor de C: ')

    if not a.isdigit() or not b.isdigit() or not c.isdigit():
        print('¡Valor invalido! Ingrese un valor numerico.')
    else:
        a, b, c = int(a), int(b), int(c)
        resultado = b ** 2 - 4 * a * c

        if resultado < 0:
            print('No existen raices reales para la funcion cuadratica.')
        else:
            positivos = (-b + math.sqrt(resultado)) / (2 * a)
            negativos = (-b - math.sqrt(resultado)) / (2 * a)
            print(f'Las raices de la funcion son:\nPositivos = {positivos} \nNegativos = {negativos}')