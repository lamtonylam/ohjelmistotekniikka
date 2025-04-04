from tkinter import ttk, StringVar, BooleanVar
from services.elo_service import EloService


class PlayerTableComponent:
    """Component for player table in the UI"""

    def __init__(self, root):
        """Initialize the PlayerTableComponent

        Args:
            root: The tkinter parent element
        """
        self.root = root
        self.players = []
        self.elo_service = EloService()

    def fetch_users(self):
        """Fetch all users from the EloService and update the players list"""
        self.players = self.elo_service.get_all_users()

    def initialize(self, row_offset=0):
        """Initialize the component UI elements

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
