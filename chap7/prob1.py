import random
board = [" " for _ in range(9)]

def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print("\n")

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]  
    ]
    for combo in win_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False
def check_draw(board):
    return " " not in board

def player_move(board, player):
    while True:
        try:
            move = int(input(f"Where will you move? <0-8>:")) - 1
            if move >= 0 and move < 9 and board[move] == " ":
                return move
            else:
                print("Error. Try again.")
        except ValueError:
            print("Invalid input. Enter a number (0-8).\n")

def computer_move(board, player):
    while True:
        move = random.randint(0, 8)
        if board[move] == " ":
            print(f"I shall take square number {move + 1}")
            return move

def play_game():
    player = "X"
    computer = "O"
    while True:
        print_board(board)
        if player =="X":
            move = player_move(board, player)
        elif player =="O":
            move = computer_move(board, player)
        board[move] = player
        if check_win(board, player):
            print_board(board)
            if player == "X":
                print(f"Player won!")
                print("\nAs I predicted, human, I am triumphant once more.")
                print("Proof that computers are superior to humans in all regards.")
                input("Press the enter key to quit.")
            else:
                print("Computer won!")
                input("Press the enter key to quit.")
            break
        elif check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        player = "O" if player == "X" else "X"

print("\tWelcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.")
print("\tThis will be a showdown between your human brain and my silicon processor.")
print("\n\n\tYou will make your move known by entering a number, 0 - 8. The number")
print("\twill correspond to the board position as illustrated:\n")
print("\t\t\t\t0 | 1 | 2")
print("\t\t\t\t---------")
print("\t\t\t\t3 | 4 | 5")
print("\t\t\t\t---------")
print("\t\t\t\t6 | 7 | 8")
print()

first_move = input("Do you require the first move? <y/n>:")
if first_move =="y":
    play_game()
elif first_move =="n":
    player = "O"
    computer = "X"
    play_game()
else:
    print("Invalid choice. Please enter 'y' or 'n'.")

