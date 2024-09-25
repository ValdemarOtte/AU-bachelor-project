### Imports
# Standard library

# Third-party libraries

# Local files


def dp(c: int, items: list[dict]) -> list[list]:
    matrix: list = []

    for _ in range(c + 1):
        matrix.append([0])

    for item in items:
        # For 0 <= d < item["weight"]
        for i in range(item["weight"]):
            matrix[i].append(matrix[i][-1])

        # For item["weight"] <= d <= c
        for i in range(item["weight"], c + 1):
            if matrix[i - item["weight"]][-2] + item["profit"] > matrix[i][-1]:
                value = matrix[i - item["weight"]][-2] + item["profit"]
            else:
                value = matrix[i][-1]
            matrix[i].append(value)

    return matrix
