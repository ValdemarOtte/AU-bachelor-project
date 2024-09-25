### Imports
# Standard library

# Third-party libraries

# Local files


def kp_dp(capacity: int, items: list[dict]) -> list[list]:
    """
    Knapsack Problem - Dynamic Programming

    Args:
        capacity (int): The capacity of the knapsack.
        items (list[dict]): List of items which will be used in the Knapsach Problems.
    
    Returns:
        matrix (list[list]): A matrix with the solutions for the Knapsack Problem.
    """
    matrix: list = []

    for _ in range(capacity + 1):
        matrix.append([0])

    for item in items:
        # For 0 <= d < item["weight"]
        for i in range(item["weight"]):
            matrix[i].append(matrix[i][-1])

        # For item["weight"] <= d <= capacity
        for i in range(item["weight"], capacity + 1):
            if matrix[i - item["weight"]][-2] + item["profit"] > matrix[i][-1]:
                value = matrix[i - item["weight"]][-2] + item["profit"]
            else:
                value = matrix[i][-1]
            matrix[i].append(value)

    return matrix
