def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    # elif len(arr) == 2:
    #     if arr[0] < arr[1]:
    #         return arr
    #     else:
    #         return [arr[1], arr[0]]

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
