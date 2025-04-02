from tkinter import ttk, StringVar, BooleanVar


class MatchSubmissionComponent:
    """Component for submitting match results"""
    
    def __init__(self, root):
        """Initialize the match submission component
        
        Args:
            root: The tkinter parent element
        """
        self.root = root
        self.player1_var = StringVar()
        self.player2_var = StringVar()
        self.player1_won = BooleanVar()
        self.player2_won = BooleanVar()
        
    def initialize(self, row_offset=0):
        """Initialize the component UI elements
        
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
        submit_button = ttk.Button(
            master=self.root, text="Submit", command=self.handle_submit
        )
        
        # layout grid
        player1_label.grid(row=row_offset, column=0)
        player1_entry.grid(row=row_offset, column=1)
        player2_label.grid(row=row_offset+1, column=0)
        player2_entry.grid(row=row_offset+1, column=1)
        player1_check.grid(row=row_offset+2, column=0)
        player2_check.grid(row=row_offset+2, column=1)
        submit_button.grid(row=row_offset+3, column=0, columnspan=2)
    
    def handle_submit(self):
        """Handle match submission button click"""
        # This will be implemented later when the functionality is added
        pass