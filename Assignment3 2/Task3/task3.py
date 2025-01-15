def partition(arr, low, high):
    pivot = arr[low]  # Taking the first element as the pivot
    i = low + 1  # Increasing index
    j = high  # Decreasing index
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]  # Partition is complete
    return j


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


with open('input3.txt', 'r') as input_file:
    N = int(input_file.readline())
    numbers = list(map(int, input_file.readline().split()))

quicksort(numbers, 0, N - 1)

with open('output3.txt', 'w') as output_file:
    for i in range(N):
        output_file.write(str(numbers[i]))
        if i != N - 1:
            output_file.write(' ')



