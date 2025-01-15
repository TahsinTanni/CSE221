def partition(arr, low, high):
    pivot = arr[low]  # Taking the first element as the pivot
    i = low
    for j in range(low + 1, high + 1):
        if arr[j] < pivot: #current element smaller then pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[i] = arr[i], arr[low]
    return i #index of pivot


def findKthSmallest(arr, k):
    low = 0
    high = len(arr) - 1
    while True:
        pivot_index = partition(arr, low, high)
        if pivot_index == k - 1:
            return arr[pivot_index] #got smallest
        elif pivot_index < k - 1:
            low = pivot_index + 1
        else:
            high = pivot_index - 1


with open('input4.txt', 'r') as input_file:
    N = int(input_file.readline())
    numbers = list(map(int, input_file.readline().split()))
    Q = int(input_file.readline())
    queries = [int(input_file.readline()) for i in range(Q)]

with open('output4.txt', 'w') as output_file:
    for k in queries:
        kth = findKthSmallest(numbers, k)
        output_file.write(str(kth) + '\n')

