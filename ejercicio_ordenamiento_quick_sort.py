def quick_sort(arr):
    def median_of_three(arr, low, high):
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        # Mediana es ahora arr[mid]
        arr[mid], arr[high - 1] = arr[high - 1], arr[mid]
        return arr[high - 1]

    def quick_sort_recursive(arr, low, high):
        if low < high:
            pivot = median_of_three(arr, low, high)
            i, j = low, high - 1

            while True:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1

            arr[i], arr[high - 1] = arr[high - 1], arr[i]
            quick_sort_recursive(arr, low, i - 1)
            quick_sort_recursive(arr, i + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)
    return arr

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", arr)
sorted_arr = quick_sort(arr)
print("Lista ordenada:", sorted_arr)
