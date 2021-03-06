import pytest
from queue import Queue

@pytest.fixture()
def test_queue():
    return Queue()
