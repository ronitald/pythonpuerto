def diccionarioExcepciones():
    diccionario = {}
    try:
        while True:
            clave = input('Ingrese una clave para añadir al diccionario: ')
            if clave in diccionario:
                print('No se puede agregar una clave duplicada. Intente nuevamente.')
                print()
            else:
                valor = input('Ingrese el valor de la clave. \nOprima "Ctrl + C" para finalizar: ')
                diccionario[clave] = valor
    except KeyboardInterrupt:
        print('\nHa terminado de agregar elementos al diccionario.')
    except:
        print('Ha ocurrido un error.')
    print(f'DICCIONARIO: {diccionario}')
    print()

    while True:
        try:
            clave_buscada = input('Ingrese la clave que desea buscar en el diccionario: ')
            valor_encontrado = diccionario[clave_buscada]
            print(f'La clave {clave_buscada} tiene el valor {valor_encontrado}.')
            print('--- FIN ---')
            break 
        except KeyError:
            print('La clave que desea encontrar no existe.')
        except:
            print('Ha ocurrido un error.')

diccionarioExcepciones()
