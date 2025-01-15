#task1a
#topological sort using DFS
dict = {}

with open("input1a_2.txt","r") as f:
    with open("output1a_2.txt", "w") as f1:
        n1 = f.readline().strip().split()
        m , n = int(n1[0]), int(n1[1])
        for i in range(1,m+1):
          dict[i] = []

        class Graph:
          def __init__(self):
            self.graph = dict
            self.c=0
            self.end=[]*(100)
            self.visited = set()
            self.flag=False

          def addEdge(self, u, v):
            self.graph[u].append(v)

          def DFSUtil(self, v ,visited):
            self.visited.add(v)
            # f1.write(str(v)+" ")
            # print(v)
            for i in self.graph[v]:
              if i not in self.visited:
                self.DFSUtil(i,self.visited)
              elif i in self.visited and i not in self.end:
                  self.flag=True
                  # print(self.flag)

            self.c+=1
            self.end+=[v]

          def DFS(self, v):

            self.DFSUtil(v, self.visited)
        g = Graph()
        for i1 in range(n):
          n2 = f.readline().strip().split()
          i,j = int(n2[0]), int(n2[1])
          g.addEdge(i,j)
        # for i in g.graph.values():
        #     i.sort()

        g.DFS(1)
        for i in range(1,m+1):
            if i not in g.visited:
                g.DFS(i)
        if g.flag:
            f1.write("IMPOSSIBLE")
        else:
            g.end.reverse()
            for i in g.end:
                f1.write(str(i)+" ")



