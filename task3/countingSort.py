def countingSort(arr):
    counter = [0] * (max(arr) + 1 + abs(min(arr)))

    for num in arr:
        counter[num + abs(min(arr))] += 1

    return [num - abs(min(arr)) for num, count in enumerate(counter) for i in range(count)]