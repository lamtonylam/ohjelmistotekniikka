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
        self.status_message = StringVar()

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

        # status message on player creation
        status_label = ttk.Label(
            master=self.root,
            textvariable=self.status_message,
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
        status_label.grid(row=6, column=0, columnspan=3)

    def handle_submit(self):
        pass

    def create_player(self):
        player_name = self.create_player_name.get()
        if player_name:
            try:
                elo_service = EloService()
                elo_service.create_user(player_name)
                self.status_message.set(
                    f"Player '{player_name}' has been added successfully!"
                )
                self.create_player_name.set("")
            except Exception as e:
                self.status_message.set(f"Error: {str(e)}")
        else:
            self.status_message.set("Error: Player name cannot be empty!")

        self.root.after(3000, lambda: self.status_message.set(""))
