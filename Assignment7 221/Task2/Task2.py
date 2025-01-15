input_file = open("input2_4.txt", 'r')
output_file = open('output2_4.txt', 'w')

x, y = map(int, input_file.readline().split())

dic = {}
for key in range(1, y + 1):
    dic[key] = []

k = input_file.readlines()
li = []

for i in range(x):
    li.append(list(map(int, k[i].split())))

li.sort(key=lambda task: task[1])
print(li)

count = 0
for task in range(1, len(li)):
    start, end = li[task][0], li[task][1]
    for i in dic:
        if not dic[i]:
            dic[i] = [task]
            store = end
            count += 1
            break
        if dic[i] != [] and li[dic[i][-1]][1] <= start  and li[dic[i][-1]][1] == start:
            dic[i].append(task)
            store = end
            count +=1
            break

output_file.write(str(count+1))

input_file.close()
output_file.close()



















