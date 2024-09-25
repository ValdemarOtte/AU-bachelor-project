def dp(c: int, items: dict) -> None:
    matrix: list = []

    for d in range(c + 1):
        matrix.append([0])

    for i, item in enumerate(items):
        # For 0 <= d < item["weight"]
        for d in range(item["weight"]):
            matrix[d].append(matrix[d][-1])

        # For item["weight"] <= d <= c
        for d in range(item["weight"], c + 1):
            if matrix[d - item["weight"]][-2] + item["profit"] > matrix[d][-1]:
                value = matrix[d - item["weight"]][-2] + item["profit"]
            else:
                value = matrix[d][-1]
            matrix[d].append(value)

    for row in matrix:
        print(row)


items = [
    {
        "profit": 6,
        "weight": 2,
    },
    {
        "profit": 5,
        "weight": 3,
    },
    {
        "profit": 8,
        "weight": 6,
    },
    {
        "profit": 9,
        "weight": 7,
    },
    {
        "profit": 6,
        "weight": 5,
    },
    {
        "profit": 7,
        "weight": 9,
    },
    {
        "profit": 3,
        "weight": 4,
    },
]

