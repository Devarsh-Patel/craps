def roll_dice():
    """Roll two six-sided dice and return their values as a tuple."""
    import random
    die1 = random.randint(1, 6)  # Roll the first die
    die2 = random.randint(1, 6)  # Roll the second die
    return die1, die2

def validate_bet(bet, balance):
    """Check if the bet is valid based on the player's balance.
    
    Args:
        bet (float): The amount the player wants to bet.
        balance (float): The player's current balance.
    
    Returns:
        bool: True if the bet is valid, False otherwise.
    """
    return 0 < bet <= balance

def display_status(players):
    """Display the current status of all players in the game.
    
    Args:
        players (list): A list of Player objects.
    """
    for player in players:
        print(f"Player: {player.name}, Balance: ${player.balance:.2f}")