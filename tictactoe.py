#tic toe toe game by elliot

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = "X"
player2="O"
winner = None
gameRunning = True

#making the board

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#input part
def playerInput(board):
    inp=int(input("enter a number 1-9: "))
    if inp>=1 and inp <=9 and board[inp-1]=="-":
        board[inp-1]=currentPlayer
    else:
        print("CANNOT PLACE HERE!")

#checking win status

def checkHorizontal(board):
    global winner
    if(board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-")or(board[6] == board[7] == board[8] and board[6] != "-"):
        winner=currentPlayer
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0]!="-")or(board[2] == board[4] == board[6] and board[2]!="-"):
        winner=currentPlayer
        return True

def checkColumbs(board):
    global winner
    if (board[0]==board[3]==board[6]and board[0]!="-")or (board[1]==board[4]==board[7] and board[1]!="-")or (board[2]==board[5]==board[8] and board[2]!="-"):
        winner=currentPlayer
        return True


def checkWin():
    if checkHorizontal(board) or checkDiagonal(board) or checkColumbs(board):
        print(currentPlayer,"you won yay")
        return True

#finally, check for a tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("YOU HAVE TIED")
        gameRunning = False
#switch tha player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

if __name__ == '__main__':
    while gameRunning:
        if (checkWin()==True):
            break
        printBoard(board)
        playerInput(board)
        switchPlayer()
  #      checkTie(board)
   #     switchPlayer()1