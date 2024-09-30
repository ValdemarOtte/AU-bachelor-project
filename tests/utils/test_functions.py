## Imports
# Standard library

# Third-party libraries
from _pytest.capture import CaptureFixture

# Local files
from au_bachelor_project.utils.functions import print_matrix


class TestFunctions:
    def test_print_matrix(self, capsys: CaptureFixture):
        """Test if function will return the correct result."""
        # Setup
        result: str = "c\\j|  0  1\n---+------\n 0 |  1  2\n 1 |  3  4\n"
        matrix = [[1, 2], [3, 4]]

        # Run
        print_matrix(matrix)
        captured = capsys.readouterr()

        # Assert
        assert captured.out == result
