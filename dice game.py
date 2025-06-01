# Language selected: Python

# You can start writing your Python code below.
import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = int(input("Number of players: "))
    if 2 <= players <= 4:
        break
    else:
        print("Only 2 to 4 players are allowed")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_id in range(players):
        print("\nPlayer", player_id + 1,"'s turn!")
        print("Your current score is", player_scores[player_id])
        current_score = 0
        while True:
            should_roll = input("Would you like to roll the dice? (y): ")
            if should_roll.lower() != 'y':
                break

            value = roll_dice()

            if value == 1:
                print("You rolled a 1! Your score has been reset to 0.")
                current_score = 0
                break

            else:
                current_score += value
                print("You rolled a", value)

            print("Your score is", current_score)    

    player_scores[player_id] += current_score
    print("Your total score is", player_scores[player_id])
      
max_score = max(player_scores)
winning_id = palyer_scores.index(max_score)
print("Player", winning_id + 1, "wins with a score of", max_score)
          


        
    
