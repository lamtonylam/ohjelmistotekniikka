from tkinter import Tk, ttk, StringVar, BooleanVar
from services.elo_service import EloService


class UI:
    """Main UI class that coordinates the application's user interface"""

    def __init__(self, root):
        """Initialize the UI

        Args:
            root: The tkinter root window
        """
        self.root = root
        self.elo_service = EloService()

        self.player1_var = StringVar()
        self.player2_var = StringVar()
        self.player1_won = BooleanVar()
        self.player2_won = BooleanVar()

        self.create_player_name = StringVar()
        self.status_message = StringVar()

        self.players = []

    def start(self):
        """Start the UI and arrange all components"""
        self.initialize_match_submission(row_offset=0)

        placeholder_label = ttk.Label(master=self.root, text="")
        placeholder_label.grid(row=4, column=0)

        self.initialize_player_creation(row_offset=5)

        placeholder_label = ttk.Label(master=self.root, text="")
        placeholder_label.grid(row=9, column=0)

        self.initialize_player_table(row_offset=10)

    def initialize_match_submission(self, row_offset=0):
        """Initialize the match submission UI elements

        Args:
            row_offset: The starting row for component elements
        """
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
        submit_button = ttk.Button(master=self.root, text="Submit")

        # layout grid
        player1_label.grid(row=row_offset, column=0)
        player1_entry.grid(row=row_offset, column=1)
        player2_label.grid(row=row_offset + 1, column=0)
        player2_entry.grid(row=row_offset + 1, column=1)
        player1_check.grid(row=row_offset + 2, column=0)
        player2_check.grid(row=row_offset + 2, column=1)
        submit_button.grid(row=row_offset + 3, column=0, columnspan=2)

    def initialize_player_creation(self, row_offset=5):
        """Initialize the player creation UI elements

        Args:
            row_offset: The starting row for component elements
        Returns:
            StringVar: The status message variable for external access
        """
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
        player_creation_label.grid(row=row_offset, column=0)
        player_creation_entry.grid(row=row_offset, column=1)
        player_creation_button.grid(row=row_offset, column=2)
        status_label.grid(row=row_offset + 1, column=0, columnspan=3)
        return self.status_message

    def create_player(self):
        """Handle player creation button click"""
        player_name = self.create_player_name.get()
        if player_name:
            try:
                self.elo_service.create_user(player_name)
                self.status_message.set(
                    f"Player '{player_name}' has been added successfully!"
                )
                self.create_player_name.set("")
                self.fetch_users()
            except Exception as e:
                self.status_message.set(f"Error: {str(e)}")
        else:
            self.status_message.set("Error: Player name cannot be empty!")

    def fetch_users(self):
        """Fetch all users from the EloService"""
        self.players = self.elo_service.get_all_users()

    def initialize_player_table(self, row_offset=10):
        """Initialize the player table UI elements

        Args:
            row_offset: The starting row for component elements
        """
        # Fetch users
        self.fetch_users()

        # Create a label for each player
        for i, player in enumerate(self.players):
            player_label = ttk.Label(self.root, text=player.name)
            # Display label
            player_label.grid(row=row_offset + i, column=0, sticky="w")
