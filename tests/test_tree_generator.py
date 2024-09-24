import os
import pytest
from tree_generator import TreeGenerator


@pytest.fixture
def setup_teardown():
    test_file = "test_tree.txt"
    yield test_file
    if os.path.exists(test_file):
        os.remove(test_file)


def test_generate_tree_3_levels(setup_teardown):
    test_file = setup_teardown
    expected_output = (
        "      W      \n"
        "      *      \n"
        "  @ * * * *  \n"
        "* * * * * * * * @\n"
        "@ * * * * * * * * * * * *\n"
        "    TTTTT    \n"
        "    TTTTT    \n"
    )

    tree = TreeGenerator(3, test_file)
    tree.generate_tree()

    with open(test_file, 'r') as f:
        content = f.read()

    assert content == expected_output
    print("елка совпадает")