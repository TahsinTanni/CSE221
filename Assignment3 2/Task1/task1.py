def merge_and_count(left, right):
    result = []
    i = j = inversions = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversions += len(left) - i
    result += left[i:]
    result += right[j:]
    return result, inversions

def mergesort_and_count(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, left_inversions = mergesort_and_count(arr[:mid])
    right, right_inversions = mergesort_and_count(arr[mid:])
    merged,merge_inversions = merge_and_count(left, right)
    return merged,left_inversions + right_inversions + merge_inversions

with open('input1.txt', 'r') as file:
    n = int(file.readline())
    heights = list(map(int, file.readline().split()))

# Perform calculations
inversions = str(mergesort_and_count(heights)[0])

with open('output1.txt', 'w') as file:
    file.write(str(inversions))
