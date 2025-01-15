def merge(left, right):
    arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        elif left[i] > right[j]:
            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            arr.append(right[j])
            i += 1
            j += 1
    while i < len(left):
        arr.append(left[i])
        i += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
    return arr

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

with open("input3.txt", "r") as x:
    n = int(x.readline())
    arr = list(map(int, x.readline().split()))

sorted_arr = mergeSort(arr)

with open("output3.txt", "w") as x:
    for i in range(len(sorted_arr)):
        x.write(str(sorted_arr[i]))
        if i != len(sorted_arr) - 1:
            x.write(" ")
    x.write("\n")







