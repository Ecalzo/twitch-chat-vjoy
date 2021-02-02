# twitch-chat-vjoy
twitch-chat-vjoy is a tool for converting button presses from twitch chat into raw input for the [vjoy](http://vjoystick.sourceforge.net/site/) application. Vjoy configures nicely with the Dolphin emulator in particular. This project is a work in progress.

## Architecture
* 1 Queue    (`src/main.py`)
* 1 producer (`src/producer.py`)
* 1 consumer (`src/consumer.py`)

- Producer reads and parses chat for commands then push to the Queue
- Consumer reads the latest entry in the queue and executes it as a vjoy controller

## Usage
This section will be changing as usage evolves
```shell
git clone <this_repo>
export TWITCH_OATH = "<my_oath_token>"
pip install -r requirements.txt
cd src/
vim producer.py  # update the globals in producer.py  
python main.py
```
