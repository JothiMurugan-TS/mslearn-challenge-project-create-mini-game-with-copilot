import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    rounds = int(input("Enter the number of rounds: "))
    player1_score = 0
    player2_score = 0

    for round in range(1, rounds+1):
        print(f"Round {round}")
        computer_choice = random.choice(choices)
        player1_choice = input("Player 1, enter your choice (rock/paper/scissors): ").lower()
        player2_choice = input("Player 2, enter your choice (rock/paper/scissors): ").lower()

        if player1_choice not in choices or player2_choice not in choices:
            print("Invalid choice. Please try again.")
            return

        print(f"Player 1 chose: {player1_choice}")
        print(f"Player 2 chose: {player2_choice}")

        if player1_choice == player2_choice:
            print("It's a tie!")
        elif (player1_choice == "rock" and player2_choice == "scissors") or \
             (player1_choice == "paper" and player2_choice == "rock") or \
             (player1_choice == "scissors" and player2_choice == "paper"):
            print("Player 1 wins!")
            player1_score += 1
        else:
            print("Player 2 wins!")
            player2_score += 1

    return player1_score, player2_score

player1_score, player2_score = play_game()

print("Game over!")
print(f"Player 1 score: {player1_score}")
print(f"Player 2 score: {player2_score}")
