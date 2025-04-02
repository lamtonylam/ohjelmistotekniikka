from tkinter import Tk, ttk, StringVar

from ui.components.player_creation import PlayerCreationComponent
from ui.components.match_submission import MatchSubmissionComponent


class UI:
    """Main UI class that coordinates the application's user interface"""

    def __init__(self, root):
        """Initialize the UI

        Args:
            root: The tkinter root window
        """
        self.root = root

        # Initialize components
        self.match_submission = MatchSubmissionComponent(root)
        self.player_creation = PlayerCreationComponent(root)

    def start(self):
        """Start the UI and arrange all components"""
        # Initialize match submission component
        self.match_submission.initialize(row_offset=0)

        # Add a separator placeholder
        placeholder_label = ttk.Label(master=self.root, text="")
        placeholder_label.grid(row=4, column=0)

        # Initialize player creation component
        self.player_creation.initialize(row_offset=5)
