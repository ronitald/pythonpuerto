diccionario = {'pollo': 'chicken', 
               'pato': 'duck', 
               'perro': 'dog',
               'leon': 'lion',
               'jirafa': 'giraffe'}

def animales(d1):
    lista1=[]
    lista2=[]
    for clave,valor in diccionario.items():
        lista1.append({clave})
        lista2.append({valor})
        tuplaEs = tuple(lista1)
        tuplaIn = tuple(lista2)
    return (tuplaEs, tuplaIn)

print()  
tupla1, tupla2= animales(diccionario)
print (f'La tupla con las palabras en español es: {tupla1} ')
print (f'La tupla con las pallabras en ingles es: {tupla2} ')
print()