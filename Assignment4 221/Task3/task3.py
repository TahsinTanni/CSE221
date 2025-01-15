def dfsTraversal(graph, visited, start, output_file):
    visited[start] = True
    output_file.write(str(start) + ' ')
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfsTraversal(graph, visited, neighbor, output_file)

# Read input from the file
with open("input3.txt", "r") as input_file:
    n, m = input_file.readline().strip().split()
    n, m = int(n), int(m)  # splitting the vertices and edges
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        u, v = input_file.readline().strip().split()
        u, v = int(u), int(v)
        graph[u].append(v)
        graph[v].append(u)

visited = [False] * (n + 1)

# Write the DFS traversal to the output file
with open("output3.txt", "w") as output_file:
    dfsTraversal(graph, visited, 1, output_file)
