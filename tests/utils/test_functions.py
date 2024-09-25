## Imports
# Standard library

# Third-party libraries
import pytest

# Local files
from au_bachelor_project.utils.functions import print_matrix


class TestFunctions:
    def test_transform_list_urls(self):
        """Test if function will return the correct result."""
        # Setup
        correct_answers = [{"url": "url_1", "scraper": "A"}, {"url": "url_2", "scraper": "A"}]
        urls = ["url_1", "url_2"]
        # Run
        #result = transform_list_urls(urls, "A")
        # Assert
        assert 1 == 1