def objective_function(x):
    return 10 - (x - 1) ** 2

def hill_climbing(start, step_size, max_iterations):
    current = start

    for i in range(max_iterations):
        left = current - step_size
        right = current + step_size

        current_value = objective_function(current)
        left_value = objective_function(left)
        right_value = objective_function(right)

        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break

    return current, objective_function(current)


start = float(input("Enter the starting point: "))
step_size = float(input("Enter step size: "))
max_iterations = int(input("Enter maximum iterations: "))

best_position, best_value = hill_climbing(
    start, step_size, max_iterations
)

print("Best position:", best_position)
print("Maximum value:", best_value)