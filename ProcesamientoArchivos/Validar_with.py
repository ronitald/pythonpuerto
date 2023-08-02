from os import strerror

def validar_archivo(NombreArchivo):
    try:
        with open(NombreArchivo, 'r'):
            print('El archivo ya existe.')
            lineas = nombre_archivo.readlines()
            ContarLineas = len(lineas)
            print(f'En el archivo hay {ContarLineas} líneas.')
    except FileNotFoundError:
        print('El archivo no existe.')
        try:
            with open(NombreArchivo, 'w'):
                print(f'¡Archivo creado con éxito!: {NombreArchivo}')
        except IOError as e:
            print(f'Se produjo un error de: {strerror(e.errno)}')

nombre_archivo = 'Prueba.txt'
validar_archivo(nombre_archivo)
