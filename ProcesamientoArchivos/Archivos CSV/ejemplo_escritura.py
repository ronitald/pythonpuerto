import csv

comidas = [
    ['Pizza', 'Carnes', 8.000],
    ['Arepa', 'Pollo', 5.000],
    ['Dulces', 'Trululu', 2.000]
]

nombre_archivo = 'comidas.csv'

with open(nombre_archivo, "w") as file:
    writer = csv.writer(file)

    # Escribir el encabezado
    writer.writerow(['Nombre', 'Tipo', 'Precio'])

    # Escribir los datos de las comidas
    writer.writerows(comidas)

print(f'El archivo {nombre_archivo} se creo correctamente.')