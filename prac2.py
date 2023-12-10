from queue import PriorityQueue

num_vertices = 9
# num_vertices = 5
graph = [[] for _ in range(num_vertices)]

heuristic = [10, 7, 3, 5, 2, 4, 6, 4, 1]
# heuristic = [20,24,16,7,0]
def best_first_search(start, goal, num_vertices):
    visited = [False] * num_vertices
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic[start], start))
    min_cost = [float('inf')] * num_vertices
    min_cost[start] = 0  

    while not priority_queue.empty():
        _, current_node = priority_queue.get()

        if visited[current_node]:
            continue

        visited[current_node] = True
        print(current_node, end=" ")

        if current_node == goal:
            break

        for neighbor, neighbor_cost in graph[current_node]:
            if not visited[neighbor]:
                total_cost = min_cost[current_node] + neighbor_cost
                if total_cost < min_cost[neighbor]:
                    min_cost[neighbor] = total_cost
                    priority_queue.put((heuristic[neighbor], neighbor))

    if visited[goal]:
        print("\nGoal reached.")
        print("Minimal Cost:", min_cost[goal])
    else:
        print("\nGoal not reached.")

def add_edge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))


add_edge(0, 1, 4)
add_edge(0, 7, 8)
add_edge(1, 7, 11)
add_edge(1, 2, 8)
add_edge(2, 8, 2)
add_edge(2, 3, 7)
add_edge(2, 5, 4)
add_edge(3, 4, 9)
add_edge(3, 5, 14)
add_edge(4, 5, 10)
add_edge(5, 6, 2)
add_edge(6, 8, 6)
add_edge(6, 7, 1)
add_edge(7, 8, 7)

start_node = 0
goal_node = 4


best_first_search(start_node, goal_node, num_vertices)

# testcase2
# num_vertices = 5
# goal_node = 4
# add_edge(0, 1, 6)
# add_edge(0, 3, 13)
# add_edge(1, 2, 7)
# add_edge(2, 3, 16)
# add_edge(2, 4, 18)
# add_edge(3, 4, 8)
