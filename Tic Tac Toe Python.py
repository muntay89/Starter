import random
random.seed()

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-" ]
player = "X"
winner = None
gamerunning = True
i = 1

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])



def playerInput(board):
    inp = int(input(f"Player {i}: Enter a number 1- 9: "))
    if inp >= 1 and inp <=9:
        board[inp-1] = player 
    else:
        print("Invalid input")


def checkBoard(board):
    global winner
    global gamerunning
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        gamerunning = False
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner == board[5]
        gamerunning = False
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner == board[7]
        gamerunning = False
        return True
    elif board[0] == board[3] == board[6] and board[3] != "-":
        winner = board[3]
        gamerunning = False
        return True
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[7]
        gamerunning = False
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[8]
        gamerunning = False
        return True
    elif board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[8]
        gamerunning = False
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        gamerunning = False
        return True

def checkWinner(board):
    if checkBoard(board):
        global gamerunning
        printBoard(board)
        print(f"The winner is Player {i}")

def checkTie(board):
    if "-" not in board:
        global gamerunning
        printBoard(board)
        print("There is no winner! Try again?")
        gamerunning = False

def switchPlayer(board):
    global player
    global i
    if player == "X":
        player = "O"
        i = 2
    else:
        player = "X"
        i = 1

def game(board):
    while gamerunning:
        printBoard(board)
        playerInput(board)
        checkWinner(board)
        checkTie(board)
        switchPlayer(board)
    
game(board)

inp = input(("Play again? \n[Y] \n[N]\n"))
if inp == "Y":
    gamerunning = True
    board =["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-" ]
    game(board)
else:
    print("Thanks for Playing")
    



