def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Reduce el intervalo a la mitad en cada iteración
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Realiza el ordenamiento por inserción con el intervalo actual
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

        gap //= 2  # Reduce el intervalo a la mitad

    return arr

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", arr)
sorted_arr = shell_sort(arr)
print("Lista ordenada:", sorted_arr)
