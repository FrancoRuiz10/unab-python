def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Bandera para detectar si hubo un intercambio
        swapped = False
        for j in range(0, n-i-1):
            # Comparar elementos adyacentes
            if arr[j] > arr[j+1]:
                # Intercambiar si están en el orden equivocado
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # Si no hubo intercambios, la lista ya está ordenada
        if not swapped:
            break
    return arr

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", arr)
sorted_arr = bubble_sort(arr)
print("Lista ordenada:", sorted_arr)
