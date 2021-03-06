from .config_utils import get_config

config = get_config()
# convert unicode string to integer for vJoy
raw_button_mapping = config._sections["BUTTON_MAPPING"]
BUTTON_MAPPING = {cmd: int(btn) for cmd, btn in raw_button_mapping.items()}

def map_button_press_to_input(button_press: str) -> int:
    if button_press in BUTTON_MAPPING:
        return BUTTON_MAPPING[button_press]
    elif button_press == "escape":
        return 0
    else:
        return None
