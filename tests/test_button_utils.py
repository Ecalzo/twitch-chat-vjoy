import pytest
from src.utils.button_utils import BUTTON_MAPPING, map_button_press_to_input

def test_map_button_press_to_input():
    assert map_button_press_to_input("up") == BUTTON_MAPPING["up"]
    assert map_button_press_to_input("escape") == 0
    assert map_button_press_to_input("should return None") == None

