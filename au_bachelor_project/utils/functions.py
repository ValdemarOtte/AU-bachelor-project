### Imports
# Standard library
# Third-party libraries
# Local files
 

def print_matrix(matrix: list[list]) -> None:
    """
    Print the matrix to a more reable version.

    Args:
        matrix (list[list]): A matrix which will be printed.
    """
    # Find the longest string in the matrix
    max_value: int = max([max(row) for row in matrix])
    string_lenght: int = len(str(max_value)) + 2

    # Transform matrix to a matrix with strings
    matrix = [[f"{str(x):>{string_lenght}}" for x in row] for row in matrix]

    # Append numbering to beside matrix
    for i, row in enumerate(matrix):
        row.insert(0, f"{i:>2} |")

    top_row: list[str] = ["c\j|"]
    # Append numbering to "top_row"
    for i in range(len(matrix[0]) - 1):
        top_row.append(f"{i:>{string_lenght}}")

    # Add dotted line
    totalt_lenght: int = len("".join(top_row))
    rrow: list[str] = ["---+" + "-"*(totalt_lenght - 4)]

    # Append top_row and d
    matrix.insert(0, rrow)
    matrix.insert(0, top_row)

    for row in matrix:
        print("".join(row))
