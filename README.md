# twitch-chat-vjoy
twitch-chat-vjoy is a tool for converting button presses from twitch chat into raw input for the [vjoy](http://vjoystick.sourceforge.net/site/) application. Vjoy configures nicely with the Dolphin emulator in particular. This project is a work in progress.

## Architecture
* Queue    (`src/main.py`)
* producer (`src/producer.py`)
* consumer (`src/consumer.py`)

- Producer reads and parses chat for commands then pushes to the Queue
- Consumer reads the latest entry in the queue, decides if its valid input, and executes it as a vjoy controller

## Usage
Since vJoy is used, Windows 10 is only supported and tested.
```powershell
git clone git@github.com:Ecalzo/twitch-chat-vjoy.git
$ENV:TWITCH_OATH = "<my_oath_token>"
pip install -r requirements.txt
vim config.ini  # update the controller and twitch configs  
python src/main.py
```

Chat controls the game like this:
```
nyccoder: !right  # results in 1 press of the "right" button
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
* Redesign as pip-installable wrapper


![](https://videoapi-muybridge.vimeocdn.com/animated-thumbnails/image/521e77eb-d0d9-49e8-932e-decf6368605f.gif?ClientID=vimeo-core-prod&Date=1615509835&Signature=8ea79ab6b55a60a84ff6cf05d77782b321c77314)
