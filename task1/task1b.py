with open('input1b.txt', 'r') as x:
    y = x.readline()
    y1 = x.readlines()
    #print(y)
with open('output1b.txt', 'w') as x:
    for i in y1:
        lst = i.split(' ')
        if lst[2] == '+':
            t = int(lst[1]) + int(lst[3])
        elif lst[2] == "-":
            t = int(lst[1]) - int(lst[3])
        elif lst[2] == "*":
            t = int(lst[1]) * int(lst[3])
        else:
            t = int(lst[1]) / int(lst[3])
        x.write(f"The result of {lst[1].strip()} {lst[2].strip()} {lst[3].strip()} is {t} \n")
