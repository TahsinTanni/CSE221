input_file = open("input1_3.txt", 'r')
output_file = open('output1_3.txt', 'w')
x = int(input_file.readline())
li = []

k = input_file.readlines()
#print(k)

for i in range(x):
    li.append(list(map(int, k[i].split())))# Convert values to integers
#print(li)

# Sort tasks by end times
li.sort(key=lambda task: task[1])

#print(li)
complete = []
complete.append(li[0])
store = li[0][1]
#print(store)

for task in range(1, len(li)):
    start, end = li[task][0], li[task][1]
    if start >= store:
        complete.append(li[task])
        store = end
#return complete
output_file.write(str(len(complete))+'\n')
for e in complete:
    st,en=e
    w=str(st)+' '+str(en)+'\n'
    output_file.write(w)