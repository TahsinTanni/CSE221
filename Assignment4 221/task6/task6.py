def BFS(graph, x, y):
    row = len(graph)
    column = len(graph[0])
    if graph[x][y] == 2:
        graph[x][y] += 2
    array = [(x, y, 0)]

    while array:
        r, c, d = array.pop(0)

        for nr, nc in ((r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)):
            if 0 <= nr < row and 0 <= nc < column and (graph[nr][nc] == 1 or graph[nr][nc] == 2):
                graph[nr][nc] += 2
                array.append((nr, nc, d + 1))

    return graph

with open('input6.txt', 'r') as input_file, open('output6.txt', 'w') as output_file:
    row, column = map(int, input_file.readline().split())
    main_list = []

    for _ in range(row):
        line = input_file.readline().split()
        main_list.append([1 if char == '.' else 2 if char == 'D' else 0 for string in line for char in string])

    full_list = BFS(main_list, 0, 0)

    count = sum(row.count(4) for row in full_list)
    output_file.write(str(count))
