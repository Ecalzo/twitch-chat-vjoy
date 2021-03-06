# twitch-chat-vjoy
twitch-chat-vjoy is a tool for converting button presses from twitch chat into raw input for the [vjoy](http://vjoystick.sourceforge.net/site/) application. Vjoy configures nicely with the Dolphin emulator in particular. This project is a work in progress.

## Architecture
* 1 Queue    (`src/main.py`)
* 1 producer (`src/producer.py`)
* 1 consumer (`src/consumer.py`)

- Producer reads and parses chat for commands then push to the Queue
- Consumer reads the latest entry in the queue and executes it as a vjoy controller

## Usage
This section will be changing as usage evolves.
Since vJoy is used, Windows 10 is only supported and tested.
```powershell
git clone <this_repo>
$ENV:TWITCH_OATH = "<my_oath_token>"
pip install -r requirements.txt
vim config.ini  # update the controller and twitch configs  
python src/main.py
```

Chat controls the game like this:
```
nyccoder !right  # results in 1 press of the "right" button
nyccoder: !up 10  # results in 10 presses up the "up" button
```

## Testing
```
pip install pytest
pytest tests/
```

## Roadmap/QoL Improvements
* .ini file for twitch chat setup - DONE (combined w/ button mapping as config.ini)
* .ini file for button mapping - DONE
* remove !press from command, make them like !a or !b - DONE
* be able to press a button n number of times (limit this) - DONE
