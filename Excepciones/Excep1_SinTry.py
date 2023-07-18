while True:
    num1 = int(input('Ingrese el número dividendo: '))
    num2 = int(input('Ingrese el número divisor: '))
    
    if num2 != 0:
        resultado = num1 / num2
        print(f'El resultado de la división es {resultado}')
    else:
        print('No se puede dividir entre 0. Intenta de nuevo.')
    print()
