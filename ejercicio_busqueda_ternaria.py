def busqueda_ternaria(arr, l, r, x):
    if r >= l:
        # Dividir el rango actual en tres partes
        tercio1 = l + (r - l) // 3
        tercio2 = r - (r - l) // 3

        # Comprobar si x está en alguno de los puntos de división
        if arr[tercio1] == x:
            return tercio1
        if arr[tercio2] == x:
            return tercio2

        # Determinar en qué tercio puede estar x
        if x < arr[tercio1]:
            # El elemento está en el primer tercio
            return busqueda_ternaria(arr, l, tercio1 - 1, x)
        elif x > arr[tercio2]:
            # El elemento está en el tercer tercio
            return busqueda_ternaria(arr, tercio2 + 1, r, x)
        else:
            # El elemento está en el segundo tercio
            return busqueda_ternaria(arr, tercio1 + 1, tercio2 - 1, x)

    # El elemento no está presente en la lista
    return -1

# Ejemplo de uso
arr = [2, 3, 4, 10, 40, 44, 55, 60]
x = 10
resultado = busqueda_ternaria(arr, 0, len(arr) - 1, x)

if resultado != -1:
    print(f"El elemento {x} está presente en el índice {resultado}.")
else:
    print(f"El elemento {x} no está presente en la lista.")
