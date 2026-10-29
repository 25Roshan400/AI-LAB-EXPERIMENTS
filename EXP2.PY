
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


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
    print("DFS Traversal:", end=" ")
    dfs(graph, start)
else:
    print("Starting vertex not found in the graph.")