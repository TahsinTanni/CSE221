with open("input.txt", "r") as x:
    len1 = int(x.readline())
    lst1 = list(map(int, x.readline().strip().split()))
    len2 = int(x.readline())
    lst2 = list(map(int, x.readline().strip().split()))
    sort_lst = sorted(lst1 + lst2)

with open("output.txt", "w") as x:
    t = ""
    for i in range(len(sort_lst)):
        t += str(sort_lst[i]) + " "
    x.write(t)


#time complexity o(nlogn)