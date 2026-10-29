def alpha_beta(node, depth, alpha, beta, maximizing):

    # Leaf node reached
    if depth == 0 or not isinstance(node, list):
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(
                value,
                alpha_beta(child, depth - 1,
                           alpha, beta, False)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(
                value,
                alpha_beta(child, depth - 1,
                           alpha, beta, True)
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


# Game tree from the practical
tree = [
    [3, 5],
    [6, 9],
    [1, 2],
    [0, -1]
]

result = alpha_beta(
    tree, 2,
    float('-inf'),
    float('inf'),
    True
)

print("Optimal value:", result)