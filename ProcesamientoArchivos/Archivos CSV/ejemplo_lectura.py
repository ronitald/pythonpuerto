import csv

def leer_archivo(nombre_archivo):
    comidas = []
    with open(nombre_archivo) as archivo:
        lector_csv = csv.DictReader(archivo)
        for fila in lector_csv:
            comidas.append(fila)
    return comidas

nombre_archivo = 'comidas.csv'
comidas = leer_archivo(nombre_archivo)

for comida in comidas:
    print(f'Nombre: {comida["Nombre"]}, Tipo: {comida["Tipo"]}, Precio: {comida["Precio"]}')
