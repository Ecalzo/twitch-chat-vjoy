import socket
import re
import os
import logging
from utils.config_utils import get_config
from queue import Queue
from datetime import datetime

config = get_config()
twitch_conf = config["TWITCH"]

SERVER = twitch_conf["server"]
NICKNAME = twitch_conf["nickname"]
# https://twitchapps.com/tmi/
TOKEN = os.getenv("TWITCH_OAUTH")
CHANNEL = twitch_conf["channel"]

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s — %(message)s",
                    datefmt="%Y-%m-%d_%H:%M:%S",
                    handlers=[logging.FileHandler("twitch_vjoy.log", encoding="utf-8")])

try:
    PORT = int(twitch_conf["port"])
except TypeError:
    raise TypeError("provided port in config.ini cannot be parsed to integer")


def setup_connection() -> socket.socket:
    sock = socket.socket()
    sock.connect((SERVER, PORT))

    sock.send(f"PASS {TOKEN}\n".encode("utf-8"))
    sock.send(f"NICK {NICKNAME}\n".encode("utf-8"))
    sock.send(f"JOIN {CHANNEL}\n".encode("utf-8"))
    sock.send(":{NICKNAME}!{NICKNAME}@{NICKNAME}.tmi.twitch.tv JOIN #{channel}".encode("utf-8"))
    return sock

def clean_chat_input(chat_text: str) -> str:
    pass

def push_to_queue_if_valid_input(message: str, queue: Queue) -> str:
    if message.startswith("!"):
        inpt_as_list = message.lower().split("!")
        chat_command = inpt_as_list[-1].split()
        len_check = len(chat_command)
        if len_check == 1:
            button_press = chat_command[0].strip()
            queue.put(button_press)
            return button_press
        elif len_check > 1 and len_check < 3:
            button_press = chat_command[0].strip()
            num_presses = chat_command[1].strip()
            try:
                limit_presses = min(int(num_presses), 10)
            except ValueError:
                limit_presses = 1
            for _ in range(limit_presses):
                queue.put(button_press)
    return ""


def main_producer(queue: Queue) -> None:
    sock = setup_connection()
    while True:
        resp = sock.recv(2048).decode("utf-8")

        if resp.startswith("PING"):
            sock.send("PONG\n".encode("utf-8"))
        
        elif f"{NICKNAME} :Welcome, GLHF!" in resp:
            logging.info(resp)
        
        elif f":{NICKNAME}!{NICKNAME}@{NICKNAME}.tmi.twitch.tv JOIN" in resp:
            logging.info(resp)
            print("chat ready")

        elif len(resp) > 0:
            username, channel, message = re.search(":(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)", resp).groups()
            logging.info(f"\nDate: {datetime.now()} \nChannel: {channel} \nUsername: {username} \nMessage: {message}")
        
            button_press = push_to_queue_if_valid_input(message, queue)
            if button_press == "escape":
                logging.info(f"{username} sent the kill signal {button_press} using {message}, exiting")
                break
            elif button_press:
                logging.info(f"{username} queued {button_press} using {message}")

