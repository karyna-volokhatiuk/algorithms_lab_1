def selection_sort(arr):
    length = len(arr)
    num_compare = 0
    for i in range(length):
        min = i
        for j in range(i+1, length):
            if arr[j] < arr[min]:
                min = j
            num_compare += 1
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    return num_compare
