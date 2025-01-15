with open("input2b.txt", "r") as x:
    len1 = int(x.readline())
    lst1 = list(map(int, x.readline().strip().split()))
    len2 = int(x.readline())
    lst2 = list(map(int, x.readline().strip().split()))
    sort_lst = [0] * (len1 + len2)
    i = j = k = 0

    while j < len1 and k < len2:
        if int(lst1[j]) <= int(lst2[k]):
            sort_lst[i] = int(lst1[j])
            j += 1
        else:
            sort_lst[i] = int(lst2[k])
            k += 1
        i += 1

    while j < len1:
        sort_lst[i] = int(lst1[j])
        j += 1
        i += 1

    while k < len2:
        sort_lst[i] = int(lst2[k])
        k += 1
        i += 1

with open("output2b.txt", "w") as x:
    s = ""
    for i in range(len(sort_lst)):
        s += str(sort_lst[i]) + " "
    x.write(s)
