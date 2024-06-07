def countingSort(arr):
    counter = {}

    for num in arr:
        if num in counter.keys():
            counter[num] += 1
        else:
            counter[num] = 1

    return [num for num, count in counter.items() for i in range(count)]