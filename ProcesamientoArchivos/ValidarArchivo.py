from os import strerror

def validar_archivo(NombreArchivo):
    try:
        archivo = open(NombreArchivo)
        print('El archivo ya existe.')
        lineas = archivo.readlines()
        ContarLineas = len(lineas)
        print(f'En el archivo hay {ContarLineas} lineas.')
        archivo.close()
    except FileNotFoundError:
        print('El archivo no existe.')
        try:
            archivo = open(NombreArchivo, "w")
            print(f'!Archivo creado con exito!: {NombreArchivo}')
            archivo.close()
        except IOError as e:
            print(f'Se produjo un error de: {strerror(e.errno)}')

nombre_archivo = 'Prueba.txt'
validar_archivo(nombre_archivo)