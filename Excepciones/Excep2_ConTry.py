import math

while True:
    try:
        a = float(input('Ingrese el valor de A: '))
        b = float(input('Ingrese el valor de B: '))
        c = float(input('Ingrese el valor de C: '))
        resultado = b**2 - 4*a*c

        if resultado < 0:
            print('No existen raices reales para la funcion cuadratica.')
        else:
            positivos = (-b + math.sqrt(resultado)) / (2 * a)
            negativos = (-b - math.sqrt(resultado)) / (2 * a)
            print(f'Las raices de la funcion son:\n Positivos = {positivos} \n Negativos = {negativos}')
    except ValueError:
        print('¡Valor invalido! Ingrese un valor numerico.')
    except ZeroDivisionError:
        print("El valor de 'A' no puede ser cero.")
    except:
        print('Ah ocurrido un error.')
