f1 = open('input1_1.txt', 'r')
f2 = open('output1_1.txt', 'w')
n, m = map(int, f1.readline().strip().split())
adj = []
for i in range(m):
    e1, e2, e3 = map(int, f1.readline().strip().split())
    adj.append([e1, e2, e3])


def modified_merge_sort(array):
    length = len(array)
    if length <= 1:
        return array

    middle = length // 2
    left = modified_merge_sort(array[:middle])
    right = modified_merge_sort(array[middle:])

    merged = []
    while left and right:
        if left[0][2] < right[0][2]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(left)
    merged.extend(right)
    return merged


def find(parents, node):
    if parents[node] != node:
        parents[node] = find(parents, parents[node])
    return parents[node]


def union(parents, rank, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)

    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parents[root_y] = root_x
        else:
            parents[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1


sorted_edges = modified_merge_sort(adj)
parents = list(range(n + 1))
rank = [0] * (n + 1)
total_cost = 0

for edge in sorted_edges:
    if find(parents, edge[0]) != find(parents, edge[1]):
        union(parents, rank, edge[0], edge[1])
        total_cost += edge[2]

f2.write(str(total_cost))

f1.close()
f2.close()
