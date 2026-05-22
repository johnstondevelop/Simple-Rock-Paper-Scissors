import random;

print("Welcome to Rock, Paper, and Scissors!")

while True:
    moves = ["rock", "paper", "scissors"]

    player_move = input("Enter your move! (rock, paper, scissors): ").lower()

    if player_move not in moves:
        print("Invalid Move! Please enter 'rock', 'paper', or 'scissors'.")
        continue
    else:

        computer_move = random.choice(moves)
    print(f"Computer chose: {computer_move}")
    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == "rock" and computer_move == "scissors") or (player_move == "scissors" and computer_move == "paper") or (player_move == "paper" and computer_move == "rock"):
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Do you want to play again? (yes or no):").lower()
    if play_again != "yes":
        print("Thanks for playing!")
    elif play_again == "yes":
        print("Then lets play again!")
        continue
    break