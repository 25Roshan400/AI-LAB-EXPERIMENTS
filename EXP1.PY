from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# Input graph
graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbours = input(
        f"Enter neighbours of {vertex} separated by spaces: "
    ).split()
    graph[vertex] = neighbours

start = input("Enter starting vertex: ")

if start in graph:
    bfs(graph, start)
else:
    print("Starting vertex not found in the graph.")
