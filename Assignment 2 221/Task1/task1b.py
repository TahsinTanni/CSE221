# time complexity is O(n)
with open("input1b.txt", "r") as x:
    a, b = map(int, x.readline().split())
    lst2 = list(map(int, x.readline().split()))

idx1 = -1
idx2 = -1
lst3 = sorted(set(lst2)) #sorted list

i = 0
j = len(lst3) - 1

while i < j:
    if lst3[i] + lst3[j] == b:
        idx1 = lst2.index(lst3[i]) #finding index
        idx2 = lst2.index(lst3[j])
        break
    elif lst3[i] + lst3[j] < b:
        i += 1
    else:
        j -= 1

with open("output1b.txt", "w") as x:
    if idx1 != -1 and idx2 != -1:
        if idx1 < idx2:
            x.write(f"{idx1 + 1} {idx2 + 1}")
        else:
            x.write(f"{idx2 + 1} {idx1 + 1}")
    else:
        x.write("IMPOSSIBLE")
