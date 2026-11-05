import random

choices = ("Rock", "Paper", "Scissor")
player_wins = 0
computer_wins = 0
decisive_rounds = 0

while decisive_rounds < 5:
    player_choice = input("Choose Rock, Paper, or Scissor: ").strip().lower()
    if player_choice not in ("rock", "paper", "scissor"):
        print("Please enter Rock, Paper, or Scissor.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose {computer_choice}.")

    computer_choice = computer_choice.lower()
    if player_choice == computer_choice:
        print("It's a tie. Try again.")
        continue

    decisive_rounds += 1
    if (
        (player_choice == "rock" and computer_choice == "scissor")
        or (player_choice == "scissor" and computer_choice == "paper")
        or (player_choice == "paper" and computer_choice == "rock")
    ):
        player_wins += 1
        print("You win this round.")
    else:
        computer_wins += 1
        print("Computer wins this round.")

print(f"\nFinal score: You {player_wins} - Computer {computer_wins}")
if player_wins > computer_wins:
    print("You win the game!")
else:
    print("Computer wins the game!")
    