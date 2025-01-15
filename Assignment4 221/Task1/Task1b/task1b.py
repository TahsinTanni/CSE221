# Read input from the file
with open("input1b.txt", "r") as input_file:
    m, n = input_file.readline().strip().split()
    m, n = int(m), int(n)  # splitting the vertices and edges
    arr = [0] * (m + 1)  # making of adjacency matrix
    for i in range(m + 1):
        arr[i] = [0] * (m + 1)

    # Populate the adjacency matrix
    for t in range(n):
        n2 = input_file.readline().strip().split()
        i, j, k = int(n2[0]), int(n2[1]), int(n2[2])
        arr[i][j] = k  # Giving the weight

# Separate the code to create the adjacency list
adj_list = {i: [] for i in range(m + 1)}

for i in range(m + 1):
    for j in range(m + 1):
        if arr[i][j] != 0:
            adj_list[i].append((j, arr[i][j]))

# Write the adjacency list to the output file
with open("output1b.txt", "w") as output_file:
    for vertex in range(m + 1):
        output_file.write(str(vertex) + " : ")
        for end, weight in adj_list[vertex]:
            output_file.write(f"({end},{weight}) ")
        output_file.write("\n")


