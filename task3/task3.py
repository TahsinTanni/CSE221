def stableSelectionSort(ids, marks):
    n = len(marks)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if marks[j] > marks[min_idx] or (marks[j] == marks[min_idx] and ids[j] < ids[min_idx]):
                min_idx = j
        if min_idx != i:
            id = ids[min_idx]
            mark = marks[min_idx]
            for k in range(min_idx, i, -1):
                ids[k] = ids[k - 1]
                marks[k] = marks[k - 1]
            ids[i] = id
            marks[i] = mark

with open('input3.txt', 'r') as x:
    N = int(x.readline().strip())
    ids = list(map(int, x.readline().strip().split()))
    marks = list(map(int, x.readline().strip().split()))

stableSelectionSort(ids, marks)

with open('output3.txt', 'w') as x:
    for i in range(N):
        x.write("ID: " + str(ids[i]) + " Mark: " + str(marks[i]) + "\n")

