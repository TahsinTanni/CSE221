dict = {}
with open("input3_3.txt", "r") as input_file:
    with open("output3_3.txt", "w") as output_file:
        n1 = input_file.readline().strip().split()
        m, n = int(n1[0]), int(n1[1])
        for i in range(1, m + 1):
            dict[i] = []

        class Graph:
            def __init__(self, m):
                self.graph = {}
                for i in range(1, m + 1):
                    self.graph[i] = []
                self.stack = []

            def addEdge(self, u, v):
                self.graph[u].append(v)

            def DFS1(self, v, visited):
                visited.add(v)
                output_file.write(str(v) + " ")
                #print(v)
                for i in self.graph[v]:
                    if i not in visited:
                        self.DFS1(i, visited)
                self.stack.append(v)

            def transpose(self):
                gg = Graph(len(g.graph))
                for i in self.graph:
                    for j in self.graph[i]:
                        gg.addEdge(j, i)
                return gg

            def DFS2(self, v, visited2):
                visited2[v] = True
                #print(v, end=" ")
                for i in self.graph[v]:
                    if not visited2[i]:
                        self.DFS2(i, visited2)

            def DFS(self, v):
                visited = set()
                self.DFS1(v, visited)

        g = Graph(m)
        for i1 in range(n):
            n2 = input_file.readline().strip().split()
            i, j = int(n2[0]), int(n2[1])
            g.addEdge(i, j)

        g.DFS(1)
        #print(g.stack)
        trans = g.transpose()
        #print(trans.graph)

        visited2 = [False] * (len(g.graph) + 1)
        while g.stack:
            i = g.stack.pop()
            if not visited2[i]:
                trans.DFS2(i, visited2)
                #print()








