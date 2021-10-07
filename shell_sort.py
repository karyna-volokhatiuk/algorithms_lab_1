def shell_sort(arr):
    length = len(arr)
    num_compare = 0
    h = 1

    while (h < length/3):
        h = 3*h + 1

    while h >= 1:
        for i in range(h, length):
            for j in range(i, h-1, -h):
                num_compare += 1
                if arr[j] < arr[j-h]:
                    temp = arr[j]
                    arr[j] = arr[j-h]
                    arr[j-h] = temp
                else:
                    break
        h //= 3
    return num_compare
