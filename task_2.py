import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        """
        Create the game board with buttons.
        """
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=('Helvetica', 20), 
                                               width=8, height=4, 
                                               command=lambda i=i, j=j: self.make_move(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        """
        Make a move on the board and check for win or draw conditions.
        """
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.buttons[row][col]['text'] = self.current_player
            if self.check_win(row, col):
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self, row, col):
        """
        Check if the current move resulted in a win.
        """
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
            return True
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
            return True
        if (row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ') or \
           (row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True
        return False

    def check_draw(self):
        """
        Check if the game has ended in a draw.
        """
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def reset_board(self):
        """
        Reset the game board after a win or draw.
        """
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x600")  # Set the size of the window
    game = TicTacToe(root)
    root.mainloop()
