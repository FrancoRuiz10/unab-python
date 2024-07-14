# Ordenamiento por insercion

def ordenamineto_por_insercion(lista_desordenada):
    for i in range(1, len(lista_desordenada)):
        j = i-1
        siguiente_elemento = lista_desordenada[i]
        
        while j >= 0 and lista_desordenada[j] > siguiente_elemento: # cambiando el simbolo > por < se elije de forma ascendente o descendente
            lista_desordenada[j + 1] = lista_desordenada[j]
            j -= 1
        
        lista_desordenada[j+1] = siguiente_elemento
        
    return lista_desordenada


lista3 = [-6, 5, 3, 1, 8, 7, 11, 0]

ordenamineto_por_insercion(lista3)

print(lista3)