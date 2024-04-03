import random
import time

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        print(f"{self.name} rolls a {dice_roll}.")
        return dice_roll

def play_game():
    computer = Player("Computer")
    player = Player("Player")

    while computer.score < 50 and player.score < 50:
        time.sleep(1)  # Pause for better visualization
        computer_roll = computer.roll_dice()
        computer.score += computer_roll
        print(f"{computer.name} total score: {computer.score}\n")

        time.sleep(1)  # Pause for better visualization
        player_roll = player.roll_dice()
        player.score += player_roll
        print(f"{player.name} total score: {player.score}\n")

    if computer.score >= 50:
        print(f"{computer.name} wins!")
    else:
        print(f"{player.name} wins!")

if __name__ == "__main__":
    play_game()
