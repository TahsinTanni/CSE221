#time complexity O(nlogn)
def getmax(arr):
    if len(arr) == 1:
        return float('-inf')
    if len(arr) == 2:
        return arr[0] + arr[1] ** 2
    leftmax = getmax(arr[:len(arr) // 2])
    rightmax = getmax(arr[len(arr) // 2:])
    cross = get_crossmax(arr)
    return max(leftmax, rightmax, cross)

def get_crossmax(arr):
    best_leftnumber = float('-inf')
    for i in range(len(arr) // 2 - 1, -1, -1):
        if abs(arr[i]) > best_leftnumber:
            best_leftnumber = abs(arr[i])
    best_rightnumber = float('-inf')
    for i in range(len(arr) // 2, len(arr)):
        if abs(arr[i]) > best_rightnumber:
            best_rightnumber = abs(arr[i])
    return best_leftnumber + best_rightnumber ** 2

# Read input from file
with open('input2.txt', 'r') as input_file:
    N = int(input_file.readline())
    arr = list(map(int, input_file.readline().split()))

# Call the function to get the maximum value
max_val = getmax(arr)

# Write output to file
with open('output2.txt', 'w') as output_file:
    output_file.write(str(max_val))
