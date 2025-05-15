class Player:
    def __init__(self, name):
        """
        Initializes a new player with a name and a starting balance.
        
        :param name: The name of the player.
        """
        self.name = name  # Player's name
        self.balance = 5000  # Starting balance for each player

    def place_bet(self, amount):
        """
        Allows the player to place a bet, deducting the amount from their balance.
        
        :param amount: The amount to bet.
        :return: True if the bet is placed successfully, False if insufficient balance.
        """
        if amount > self.balance:
            print(f"{self.name} does not have enough balance to place this bet.")
            return False
        self.balance -= amount  # Deduct the bet amount from balance
        print(f"{self.name} placed a bet of ${amount}. Remaining balance: ${self.balance}.")
        return True

    def update_balance(self, amount):
        """
        Updates the player's balance based on the game outcome.
        
        :param amount: The amount to add to the balance (can be negative for losses).
        """
        self.balance += amount  # Update balance based on game outcome
        if amount > 0:
            print(f"{self.name} won ${amount}! New balance: ${self.balance}.")
        else:
            print(f"{self.name} lost ${-amount}. New balance: ${self.balance}.")

    def __str__(self):
        """
        Returns a string representation of the player.
        
        :return: A string with the player's name and current balance.
        """
        return f"Player: {self.name}, Balance: ${self.balance}"