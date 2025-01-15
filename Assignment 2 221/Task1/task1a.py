#time complexity O(n**2)
with open("input1a.txt", "r") as x:
    y=x.readline().split()
    a=int(y[0])
    b=int(y[1])
    lst1=x.readlines()
    lst2= lst1[0].split(" ")
    idx1 = -1
    idx2 = -1
    for i in range(a):
        for j in range(i+1, a):
            if int(lst2[j]) + int(lst2[i]) == b:
                idx1 = i
                idx2 = j
                #print(x1,x2)
                break
        if idx1 != -1 and idx2 != -1:
            break

with open("output1a.txt", "w") as x:
    if idx1 != -1 and idx2 != -1:
        x.write(f"{idx1 + 1} {idx2 + 1}")
    else:
        x.write("IMPOSSIBLE")