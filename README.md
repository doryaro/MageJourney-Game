# MageJourney

MageJourney is a single-player action-adventure game built using the `pygame` library.

## Installation and Running

### Prerequisites

- **Python** and **pip** should be installed on your machine.
- Navigate to the **MageJourney** project directory using the command prompt or terminal.

### Build and Play Instructions:

1. **Install `pyinstaller`**  
   If you haven't already installed `pyinstaller`, do so with the following command:  

2. **Generate the standalone executable for MageJourney**  
Ensure you're in the directory where `main.py` is located and then run:  
`pyinstaller --onefile --windowed --name MageJourney --icon=MobliePics\icon.ico --add-data MageJourney-Game\MobliePics;MobliePics --add-data MageJourney-Game\Sounds;Sounds --add-data MageJourney-Game\config.ini;. main.py Mage.py MageSpells.py Monster.py Zombie.py Game.py`


3. **Navigate to the `dist` directory**:  
cd dist

4. run `MageJourney.exe` or Double click the MageJourney.exe icon

## Gameplay

Use your mouse to cast spells or to use health potions. \
Casting Spells: With a simple click of your mouse, unleash the fury of your magic. Choose between:
1. Fireball: A classic spell, a ball of fire towards your enemy
2. Meteor shower: Call down a meteor from the sky, dealing massive damage 
   
Drink a Health Potion: Restore some of your lost vitality, but use them wisely you might run out when you need them most! \

Thank you for playing MageJourney!
