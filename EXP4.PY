import heapq

def astar(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while priority_queue:
        f, g, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, g

        if node in visited:
            continue

        visited.add(node)

        for neighbour, cost in graph[node]:
            if neighbour not in visited:
                new_g = g + cost
                new_f = new_g + heuristic[neighbour]

                heapq.heappush(
                    priority_queue,
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    return None, float("inf")


graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 4), ('E', 2)],
    'C': [('A', 3), ('F', 2)],
    'D': [('B', 4)],
    'E': [('B', 2), ('G', 3)],
    'F': [('C', 2), ('G', 2)],
    'G': [('E', 3), ('F', 2)]
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 2,
    'G': 0
}

start = input("Enter the start node: ").upper()
goal = input("Enter the goal node: ").upper()

if start in graph and goal in graph:
    path, cost = astar(graph, heuristic, start, goal)

    if path:
        print("Shortest path:", " -> ".join(path))
        print("Total cost:", cost)
    else:
        print("No path found.")
else:
    print("Invalid start or goal node.")