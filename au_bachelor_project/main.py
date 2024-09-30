### Imports
# Standard library

# Third-party libraries

# Local files
from au_bachelor_project.kp_dp import kp_dp
from au_bachelor_project.utils.functions import print_matrix


def main(capacity: int, items: list[dict]) -> None:
    """
    Main function for AU Bachelr Project.

    Args:
        capacity (int): The capacity of the knapsack.
        items (list[dict]): List of items which will be used in the Knapsach Problems.

    """
    # Knapsack Problem - Dynamic Programming
    matrix = kp_dp(capacity, items)

    # Print matrix
    print_matrix(matrix)


if __name__ == "__main__":
    capacity: int = 10
    d_1_items: list[dict] = [
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
    main(capacity, d_1_items)
