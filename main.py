import tkinter as tk
from tkinter import messagebox

class TicTacToe:

    def __init__(self):
        # Setup Window
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#E6F0FA")  
        self.root.resizable(False, False)

        self.current_player = "X"
        self.winner = False

        # Setup Label
        self.label = tk.Label(self.root, text=f"Player {self.current_player}'s turn",font=("Helvetica", 16, "bold"), bg="#E6F0FA", fg="#2C3E50")
        self.label.grid(row=0, column=0, columnspan=3, pady=10)

        # Setup Buttons
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Helvetica", 24, "bold"),width=6, height=2, bg="#F8F9FA", fg="#2C3E50",activebackground="#AEDFF7", activeforeground="#2C3E50",relief="groove", borderwidth=2, command=lambda i=i: self.button_click(i))
            btn.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # Restart Button
        self.restart_btn = tk.Button(self.root, text="Restart Game", font=("Helvetica", 14, "bold"), bg="#87BADC", fg="white", activebackground="#3498DB",activeforeground="white", relief="raised", borderwidth=3, command=self.reset_game)
        self.restart_btn.grid(row=4, column=0, columnspan=3, pady=10, ipadx=10, ipady=5)

    # Handle Click
    def button_click(self, index):
        if self.buttons[index]["text"] == "" and not self.winner:
            self.buttons[index]["text"] = self.current_player
            self.buttons[index].config(fg="#1A5276" if self.current_player == "X" else "#943126")
            self.check_winner()
            self.toggle_player()
            self.check_draw()

    # Switch Player
    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.label.config(text=f"Player {self.current_player}'s turn")

    # Check combos
    def check_winner(self):
        winning_combos = [[0,1,2], [3,4,5], [6,7,8],
                          [0,3,6], [1,4,7], [2,5,8],
                          [0,4,8], [2,4,6]]

        for combo in winning_combos:
            if (self.buttons[combo[0]]["text"] == self.buttons[combo[1]]["text"] == self.buttons[combo[2]]["text"] != ""):
                
                for i in combo:
                    self.buttons[i].config(bg="#63D494")  # highlight green for winner

                for b in self.buttons:
                    b.config(state="disabled")

                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.buttons[combo[0]]['text']} wins! 🎉")
                self.winner = True
                self.ask_replay()
                return

    # Check for draw
    def check_draw(self):
        if all(button["text"] != "" for button in self.buttons) and not self.winner:
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw! 🤝")
            self.ask_replay()

    # Reset game
    def reset_game(self):
        for button in self.buttons:
            button.config(text="", bg="#F8F9FA", state="normal")
        self.winner = False
        self.current_player = "X"
        self.label.config(text=f"Player {self.current_player}'s turn")
        self.root.update_idletasks()

    # Ask for replay
    def ask_replay(self):
        answer = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if answer:
            self.reset_game()
        else:
            self.root.destroy()

    # Start game
    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    game = TicTacToe()
    game.start()
