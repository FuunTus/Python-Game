print("Rock, Paper, Scissors")

# Prompt player 1 to choose rock, paper, or scissors
while True:
    player1 = input("Player 1, choose rock, paper, or scissors: ")
    if player1 in ['rock', 'paper', 'scissors']:
        break
    print("Invalid input. Try again.")

# Prompt player 2 to choose rock, paper, or scissors
while True:
    player2 = input("Player 2, choose rock, paper, or scissors: ")
    if player2 in ['rock', 'paper', 'scissors']:
        break
    print("Invalid input. Try again.")

# Determine the winner
if player1 == player2:
    print("Draw")
elif player1 == 'rock' and player2 == 'scissors':
    print("Player 1 wins")
elif player1 == 'paper' and player2 == 'rock':
    print("Player 1 wins")
elif player1 == 'scissors' and player2 == 'paper':
    print("Player 1 wins")
else:
    print("Player 2 wins")
