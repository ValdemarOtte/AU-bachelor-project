### Imports
# Standard library

# Third-party libraries

# Local files
from au_bachelor_project.dp import dp
from au_bachelor_project.utils.functions import print_matrix


def main(c: int, items: list[dict]) -> None:
    """
    Main function for AU Bachelr Project.

    Args:
        c (int): Caaa
        items (list[dict]): List of items which will be used in the Knapsach Problems

    """
    # Simple dynamic programming
    matrix = dp(c, items)

    # Print matrix
    print_matrix(matrix)


if __name__ == "__main__":
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
    main(1, items)
