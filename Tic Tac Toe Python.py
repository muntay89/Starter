import random
random.seed()

board = ["-", "-", "-",
         "-", "-", "-", #board
         "-", "-", "-" ]
player = "X" #X's and O's
winner = None # winner variable
gamerunning = True #Game running bool

def printBoard(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5]) #print board
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])

def playerInput(board):
    inp = int(input(f"Player {player}: Enter a number 1- 9: "))
    if board[inp -1] == "-": #Only input X/O if square is available
        if inp >= 1 and inp <= 9: #Only if within range
            board[inp - 1] = player #Change square to X/O
        else:
            print("Invalid Input")
    else:
        print("Square already chosen!")
        playerInput(board) #Player not swapped until valid square chosen

def checkBoard(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner == board[5]
        return True
    elif board[6] == board[7] == board[8] and board[7] != "-":
        winner == board[7]
        return True
    elif board[0] == board[3] == board[6] and board[3] != "-": #Check if win condition is met
        winner = board[3]
        return True #Return Bool
    elif board[1] == board[4] == board[7] and board[4] != "-":
        winner = board[7]
        return True
    elif board[2] == board[5] == board[8] and board[5] != "-":
        winner = board[8]
        return True
    elif board[0] == board[4] == board[8] and board[4] != "-":
        winner = board[8]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[4]
        return True

def checkWinner(board):
    if checkBoard(board): # If bool returned (Win condition met)
        global gamerunning
        printBoard(board)
        print(f"The winner is Player {winner}")
        gamerunning = False

def checkTie(board):
    if "-" not in board: #If all squares filled
        global gamerunning
        printBoard(board)
        print("There is no winner! Try again?")
        gamerunning = False

def switchPlayer(board):
    global player
    if player == "X": 
        player = "O" #Swap player
    else:
        player = "X"

def continuePlaying(board):
    global gamerunning
    global winner
    inp = input("Play again? \n [Y] \n [N] \n")
    if inp == "Y":
        board = ["-", "-", "-",
                 "-", "-", "-", #Reset board
                 "-", "-", "-"]
        gamerunning = True #Set gamerunning bool
        winner = None #Reset winner
        game(board) #Restart fct
    else:
        print("Thanks for playing")
       
    
def game(board):
    while gamerunning: #While bool is met
        printBoard(board)
        playerInput(board)
        checkWinner(board)
        checkTie(board)
        switchPlayer(board)
        if winner != None: #If game is over
            continuePlaying(board)
game(board)



