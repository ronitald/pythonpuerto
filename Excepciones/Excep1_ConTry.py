def diviciones():
    while True:
        try:
            num1 = int(input('Ingrese el numero dividendo: '))
            num2 = int(input('Ingrese el numero divisor: '))
            if num1 / num2 or num2 / num1:
                resultado = num1/num2
            print(f'El resultado de la division es: {resultado}')
        except ZeroDivisionError: 
            print('No se puede dividir entre 0 \n Intentalo denuevo. ')
        except ValueError:
            print('Valor invalido. ')
        except:
            print('Ah ocurrido un error. ')
        print()

diviciones()