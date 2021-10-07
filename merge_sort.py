def merge_sort(arr, num_comapare = 0):
    length = len(arr)
    if (length > 1):
        mid = length//2

        arr1 = arr[:mid]
        arr2 = arr[mid:]

        num_comapare = merge_sort(arr1, num_comapare)
        num_comapare = merge_sort(arr2, num_comapare)

        i = j = m = 0
        while i < len(arr1) and j < len(arr2):
            num_comapare += 1
            if arr1[i] < arr2[j]:
                arr[m] = arr1[i]
                i += 1
                m += 1
            else:
                arr[m] = arr2[j]
                j += 1
                m += 1

        while i < len(arr1):
            arr[m] = arr1[i]
            i += 1
            m += 1
        
        while j < len(arr2):
            arr[m] = arr2[j]
            j += 1
            m += 1
    return num_comapare
