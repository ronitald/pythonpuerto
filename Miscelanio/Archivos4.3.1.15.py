# Se importa la funcion strerror desde el modulo os. 
# Esta funcion solo espera un argumento: un numero de error.
from os import strerror

# Inicializa 26 contadores para cada letra. 
# Se crea un diccionario por comprension, cada letra esta esta establecida por un contador en 0.
# Se utiliza para contar cuantas veces aparece cada letra en el archivo.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}

# Inicializa un contador para caracteres numericos...
# Inicializa otro para caracteres especiales.
numeros_counter = 0
caracteres_counter = 0

# Se definen los caracteres especiales.
caracteres_especiales = "{[/<¡(`^)%;>'}-@#$*,_!+|¿:].?"

# Se Solicita al usuario que ingrese el nombre del archivo a analizar.
# Se almacena en la variable de file_name.
file_name = input("Ingresa el nombre del archivo a analizar: ")

# Se crea un Try-Except
try:
    # Se intenta abrir el archivo en lectura de texto.
    # Se asigna a la variable file.

    with open(file_name, "rt") as file:

        # Itera cada linea del archivo.
        # Se asigna a la variable line.
        for line in file:

            # Itera nuevamente pero ahora cada caracter en la linea.
            # Se asigna a la variable char.
            for char in line:
                
                # El metodo isalpha verifica si el caracter es una letra.
                if char.isalpha():

                    # El metodo lower cambia el caracter a minusculas.
                    # Se actualiza el contador en uno.
                    counters[char.lower()] += 1

                # El metodo isdigit verifica si el caracter es un numero.
                elif char.isdigit():
                    numeros_counter += 1

                # Si no es una letra ni un numero...
                # Considerarlo como caracter especial.
                elif char in caracteres_especiales:
                    caracteres_counter += 1

        # Se cierra el archivo.
        file.close()

    # Imprime cada letra que aparecio en el archivo...
    # Imprime cuantas veces aparececada letra.
    for char, count in counters.items():
        if count > 0:
            print(char, '->', count)

    # Imprime cuanto numeros aparecen en el archivo.
    # Imprime cuantos caracteres especiales aparecen en el archivo.
    print(f'Caracteres numericos -> {numeros_counter}')
    print(f'Caracteres especiales -> {caracteres_counter}')

# Imprime los posibles errores que pueden suceder.
# Se asigana "e" a IOError para que sea imprimido el mensaje de error que ha sucedido.
except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))

#C:\Users\Ronald Puerto\Pictures\Prueba.txt