arr = map(int, raw_input().strip().split())


def swap(n, m):
    temp = arr[m]
    arr[m] = arr[n]
    arr[n] = temp


def partition(first, last):
    pivot = arr[first]
    i = first + 1
    j = last
    if first == last:
        return last
    while True:
        while i <= last and arr[i] <= pivot:
            i = i + 1
        while j > first and arr[j] > pivot:
            j = j - 1
        if i > j:
            break;
        swap(i, j)
    swap(first, j)
    return j


def qsort(f, l):
    if f < l:
        key = partition(f, l)
        qsort(f, key - 1)
        qsort(key + 1, l)


qsort(0, len(arr) - 1)

print arr
