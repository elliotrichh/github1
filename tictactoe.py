import tkinter as tk
from tkinter import messagebox

# initialize the game board and variables
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
currentPlayer = "X"
player2 = "O"
winner = None
gameRunning = True

# print the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Check for a win in rows
def checkHorisontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer

# Check for a win in diagonals
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer

# Check for a win in columns
def checkColums(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer

# Check if any player has won
def checkWin(board):
    checkHorisontal(board)
    checkDiagonal(board)
    checkColums(board)

# Check for a tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("TIE!")
        gameRunning = False

# Switch players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Define a function to handle button clicks
def handleclick(indx, buttons, board):
    global currentPlayer, gameRunning, winner
    if board[indx] == "-" and gameRunning:
        board[indx] = currentPlayer
        buttons[indx].config(text=currentPlayer)
        checkWin(board)
        checkTie(board)
        if not gameRunning:
            if winner:
                messagebox.showinfo("Ultimate CHAMPION", "YOU WIN!!")
            else:
                messagebox.showerror("failed", "TIED")

        switchPlayer()


# Create the main GUI window
root = tk.Tk()
root.title("Tic tac toe gui project")

# Create buttons for the game
buttons = []
for i in range(9):
    row = i // 3
    col = i % 3
    button = tk.Button(root, text="-", font=("Helvetica", 24), height=2, width=5,
                       command=lambda i=i: handleclick(i, buttons, board))
    button.grid(row=row, column=col)
    buttons.append(button)

root.mainloop()
