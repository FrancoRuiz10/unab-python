"""
lista1 = [5, 3, 1 , -2, 8, 4, 0, -6]

lista1.sort()
print(lista1)

lista1.sort(reverse=True)
print(lista1)


lista1 = [5, 3, 1 , -2, 8, 4, 0, -6]

indice = 0
print(lista1[indice])

lista1[len(lista1)-1]

for i in range(0, len(lista1)):
    print(i, lista1[i])
    
"""
    
lista2 = [8, 5, -1, 6, 3, 4, -6, 0]


# Ordenamiento burbuja
for j in range(len(lista2)-1, 0, -1):
    for i in range(0, j):
        if lista2[i] < lista2[i+1]:
            lista2[i], lista2[i+1] = lista2[i+1], lista2[i]

print(f"pasada {j} la lista quedo {lista2}")

