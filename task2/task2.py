def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

with open('input2.txt', 'r') as x:
    y = int(x.readline())
    y1 = x.readline().strip().split(',')
    flag = True
    for i in range(len(y1)-1):
        if y1[i] > y1[i+1]:
            flag = False

with open('output2.txt', 'w') as x:
    if flag==True: #if flag is True then it means it is sorted in ascending order for it's best case scenario.
        # For checking there is only one loop which means the time complexity is O(n) in here.
        for i in range(len(y1)):
            x.write(str(y1[i]) + " ")
    else:
        t = bubbleSort(y1)
        for i in range(len(y1)):
            x.write(str(y1[i]) + " ")







