def listasExcepciones():
    lista = []
    try:
        while True:
            elemento = input('Ingrese un elemento para añadir a la lista. \nOprima "Ctrl + C" para finalizar: ')
            if elemento in lista:
                print('No se puede agregar un elemento duplicado. Intente nuevamente.')
                print()
            else:
                lista.append(elemento)
    except ValueError:
        print('No se ha podido ingresar el elemento a la lista. ')
    except KeyboardInterrupt:
        print('\nHa terminado de agregar elementos a la lista. ')
    except:
        print('Ha ocurrido un error. ')
    print(f'LISTA: {lista}')
    print()

    while True:
        try:
            posicion = int(input('Ingrese la posicion que desea buscar en la lista: '))
            elemento = lista[posicion]
            print(f'En la posición {posicion} se encuentra el elemento {elemento}.')
            print('--- FIN ---')
            break
        except IndexError:
            print('La posición que desea encontrar no existe.')
        except ValueError:
            print('Ingrese un valor entero valido.')
        except:
            print('Ah ocurrido un error.')

listasExcepciones()