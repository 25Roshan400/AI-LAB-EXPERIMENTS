from collections import deque

def water_jug(capacity1, capacity2, target):
    initial_state = (0, 0)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        (jug1, jug2), path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        current_path = path + [(jug1, jug2)]

        if jug1 == target or jug2 == target:
            print("Solution Found!")
            print("Steps to reach the target:")

            for state in current_path:
                print(state)

            print("Total steps:", len(current_path) - 1)
            return

        next_states = [
            (capacity1, jug2),
            (jug1, capacity2),
            (0, jug2),
            (jug1, 0)
        ]

        transfer = min(jug1, capacity2 - jug2)
        next_states.append((jug1 - transfer, jug2 + transfer))

        transfer = min(jug2, capacity1 - jug1)
        next_states.append((jug1 + transfer, jug2 - transfer))

        for state in next_states:
            if state not in visited:
                queue.append((state, current_path))

    print("No solution exists.")


capacity1 = int(input("Enter capacity of Jug 1: "))
capacity2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

if capacity1 <= 0 or capacity2 <= 0:
    print("Jug capacities must be positive.")
elif target < 0 or target > max(capacity1, capacity2):
    print("Invalid target amount.")
else:
    water_jug(capacity1, capacity2, target)