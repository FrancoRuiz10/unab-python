# ordenamiento por seleccion

def ordenamiento_por_seleccion(lista_a_ordenar):
    for indice_exterior in range(len(lista_a_ordenar) - 1, 0, -1):
        indice_mayor = 0
        for indice_interior in range(1, indice_exterior + 1):
            if lista_a_ordenar[indice_interior] > lista_a_ordenar[indice_mayor]:
                indice_mayor = indice_interior
        lista_a_ordenar[indice_exterior], lista_a_ordenar[indice_mayor] = lista_a_ordenar[indice_mayor], lista_a_ordenar[indice_exterior]
    
    return lista_a_ordenar


lista4 = [11, -13, 0, 5, 4, 2, 0, -1, 6]

print(ordenamiento_por_seleccion(lista4))

