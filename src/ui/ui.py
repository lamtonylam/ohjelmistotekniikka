from tkinter import Tk, ttk, StringVar, BooleanVar


class UI:
    def __init__(self, root):
        self.root = root
        self.player1_var = StringVar()
        self.player2_var = StringVar()
        self.player1_won = BooleanVar()
        self.player2_won = BooleanVar()

    def start(self):
        # player 1 input
        player1_label = ttk.Label(master=self.root, text="Player 1:")
        player1_entry = ttk.Entry(master=self.root, textvariable=self.player1_var)

        # player 2 input
        player2_label = ttk.Label(master=self.root, text="Player 2:")
        player2_entry = ttk.Entry(master=self.root, textvariable=self.player2_var)

        # winner checkboxes
        player1_check = ttk.Checkbutton(
            master=self.root, text="Player 1 won", variable=self.player1_won
        )
        player2_check = ttk.Checkbutton(
            master=self.root, text="Player 2 won", variable=self.player2_won
        )

        # submit button
        submit_button = ttk.Button(
            master=self.root, text="Submit", command=self.handle_submit
        )

        # layout grid
        player1_label.grid(row=0, column=0)
        player1_entry.grid(row=0, column=1)
        player2_label.grid(row=1, column=0)
        player2_entry.grid(row=1, column=1)
        player1_check.grid(row=2, column=0)
        player2_check.grid(row=2, column=1)
        submit_button.grid(row=3, column=0, columnspan=2)

    def handle_submit(self):
        pass
