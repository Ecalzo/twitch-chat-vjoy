import pytest
from queue import Queue
from src.utils.producer_utils import push_to_queue_if_valid_input

MAX_CMD_SEQ = 10


def test_push_to_queue_if_valid_input(test_queue):
    inpt = "!up 14"
    push_to_queue_if_valid_input(inpt, test_queue)
    assert test_queue.qsize() == 10
    for i in range(MAX_CMD_SEQ):
        test_queue.get()
    assert test_queue.empty()
