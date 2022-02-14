# arr = [6, 1, 3, 4, 2, 7, 5, 8, 10, 9, 0]

def selectionSort(arr, n):  #arr is the array and n is the size of the array
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubbleSort(arr, n):  #arr is the array and n is the size of the array
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertionSort(arr, n):  #arr is the array and n is the size of the array
    for i in range(1, n):
        cur = arr[i]
        j = i - 1
        while arr[j] > cur and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = cur
    return arr
