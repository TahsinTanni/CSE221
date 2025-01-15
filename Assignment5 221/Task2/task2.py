class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = {}

        for i in range(1, num_vertices + 1):
            self.graph[i] = []

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def insert_sorted(self, queue, val):
        i = 0
        while i < len(queue) and val >= queue[i]:
            i += 1
        queue.insert(i, val)

    def bfs_topological_sort(self):
        indegree = [0] * (self.num_vertices + 1)

        # Calculate indegree of each node
        for u in self.graph:
            for v in self.graph[u]:
                indegree[v] += 1

        priority_queue = []
        result = []

        # Add nodes with indegree 0 to the priority queue
        for i in range(1, self.num_vertices + 1):
            if indegree[i] == 0:
                self.insert_sorted(priority_queue, i)

        while priority_queue:
            node = priority_queue.pop(0)
            result.append(node)

            for neighbor in self.graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    self.insert_sorted(priority_queue, neighbor)

        return result if len(result) == self.num_vertices else []

# Read input from input.txt
with open("input2_3.txt", "r") as file:
    num_courses, num_prerequisites = map(int, file.readline().split())
    prerequisites = [tuple(map(int, line.split())) for line in file]

graph = Graph(num_courses)
for prereq in prerequisites:
    graph.add_edge(prereq[0], prereq[1])

# Perform topological sorting using BFS
result = graph.bfs_topological_sort()

# Check if the result contains all courses (1 to num_courses)
if result:
    output = " ".join(map(str, result))
else:
    output = "impossible"

# Write the lexicographically shortest path output to the output.txt file
with open("output2_3.txt", "w") as file:
    file.write(output)



