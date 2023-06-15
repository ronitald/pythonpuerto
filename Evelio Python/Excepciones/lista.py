lista = [3, 5, 6, 8, 8, 6, 4, 5, 66, 777, 3, 3, 3, 5, 6, 5]
pos = 0

print('Escribe "fin" para salir. ') 

while True:
    try:
        pos_input = input('Ingresa la posición del elemento que deseas obtener:')

        if pos_input == 'fin':
            break
        
        pos = int(pos_input)
        
        print(f'El valor en la posición {pos} es {lista[pos]}')
        
    except IndexError:
        print('La posición ingresada no existe.')
        
    except ValueError:
        print('El valor ingresado no es válido.')

print('Programa finalizado.')
