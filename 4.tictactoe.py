import tkinter as tk
from tkinter import messagebox

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("300x400")  # Increased height to accommodate status label and reset button

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.create_widgets()

    def create_widgets(self):
        self.board_frame = tk.Frame(self)
        self.board_frame.pack(pady=20, padx=50)  # Added padding to center the board

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.board_frame, text="", font=("Arial", 20), width=6, height=3,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j, padx=5, pady=5)  # Added padding for spacing

        self.status_label = tk.Label(self, text=f"Player {self.current_player}'s turn", font=("Arial", 12))
        self.status_label.pack(pady=10)

        self.reset_button = tk.Button(self, text="Reset", command=self.reset_game)
        self.reset_button.pack()

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_win(self, player):
        for i in range(3):
            if all([self.board[i][j] == player for j in range(3)]) or \
               all([self.board[j][i] == player for j in range(3)]):
                return True

        if all([self.board[i][i] == player for i in range(3)]) or \
           all([self.board[i][2-i] == player for i in range(3)]):
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if " " in row:
                return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")

        self.status_label.config(text=f"Player {self.current_player}'s turn")

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()

'''
Explanation:
Initialization (__init__ method):

Initializes the TicTacToe class as a subclass of tk.Tk.
Sets the title, geometry, current player (self.current_player), and initializes the board (self.board) as a 3x3 grid of empty strings " ".
Creating Widgets (create_widgets method):

Creates a 3x3 grid of tk.Button widgets (self.buttons) where players can click to make their moves.
Sets up a status label (self.status_label) to display whose turn it is.
Adds a reset button (self.reset_button) to reset the game.
Handling Button Clicks (on_button_click method):

Checks if the clicked button (self.buttons[row][col]) corresponds to an empty space on the board (self.board[row][col] == " ").
Updates the board and button text with the current player's mark (self.current_player).
Checks for a win (self.check_win(self.current_player)) or a tie (self.is_board_full()).
Updates the current player and status label accordingly.
Checking Win (check_win method):

Checks rows, columns, and diagonals to determine if the current player has won.
Board Full Check (is_board_full method):

Checks if there are any empty spaces left on the board to determine if the game is a tie.
Resetting the Game (reset_game method):

Resets the current player (self.current_player), clears the board (self.board), and updates button texts to empty.
Resets the status label to indicate it's Player X's turn.
Main Loop:

Initializes an instance of TicTacToe (app) and starts the tkinter main event loop (app.mainloop()).
Changes Made:
Board Frame:

Created a self.board_frame using tk.Frame to contain the Tic Tac Toe grid.
Packed self.board_frame with pady=20 and padx=50 to center align the grid and provide adequate padding around it.
Grid Layout:

Used grid() method for placing buttons (self.buttons[i][j].grid(...)) within self.board_frame.
Added padx=5 and pady=5 within grid() to create space between buttons for better visual separation.
Status Label and Reset Button:

self.status_label and self.reset_button are packed directly in the main window (self) below self.board_frame.
Adjusted self.geometry("300x400") to accommodate the status label and reset button at the bottom of the window.
Responsive Design:

By using pack() and grid() with appropriate padding and alignment, the game interface is made more responsive and centered within the window.
'''