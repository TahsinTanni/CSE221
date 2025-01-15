input_file = open('input4.txt', 'r')
output_file = open('output4.txt', 'w')

n, m = map(int, input_file.readline().strip().split())
n = n + 1
adjancy_list = {}
c = []

for i in range(n):
    adjancy_list[i] = []
# print(adjancy_list)

for j in range(m):
    e1, e2 = map(int, input_file.readline().strip().split())
    adjancy_list[e1].append((e2))
    adjancy_list[e2].append((e1))
    c += [e1]

# print(adjancy_list)

color = {}
parent = {}

for elem in adjancy_list.keys():
    color[elem] = 'W'
    parent[elem] = None


def DFS(elem, color, parent):
    color[elem] = 'G'
    for v in adjancy_list[elem]:
        if color[elem] == "W":
            cycle = DFS(elem, color, parent)
            if cycle == True:
                return True
        elif color[v] == 'G':
            return True
    color[elem] = 'B'
    return False


flag = False
for elem in adjancy_list.keys():
    if color[elem] == 'W':
        flag = DFS(elem, color, parent)
        if flag == True:
            break

if flag == True:
    output_file.write('YES')
else:
    output_file.write('NO')
