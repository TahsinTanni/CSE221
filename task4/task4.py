with open("input4.txt", 'r') as x:
    n = int(x.readline())
    li = []
    for i in range(1, n + 1):
        li.append(x.readline().strip())
        #print(li)
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            line1= li[j].split(' ')
            line2 = li[j + 1].split(' ')

            if line1[0] > line2[0]:
                li[j], li[j + 1] = li[j + 1], li[j]
            elif line1[0] == line2[0] and line1[-1]<line2[-1]:
                li[j], li[j + 1] = li[j + 1], li[j]

# Write the sorted lines to the output file
with open('output4.txt', 'w') as x:
    for k in li:
        x.write(k + "\n")




