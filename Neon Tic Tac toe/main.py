import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Neon Tic Tac Toe")

# Global variables
current_player = "X"
board = [" " for _ in range(9)]
buttons = []

# Define colors
neon_green = "#39FF14"
neon_pink = "#FF1493"
bg_color = "#000000"  # Black background
fg_color = "#FFFFFF"  # White foreground for buttons

# Function to check for a winner
def check_winner():
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)  # Diagonal
    ]

    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != " ":
            return board[combo[0]]
    return None

# Function to handle button click
def on_button_click(index):
    global current_player

    if board[index] == " ":
        board[index] = current_player
        buttons[index].config(text=current_player, state="disabled")

        winner = check_winner()
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_game()
        elif " " not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to reset the game
def reset_game():
    global current_player, board

    current_player = "X"
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="normal")

# Create the buttons
for i in range(9):
    button = tk.Button(root, text=" ", font=("Helvetica", 20), width=5, height=2,
                       fg=fg_color, bg=bg_color, activeforeground=neon_green, activebackground=neon_pink,
                       command=lambda i=i: on_button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Set the background color of the root window
root.configure(bg=bg_color)

# Start the main event loop
root.mainloop()
