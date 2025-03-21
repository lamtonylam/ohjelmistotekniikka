from tkinter import Tk, ttk, StringVar, BooleanVar

from services.elo_service import EloService


class UI:
    def __init__(self, root):
        self.root = root
        self.create_player_name = StringVar()
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

        # player creation
        placeholder_label = ttk.Label(master=self.root, text="")
        player_creation_label = ttk.Label(master=self.root, text="Create Player:")
        player_creation_entry = ttk.Entry(
            master=self.root, textvariable=self.create_player_name
        )
        player_creation_button = ttk.Button(
            master=self.root, text="Create", command=self.create_player
        )

        # layout grid
        player1_label.grid(row=0, column=0)
        player1_entry.grid(row=0, column=1)
        player2_label.grid(row=1, column=0)
        player2_entry.grid(row=1, column=1)
        player1_check.grid(row=2, column=0)
        player2_check.grid(row=2, column=1)
        submit_button.grid(row=3, column=0, columnspan=2)

        placeholder_label.grid(row=4, column=0)
        player_creation_label.grid(row=5, column=0)
        player_creation_entry.grid(row=5, column=1)
        player_creation_button.grid(row=5, column=2)

    def handle_submit(self):
        pass

    def create_player(self):
        elo_service = EloService()
        elo_service.create_user(self.create_player_name.get())
        self.create_player_name.set("")
