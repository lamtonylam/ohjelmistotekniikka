from tkinter import Tk, ttk, StringVar, BooleanVar, Frame
from services.elo_service import EloService
from services.match_service import MatchService


class UI:
    """Main UI class that coordinates the application's user interface"""

    def __init__(self, root):
        """Initialize the UI

        Args:
            root: The tkinter root window
        """
        self.root = root
        self.elo_service = EloService()
        self.match_service = MatchService()

        self.player1_var = StringVar()
        self.player2_var = StringVar()
        self.winner_var = StringVar()
        self.match_submission_status_message = StringVar()

        self.create_player_name = StringVar()
        self.status_message = StringVar()

        self.players = []
        self.player_table_frame = None

        self.match_submission_frame = None

        self.player_creation_frame = None

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

        # creates a root frame for the player table
        self.match_submission_frame = Frame(self.root)
        self.match_submission_frame.grid(
            row=row_offset, column=0, columnspan=3, sticky="ew"
        )
        # create header frame
        header_frame = Frame(self.match_submission_frame)
        header_frame.pack(fill="x")

        # on the left "player list" text, apart of headerframe
        table_header = ttk.Label(header_frame, text="Record a match")
        table_header.pack(side="left", anchor="w", padx=5)

        # player creation frame
        player_creation_frame = Frame(self.match_submission_frame)
        player_creation_frame.pack(fill="x")

        # player 1 input
        player1_label = ttk.Label(player_creation_frame, text="Player 1:")
        player1_label.pack(side="left", anchor="w", padx=5)
        player1_entry = ttk.Entry(player_creation_frame, textvariable=self.player1_var)
        player1_entry.pack(side="left", anchor="w", padx=5)

        # player 1 input
        player2_label = ttk.Label(player_creation_frame, text="Player 2:")
        player2_label.pack(side="left", anchor="w", padx=5)
        player2_entry = ttk.Entry(player_creation_frame, textvariable=self.player2_var)
        player2_entry.pack(side="left", anchor="w", padx=5)

        # winner checkboxes frame
        winner_frame = Frame(self.match_submission_frame)
        winner_frame.pack(fill="x", pady=5)

        # player 1 won radio button
        player1_radio = ttk.Radiobutton(
            winner_frame,
            text="Player 1 won",
            variable=self.winner_var,
            value="player1",
        )
        player1_radio.pack(side="left", anchor="w", padx=5)

        # player 2 won radio button
        player2_radio = ttk.Radiobutton(
            winner_frame,
            text="Player 2 won",
            variable=self.winner_var,
            value="player2",
        )
        player2_radio.pack(side="left", anchor="w", padx=5)

        # submit button frame
        submit_frame = Frame(self.match_submission_frame)
        submit_frame.pack(fill="x", pady=5)

        # submit button
        submit_button = ttk.Button(
            submit_frame, text="Submit", command=self.handle_match_submit
        )
        submit_button.pack(side="top", anchor="center", pady=5)

        status_label = ttk.Label(
            master=submit_frame,
            textvariable=self.match_submission_status_message,
        )
        status_label.pack(side="top", anchor="center", pady=5)

    def handle_match_submit(self):
        player1 = self.player1_var.get()
        player2 = self.player2_var.get()

        # if two usernames are the same show error
        if player1 == player2:
            self.match_submission_status_message.set(
                "Two players' usernames cannot be the same!"
            )
            return

        # if one of the player names are empty, show error
        if not player1 or not player2:
            self.match_submission_status_message.set("Player name cannot be empty!")
            return

        winner = self.winner_var.get()
        winner_username = ""
        loser_username = ""

        if winner == "player1":
            winner_username = player1
            loser_username = player2
        else:
            winner_username = player2
            loser_username = player1

        self.match_service.create_match(winner_username, loser_username)

        self.refresh_player_table()

    def initialize_player_creation(self, row_offset=5):
        """Initialize the player creation UI elements

        Args:
            row_offset: The starting row for component elements
        Returns:
            StringVar: The status message variable for external access
        """

        # creates a root frame for the player creation
        self.player_creation_frame = Frame(self.root)
        self.player_creation_frame.grid(
            row=row_offset, column=0, columnspan=3, sticky="ew"
        )
        # create header frame
        header_frame = Frame(self.player_creation_frame)
        header_frame.pack(fill="x")

        # header
        table_header = ttk.Label(header_frame, text="Create a player")
        table_header.pack(side="left", anchor="w", padx=5)

        # player creation frame
        player_creation_frame = Frame(self.player_creation_frame)
        player_creation_frame.pack(fill="x")

        # player input
        player_label = ttk.Label(player_creation_frame, text="Insert name of player")
        player_label.pack(side="left", anchor="w", padx=5)
        player_entry = ttk.Entry(
            player_creation_frame, textvariable=self.create_player_name
        )
        player_entry.pack(side="left", anchor="w", padx=5)

        # submit button frame
        submit_frame = Frame(self.player_creation_frame)
        submit_frame.pack(fill="x", pady=5)

        # Create button
        player_creation_frame = Frame(self.player_creation_frame)
        player_creation_button = ttk.Button(
            master=submit_frame, text="Create", command=self.create_player
        )
        player_creation_button.pack(side="top", anchor="center", pady=5)

        # status message on player creation
        status_label = ttk.Label(
            master=player_creation_frame,
            textvariable=self.status_message,
        )
        status_label.pack(side="top", anchor="center", pady=5)

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
                self.refresh_player_table()
            except Exception as e:
                self.status_message.set(f"Error: {str(e)}")
        else:
            self.status_message.set("Error: Player name cannot be empty!")

    def fetch_users(self):
        """Fetch all users from the EloService"""
        self.players = self.elo_service.get_all_users()

    def refresh_player_table(self):
        """Refresh the player table by destroying and recreating the player frame"""
        if self.player_table_frame:
            self.player_table_frame.destroy()

        self.initialize_player_table(row_offset=10)

    def initialize_player_table(self, row_offset=10):
        """Initialize the player table UI elements with a frame-based approach

        Args:
            row_offset: The starting row for component elements
        """
        self.fetch_users()

        # creates a root frame for the player table
        self.player_table_frame = Frame(self.root)
        self.player_table_frame.grid(
            row=row_offset, column=0, columnspan=3, sticky="ew"
        )

        # create header frame
        header_frame = Frame(self.player_table_frame)
        header_frame.pack(fill="x")

        # on the left "player list" text, apart of headerframe
        table_header = ttk.Label(header_frame, text="Player List")
        table_header.pack(side="left", anchor="w", padx=5)

        # refresh button on the right, apart of header frame
        refresh_button = ttk.Button(
            master=header_frame,
            text="Refresh Players",
            command=self.refresh_player_table,
        )
        refresh_button.pack(side="right", anchor="e", padx=5)

        # player list frame
        player_list_frame = Frame(self.player_table_frame)
        player_list_frame.pack(fill="x", expand=True, pady=5)

        # sort players by elo rating in descending order
        def get_elo_rating(player):
            return player.elo_rating

        sorted_players = sorted(self.players, key=get_elo_rating, reverse=True)

        # adding each player with pack to the player list frame
        for i, player in enumerate(sorted_players):
            player_row = Frame(player_list_frame)
            player_row.pack(fill="x", pady=2)

            player_label = ttk.Label(player_row, text=player.name)
            player_label.pack(side="left", anchor="w", padx=5)

            elo_label = ttk.Label(player_row, text=f"{round(player.elo_rating)}")
            elo_label.pack(side="right", anchor="e", padx=5)
