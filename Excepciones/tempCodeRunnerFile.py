while True:
    entrada = input('Ingrese el nombre de los aprendices para agregar a la lista:\n(0 para finalizar): ')
    try:
        num = int(entrada)
        if num == 0:
            break
        else:
            agregar_una_vez(Lista_2693630, num)
    except ValueError:
        agregar_una_vez(Lista_2693630, entrada)
Lista_2693630 = [elemento.upper() for elemento in Lista_2693630]
print(f'La lista de los aprendices es: {Lista_2693630}')
print()