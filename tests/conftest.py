"""
This file contains pytest fixtures that can be reused across multiple test files.
Fixtures defined here are automatically available to all test functions.
"""

import pytest

# Example of a fixture that could be used in tests
@pytest.fixture
def sample_list():
    """Fixture providing a sample list for testing."""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Add more fixtures as needed for your tests