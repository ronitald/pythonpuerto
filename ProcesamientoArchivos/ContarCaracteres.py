def contar_caracteres(NombreArchivo):
    try:
        archivo = open(NombreArchivo, 'r')
        contenido = archivo.read()
        NumCaracteres = len(contenido)
        archivo.close()
        print(f'El archivo contiene {NumCaracteres} caracteres.')
    except FileNotFoundError:
        print(f'El archivo {NombreArchivo} no existe.')

nombre_archivo = 'Prueba.txt'
contar_caracteres(nombre_archivo)