from queue import Queue

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
            return button_press
    return ""