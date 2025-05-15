# Craps Game

## Overview
This project implements a simple Craps game for up to 6 players. Each player starts with a balance of $5000 and can place bets until the game is turned off. The game consists of 10 rounds, with players taking turns to roll the dice.

## Project Structure
```
craps-game
├── src
│   ├── main.py        # Entry point for the game, initializes and manages game loop
│   ├── game.py        # Contains the Game class for game logic and flow
│   ├── player.py      # Defines the Player class for player management
│   └── utils.py       # Utility functions for dice rolling and game status
├── requirements.txt    # Lists dependencies for the project
└── README.md           # Documentation for the project
```

## How to Run the Game
1. Ensure you have Python installed on your machine.
2. Clone the repository or download the project files.
3. Navigate to the project directory in your terminal.
4. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
5. Start the game by executing:
   ```
   python src/main.py
   ```

## Game Rules
- Each player starts with a balance of $5000.
- Players take turns rolling two dice.
- Players can place bets on the outcome of the dice rolls.
- The game continues for a total of 10 rounds, with players switching turns.
- The game ends when players decide to exit or after 10 rounds.

## Dependencies
- The project may require libraries for random number generation and user input handling. Ensure all dependencies listed in `requirements.txt` are installed.

## Contributing
Feel free to contribute to the project by submitting issues or pull requests. Your feedback and improvements are welcome!