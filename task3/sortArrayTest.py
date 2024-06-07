import time
import random
import quickSort as qs
import mergeSort as ms


def timeSortArray(sortFunction):
    time1 = time.time()
    for i in range(1000):
        arr = list(random.sample(range(-10000, 10000), 100))
        sortFunction(arr)
    return (time.time() - time1) / 1000


def etalonTimeSortArray():
    time1 = time.time()
    for i in range(1000):
        arr = list(random.sample(range(-10000, 10000), 100))
        arr.sort()
    return (time.time() - time1) / 1000


def testCorrectSortArray(sortFunction):
    for i in range(100):
        arr = list(random.sample(range(-10000, 10000), 100))
        sortedArray = sortFunction(arr)
        arr.sort()
        if sortedArray != arr:
            return False
    arr = list(range(-100, 100))
    sortedArray = sortFunction(arr)
    if sortedArray != arr:
        return False
    return True


if __name__ == '__main__':
    print(f'Эталонное время, стандартной функции сортировки: {etalonTimeSortArray():.2e}')
    print(f'Quick sort работает корректно'
          if testCorrectSortArray(qs.quickSort)
          else f'Quick sort работает некорректно')
    print(f'Время выполнения Quick sort: {timeSortArray(qs.quickSort):.2e}')
    print(f'Merge sort работает корректно'
          if testCorrectSortArray(ms.mergeSort)
          else f'Merge sort работает некорректно')
    print(f'Время выполнения Merge sort: {timeSortArray(ms.mergeSort):.2e}')
