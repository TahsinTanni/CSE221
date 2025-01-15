input_file = open("input3_2.txt", 'r')
output_file = open('output3_2.txt', 'w')

N, K = map(int, input_file.readline().split())

parents = [-1] * (N + 1)  # Initialize each node as its own parent
sizes = [1] * (N + 1)  # Initialize sizes of circles as 1

for _ in range(K):
    A, B = map(int, input_file.readline().split())
    while parents[A] != -1:
        A = parents[A]
        #print(A)
    while parents[B] != -1:
        B = parents[B]
    if A != B:
        if sizes[A] >= sizes[B]: #resize
            parents[B] = A
            sizes[A] += sizes[B]
            output_file.write(str(sizes[A]) + '\n')
        else:
            parents[A] = B
            sizes[B] += sizes[A]
            output_file.write(str(sizes[B]) + '\n')
    else:
        output_file.write(str(sizes[A]) + '\n')

input_file.close()
output_file.close()