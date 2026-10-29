from itertools import permutations

def tsp(graph, start):
    n = len(graph)
    cities = list(range(n))
    cities.remove(start)

    min_cost = float('inf')
    best_path = None

    for route in permutations(cities):
        path = [start] + list(route) + [start]
        cost = 0

        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost


n = int(input("Enter number of cities: "))

graph = []

print("Enter the distance matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

start = int(input("Enter starting city (0 to {}): ".format(n - 1)))

if 0 <= start < n:
    path, cost = tsp(graph, start)

    print("Shortest route:", " -> ".join(map(str, path)))
    print("Minimum distance:", cost)
else:
    print("Invalid starting city.")