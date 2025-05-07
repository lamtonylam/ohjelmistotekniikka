from tkinter import Tk, ttk, StringVar, BooleanVar, Frame, constants
from services.elo_service import EloService
from services.match_service import MatchService


class MatchRecordingView:
    """Main UI class that coordinates the application's user interface"""

    def __init__(self, root, handle_hello_view):
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
        self.player_creation_status_message = StringVar()

        self.players = []
        self.matches = []

        # Main container frame
        self._frame = None

        # UI element frames
        self.match_submission_frame = None
        self.player_creation_frame = None
        self.player_table_frame = None
        self.matches_frame = None

        self.handle_hello_view = handle_hello_view

    def start(self):
        """Start the UI and arrange all components"""
        # Create the main frame
        self._frame = Frame(self.root)
        self._frame.pack(fill=constants.X)

        button = ttk.Button(
            master=self._frame,
            text="Back to main view",
            command=self.handle_hello_view,
        )
        button.pack(side="top", anchor="center", pady=5)

        self.initialize_match_submission()

        placeholder_label = ttk.Label(master=self._frame, text="")
        placeholder_label.pack()

        self.initialize_player_creation()

        placeholder_label = ttk.Label(master=self._frame, text="")
        placeholder_label.pack()

        self.initialize_player_table()

        self.initialize_match_table()

    def initialize_match_submission(self):
        """Initialize the match submission UI elements"""
        self.match_submission_frame = Frame(self._frame)
        self.match_submission_frame.pack(fill="x", pady=5)
        # create header frame
        header_frame = Frame(self.match_submission_frame)
        header_frame.pack(fill="x")

        # on the left "player list" text, apart of headerframe
        table_header = ttk.Label(
            header_frame, text="Record a match", font=("Helvetica", 16, "bold")
        )
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
        """
        Handles the submission of a match record by validating player names and winner selection.
        """
        player1 = self.player1_var.get()
        player2 = self.player2_var.get()

        # if either player name is empty, show error
        if not player1 or not player2:
            self.match_submission_status_message.set("Player name cannot be empty!")
            return

        # if two usernames are the same show error
        if player1 == player2:
            self.match_submission_status_message.set(
                "Two players' usernames cannot be the same!"
            )
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

        self.refresh_tables()

    def initialize_player_creation(self):
        """Initialize the player creation UI elements"""
        self.player_creation_frame = Frame(self._frame)
        self.player_creation_frame.pack(fill="x", pady=5)
        # create header frame
        header_frame = Frame(self.player_creation_frame)
        header_frame.pack(fill="x")

        # header
        table_header = ttk.Label(
            header_frame, text="Create a player", font=("Helvetica", 16, "bold")
        )
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
        player_creation_button = ttk.Button(
            master=submit_frame, text="Create", command=self.create_player
        )
        player_creation_button.pack(side="top", anchor="center", pady=5)

        # status message on player creation
        status_label = ttk.Label(
            master=submit_frame,
            textvariable=self.player_creation_status_message,
        )
        status_label.pack(side="top", anchor="center", pady=5)

    def create_player(self):
        """Handle player creation button click"""
        player_name = self.create_player_name.get()
        if player_name:
            try:
                self.elo_service.create_user(player_name)
                self.player_creation_status_message.set(
                    f"Player '{player_name}' has been added successfully!"
                )
                self.create_player_name.set("")
                self.refresh_tables()
            except Exception as e:
                self.player_creation_status_message.set(f"Error: {str(e)}")
        else:
            self.player_creation_status_message.set(
                "Error: Player name cannot be empty!"
            )

    def fetch_users(self):
        """Fetch all users from the EloService"""
        self.players = self.elo_service.get_all_users()

    def refresh_tables(self):
        """Refresh the player table by destroying and recreating the player frame"""
        if self.player_table_frame:
            self.player_table_frame.destroy()
            if self.matches_frame:
                self.matches_frame.destroy()

        self.initialize_player_table()
        self.initialize_match_table()

    def initialize_player_table(self):
        """Initialize the player table UI elements with a frame-based approach"""
        self.fetch_users()
        self.player_table_frame = Frame(self._frame)
        self.player_table_frame.pack(fill="x", pady=5)
        # create header frame
        header_frame = Frame(self.player_table_frame)
        header_frame.pack(fill="x")

        # on the left "player list" text, apart of headerframe
        table_header = ttk.Label(
            header_frame, text="Player List", font=("Helvetica", 16, "bold")
        )
        table_header.pack(side="left", anchor="w", padx=5)

        # on the right "elo rating" text, apart of headerframe
        elo_header = ttk.Label(header_frame, text="Elo Rating")
        elo_header.pack(side="right", anchor="e", padx=5)

        # player list frame
        player_list_frame = Frame(self.player_table_frame)
        player_list_frame.pack(fill="x", expand=True, pady=5)

        # sort players by elo rating in descending order
        def get_elo_rating(player):
            return player.elo_rating

        sorted_players = sorted(self.players, key=get_elo_rating, reverse=True)

        # adding each player with pack to the player list frame
        for player in sorted_players:
            player_row = Frame(player_list_frame)
            player_row.pack(fill="x", pady=2)

            player_label = ttk.Label(player_row, text=player.name)
            player_label.pack(side="left", anchor="w", padx=5)

            elo_label = ttk.Label(player_row, text=f"{round(player.elo_rating)}")
            elo_label.pack(side="right", anchor="e", padx=5)

    def fetch_matches(self):
        """Fetch all matches from the MatchService"""
        self.matches = self.match_service.get_all_matches()
        self.matches.sort(key=lambda match: match.date, reverse=True)

    def initialize_match_table(self):
        """Initialize match table that displays the played matches"""
        self.fetch_matches()
        self.matches_frame = Frame(self._frame)
        self.matches_frame.pack(fill="x", pady=5)
        header_frame = Frame(self.matches_frame)
        header_frame.pack(fill="x")

        table_header = ttk.Label(
            header_frame, text="Matches", font=("Helvetica", 16, "bold")
        )
        table_header.pack(side="left", anchor="w", padx=5)

        sorted_label = ttk.Label(
            header_frame,
            text="Matches are sorted from the most recent to the oldest",
        )
        sorted_label.pack(side="right", anchor="e", padx=5)

        winner_loser_header_frame = Frame(self.matches_frame)
        winner_loser_header_frame.pack(fill="x", pady=5)

        winner_label = ttk.Label(winner_loser_header_frame, text="Winner")
        winner_label.pack(side="left", anchor="w", padx=5)

        loser_label = ttk.Label(winner_loser_header_frame, text="Loser")
        loser_label.pack(side="left", anchor="w", padx=5)

        date_label = ttk.Label(winner_loser_header_frame, text="Date")
        date_label.pack(side="right", anchor="e", padx=5)

        for match in self.matches:
            match_row = Frame(self.matches_frame)
            match_row.pack(fill="x", pady=2)

            player1_label = ttk.Label(
                match_row, text=self.elo_service.find_user_by_id(match.winner).name
            )
            player1_label.pack(side="left", anchor="w", padx=5)

            vs_label = ttk.Label(match_row, text="vs")
            vs_label.pack(side="left", anchor="w", padx=5)

            player2_label = ttk.Label(
                match_row, text=self.elo_service.find_user_by_id(match.loser).name
            )
            player2_label.pack(side="left", anchor="w", padx=5)

            date_label = ttk.Label(match_row, text=match.date)
            date_label.pack(side="right", anchor="e", padx=5)

    def destroy(self):
        """Destroy all frames and UI components in this view"""
        if self._frame:
            self._frame.destroy()
            self._frame = None
