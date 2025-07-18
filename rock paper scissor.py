import random

print("Welcome to Rock Paper Scissors!")


player_score = 0
computer_score = 0

while True:
    print("\nChoose your move: rock, paper, or scissors")
    player_move = input("Your move: ").lower()

    if player_move not in ['rock', 'paper', 'scissors']:
        print("Choose anything else")
        continue

    
    computer_move = random.choice(['rock', 'paper', 'scissors'])
    print("Computer chose:", computer_move)

    
    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == 'rock' and computer_move == 'scissors') or \
         (player_move == 'paper' and computer_move == 'rock') or \
         (player_move == 'scissors' and computer_move == 'paper'):
        print("You win!")
        player_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    
    print("Score -> You:", player_score, "Computer:", computer_score)

    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
