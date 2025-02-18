# nn-n


import tkinter as tk
from tkinter import messagebox
import copy

def is_valid(board, num, row, col):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    box_x, box_y = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_x + i][box_y + j] == num:
                return False
    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, num, row, col):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

class GudokuApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gudoku")
        self.root.configure(bg="white")
        self.board = [[0] * 9 for _ in range(9)]
        self.cells = [[None] * 9 for _ in range(9)]
        self.create_grid()
        self.solve_button = tk.Button(root, text="Solve", command=self.solve_puzzle, font=("Arial", 14), bg="#4CAF50", fg="white", borderwidth=0, padx=10, pady=5)
        self.solve_button.grid(row=10, column=0, columnspan=9, sticky="nsew", pady=10)
    
    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=3, font=('Arial', 18), justify='center', relief="flat", bg="white", fg="black")
                entry.grid(row=row, column=col, ipadx=5, ipady=5, padx=(2 if col % 3 == 0 else 1, 2 if col % 3 == 2 else 1), 
                           pady=(2 if row % 3 == 0 else 1, 2 if row % 3 == 2 else 1))
                entry.bind("<FocusOut>", lambda e, r=row, c=col: self.update_board(r, c))
                self.cells[row][col] = entry
    
    def update_board(self, row, col):
        try:
            value = self.cells[row][col].get()
            if value:
                num = int(value)
                if 1 <= num <= 9 and self.board[row][col] == 0:
                    self.board[row][col] = num
                else:
                    self.cells[row][col].delete(0, tk.END)
        except ValueError:
            self.cells[row][col].delete(0, tk.END)

    def solve_puzzle(self):
        temp_board = copy.deepcopy(self.board)
        if solve(temp_board):
            for r in range(9):
                for c in range(9):
                    self.cells[r][c].delete(0, tk.END)
                    self.cells[r][c].insert(0, str(temp_board[r][c]))
        else:
            messagebox.showerror("Error", "No solution exists!")

if __name__ == "__main__":
    root = tk.Tk()
    app = GudokuApp(root)
    root.mainloop()