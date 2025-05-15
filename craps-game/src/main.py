# This is the main entry point for the craps game.

# Import necessary modules
from game import Game
from player import Player

def main():
    # Initialize the game with 6 players, each starting with $5000
    num_players = 6
    starting_balance = 5000
    players = []

    # Create player instances
    for i in range(num_players):
        player_name = f"Player {i + 1}"
        players.append(Player(name=player_name, balance=starting_balance))

    # Create a Game instance
    craps_game = Game(players)

    # Start the game loop for a maximum of 10 rounds
    rounds = 10
    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        craps_game.play_round()

    print("Game over! Thank you for playing.")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()