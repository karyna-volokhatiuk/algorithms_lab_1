def insertion_sort(arr):
    length = len(arr)
    num_compare = 0
    for i in range(1, length):
        for j in range(i, 0, -1):
            num_compare += 1
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else:
                break
    return num_compare
