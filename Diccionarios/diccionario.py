info_personal = {
    'nombre': 'Ronald',
    'edad': 17,
    'ciudad': 'Bogota',
    'profesion': 'Adso'
}

def buscar_clave(key, diccionario):
    if key in diccionario:
        valor = diccionario[key]
        tipo_valor = type(valor)
        if tipo_valor is str:
            tipo_valor = "Cadena"
        else:
            tipo_valor = "Entero"
        return f"La palabra '{key}' está asociada a '{valor}' y es de tipo {tipo_valor}"
    else: 
        return f"La clave '{key}' no está en el diccionario"

clave_buscada = input("Escriba la clave a buscar: ")
print(buscar_clave(clave_buscada, info_personal))
