class Game:
    def __init__(self, num_players=6, starting_balance=5000):
        """
        Initializes the Game class with the number of players and their starting balance.
        
        :param num_players: Number of players in the game.
        :param starting_balance: Initial amount of money each player has.
        """
        self.num_players = num_players
        self.players = []
        self.current_player_index = 0
        self.rounds = 10

        # Create player instances
        for i in range(num_players):
            player_name = f"Player {i + 1}"
            self.players.append(Player(player_name, starting_balance))

    def start_game(self):
        """
        Starts the game and manages the game loop for a set number of rounds.
        """
        for round_number in range(self.rounds):
            print(f"Round {round_number + 1}")
            self.play_round()
            self.current_player_index = (self.current_player_index + 1) % self.num_players

    def play_round(self):
        """
        Plays a round of the game where the current player rolls the dice and places bets.
        """
        current_player = self.players[self.current_player_index]
        print(f"{current_player.name}'s turn.")
        
        # Player places a bet
        bet_amount = current_player.place_bet()
        
        # Roll the dice
        roll_result = self.roll_dice()
        print(f"{current_player.name} rolled a {roll_result}.")
        
        # Determine win/loss
        if self.check_win(roll_result):
            current_player.update_balance(bet_amount)
            print(f"{current_player.name} wins! New balance: {current_player.balance}")
        else:
            current_player.update_balance(-bet_amount)
            print(f"{current_player.name} loses! New balance: {current_player.balance}")

    def roll_dice(self):
        """
        Rolls two dice and returns the total value.
        
        :return: Total value of the two dice.
        """
        import random
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1 + die2

    def check_win(self, roll_result):
        """
        Checks if the rolled result is a winning number.
        
        :param roll_result: The result of the dice roll.
        :return: True if the result is a winning number, False otherwise.
        """
        # Define winning conditions (for simplicity, let's say 7 or 11 is a win)
        return roll_result in [7, 11]