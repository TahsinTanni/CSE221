class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (n + 2)
        queue = []
        queue.append(s)
        parent[s] = -1
        visited[s] = True
        while queue:
            s = queue.pop(0)
            for i in self.graph[s]:
                if not visited[i]:
                    parent[i] = s
                    queue.append(i)
                    visited[i] = True


with open('input5.txt', 'r') as op, open('output5.txt', 'w') as opw:
    a = op.readlines()
    a1 = a[0].split(' ')
    m, n, pa = int(a1[0]), int(a1[1]), int(a1[2])

    parent = [0] * (n + 2)
    g = Graph()
    for i in range(1, m + 1):
        g.graph[i] = []

    for i1 in range(1, n + 1):
        n2 = a[i1].split(' ')
        i, j = int(n2[0]), int(n2[1])
        g.addEdge(i, j)
        g.addEdge(j, i)

    g.BFS(1)

    path = []
    temp = pa
    while temp != -1:
        path.append(temp)
        temp = parent[temp]

    path.reverse()

    p = ""
    for i in path:
        p += str(i) + " "

    opw.write(f"Time: {len(path) - 1}\nShortest Path: {p}")
