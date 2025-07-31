"""Test module for osource-reprod package."""

from osource_reprod import hello_world, add_numbers

def test_hello_world():
    """Test the hello_world function."""
    assert hello_world() == "Hello, World!"
    
def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(1, 2) == 3
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0