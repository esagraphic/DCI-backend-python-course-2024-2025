import random

class Dice:
    def __init__(self):
        self.sides = 6

    def roll(self):
        """Roll the die and return a random number between 1 and 6."""
        return random.randint(1, self.sides)

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self, dice):
        """Roll the dice and update the player's score."""
        roll_result = dice.roll()
        self.score += roll_result
        print(f"{self.name} rolled a {roll_result}. Total score: {self.score}")

class Game:
    def __init__(self, player1_name, player2_name, rounds):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.dice = Dice()
        self.rounds = rounds

    def play(self):
        """Play the game for a specified number of rounds."""
        for round_number in range(1, self.rounds + 1):
            print(f"\nRound {round_number}")
            self.player1.roll_dice(self.dice)
            self.player2.roll_dice(self.dice)

        self.declare_winner()

    def declare_winner(self):
        """Declare the winner based on the final scores."""
        print("\nFinal Scores:")
        print(f"{self.player1.name}: {self.player1.score}")
        print(f"{self.player2.name}: {self.player2.score}")

        if self.player1.score > self.player2.score:
            print(f"{self.player1.name} wins!")
        elif self.player1.score < self.player2.score:
            print(f"{self.player2.name} wins!")
        else:
            print("It's a tie!")

# Main function to run the game
if __name__ == "__main__":
    print("Welcome to the Dice Game!")
    player1_name = input("Enter the name of Player 1: ")
    player2_name = input("Enter the name of Player 2: ")
    rounds = int(input("Enter the number of rounds to play: "))

    game = Game(player1_name, player2_name, rounds)
    game.play()
