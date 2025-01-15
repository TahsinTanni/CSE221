# Graph representation using adjacency Matrix for directed weighted graph

# Read input from the file
with open("input1a.txt", "r") as input_file:
    m, n = input_file.readline().strip().split()
    m, n = int(m), int(n) # splitting the vertices and edge
    arr = [0] * (m + 1) #making of adjacency matrix
    for i in range(m + 1):
        arr[i] = [0] * (m + 1)

    # Populate the adjacency matrix
    for t in range(n):
        n2 = input_file.readline().strip().split()
        i, j, k = int(n2[0]), int(n2[1]), int(n2[2])
        arr[i][j] = k #Giving the weight

# Write the adjacency matrix to the output file
with open("output1a.txt", "w") as output_file:
    for i in range(m + 1):
        for j in range(m + 1):
            output_file.write(str(arr[i][j]) + " ")
        output_file.write("\n")