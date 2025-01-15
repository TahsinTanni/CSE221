class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (n + 2)
        queue = []

        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            output_file.write(str(s) + ' ')

            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Read input from the file
with open("input2.txt", "r") as input_file:
    a = input_file.readlines()
    a1 = a[0].split(' ')
    m, n = int(a1[0]), int(a1[1])

    g = Graph()
    for i in range(1, m + 1):
        g.graph[i] = []

    for i1 in range(1, n + 1):
        n2 = a[i1].split(' ')
        i, j = int(n2[0]), int(n2[1])
        g.addEdge(i, j)
        g.addEdge(j, i)

# Write the BFS traversal to the output file
with open("output2.txt", "w") as output_file:
    g.BFS(1)



