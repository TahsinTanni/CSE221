import math
from queue import PriorityQueue

input_file = open("input3_2.txt",'r')
output_file= open("output3_2.txt",'w')
n , m = list(map(int,input_file.readline().split(' ')))


def Graph(n, m):
    adjancy_list = [None] * (n + 1)
    for i in range(m):
        e1, e2, e3 = map(int, input_file.readline().split())
        if adjancy_list[e1] is None:
            adjancy_list[e1] = [(str(e2), e3)]
        else:
            adjancy_list[e1].append((str(e2), e3))
    return adjancy_list


def dijkstra(src, graph, danger):
    dis_list = [math.inf] * (n + 1)
    # Create a priority queue, add initial node with its danger level
    q = PriorityQueue()
    q.put((danger, src))

    while not q.empty():
        # Get the smallest danger level node from the queue
        cost, source = q.get()

        # If the current danger level is smaller than stored distance
        if dis_list[int(source)] > cost:
            # Update the stored distance with the current danger level
            dis_list[int(source)] = cost

            # If the node has neighbors
            if graph[int(source)] is not None:
                # Iterate through neighbors and their danger levels
                for neighbour in graph[int(source)]:
                    next_source, up_cost = neighbour
                    # Add neighbor to the queue with updated danger level
                    q.put((up_cost, next_source))
            else:
                pass
        else:
            pass

    # Return the list of minimum distances
    return dis_list


adj_list = Graph(n , m)
val = dijkstra(1 , adj_list , 0)
maximum = -1

for v in range(1,len(val)):
    if val[v] == math.inf:
        output_file.write('Impossible')
        break
    else:
        if maximum <val[v]:
            maximum = val[v]
output_file.write(str(maximum))