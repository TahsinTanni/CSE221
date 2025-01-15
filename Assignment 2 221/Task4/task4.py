def findMax(arr, low, high):
    if low == high:
        return arr[low]

    mid = (low + high) // 2

    leftMax = findMax(arr, low, mid)
    rightMax = findMax(arr, mid + 1, high)

    return max(leftMax, rightMax)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    merged_arr= [None] * (len(left) + len(right))
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr[k] = left[i]
            i += 1
        else:
            merged_arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged_arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged_arr[k] = right[j]
        j += 1
        k += 1

    return merged_arr

with open("input4.txt", "r") as x:
    n = int(x.readline())
    arr = list(map(int, x.readline().split()))

sorted_arr = mergeSort(arr)
maxValue = findMax(sorted_arr, 0, len(sorted_arr) - 1)

with open("output4.txt", "w") as x:
    x.write(str(maxValue) + "\n")

#the time complexity here is O(nlogn)
# as the margeSort take O(nlogn) time in the average and worst case.
# Also findMax recursively divide the array into half until one element left and takes O(logn) time.


