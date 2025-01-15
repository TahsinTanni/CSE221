with open('input1a.txt', 'r') as x:
    y=x.readline()
    y1=(x.readlines())
with open("output1a.txt", "w") as x:
    for i in y1:
        if int(i)%2==0:
            x.write(f"{i.strip()} is an even number \n")
        else:
            x.write(f'{i.strip()} is an odd number \n')