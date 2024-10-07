def eliminar_duplicados(lista):
    elementos_vistos = set()  # Conjunto para rastrear elementos únicos
    lista_sin_duplicados = []  # Lista para almacenar los elementos sin duplicados
    
    for elemento in lista:
        if elemento not in elementos_vistos:
            lista_sin_duplicados.append(elemento)  # Agrega el elemento a la lista si no ha sido visto
            elementos_vistos.add(elemento)  # Añade el elemento al conjunto para marcarlo como visto
    
    return lista_sin_duplicados

# Ejemplo de uso:
mi_lista = [1, 2, 2, 3, 4, 4, 5, 6, 6]
resultado = eliminar_duplicados(mi_lista)
print(resultado)  # [1, 2, 3, 4, 5, 6]
