import logging
import pyvjoy
import time
from configparser import ConfigParser
from queue import Queue

config = ConfigParser()
config.read("config.ini")
raw_button_mapping = config._sections["BUTTON_MAPPING"]
# convert unicode string to integer for vJoy
BUTTON_MAPPING = {cmd: int(btn) for cmd, btn in raw_button_mapping.items()}

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s — %(message)s",
                    datefmt="%Y-%m-%d_%H:%M:%S",
                    handlers=[logging.FileHandler("twitch_vjoy.log", encoding="utf-8")])


def map_button_press_to_input(button_press: str) -> int:
    if button_press in BUTTON_MAPPING:
        return BUTTON_MAPPING[button_press]
    elif button_press == "escape":
        return 0
    else:
        return None

def execute_button_press(joy_inpt: int) -> None:
    joy = pyvjoy.VJoyDevice(1)
    joy.set_button(joy_inpt, 1)
    time.sleep(0.25)
    joy.set_button(joy_inpt, 0)
    joy.reset_buttons()
    return

def main_consumer(queue: Queue) -> None:
    while True:
        # FIXME: consider implementing a timeout here
        logging.info("awaiting queue")
        button_press = queue.get()
        logging.info(f"received press: {button_press} from queue")
        controller_input = map_button_press_to_input(button_press)
        logging.info(f"mapped press: {button_press} to input: {controller_input}")
        if controller_input == 0:
            logging.info(f"received kill signal {controller_input}, exiting")
            break
        elif controller_input is not None:
            logging.info(f"executing raw input: {controller_input}...")
            time.sleep(.05)
            execute_button_press(controller_input)
            logging.info(f"successfully executed raw input: {controller_input}")
