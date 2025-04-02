from tkinter import ttk, StringVar

from services.elo_service import EloService


class PlayerCreationComponent:
    """Component for creating new players"""
    
    def __init__(self, root):
        """Initialize the player creation component
        
        Args:
            root: The tkinter parent element
        """
        self.root = root
        self.create_player_name = StringVar()
        self.status_message = StringVar()
        self.elo_service = EloService()
        
    def initialize(self, row_offset=5):
        """Initialize the component UI elements
        
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
        status_label.grid(row=row_offset+1, column=0, columnspan=3)
        
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
            except Exception as e:
                self.status_message.set(f"Error: {str(e)}")
        else:
            self.status_message.set("Error: Player name cannot be empty!")