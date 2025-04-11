class Match:
    """
    Represents a FIFA match between two players.

    Attributes:
        id (int): The unique identifier for the match.
        player1_id (int): The unique identifier for the first player.
        player2_id (int): The unique identifier for the second player.
        winner (int): The unique identifier of the player who won the match.
        date (str): The date when the match took place.
    """

    def __init__(self, loser: int, winner: int, date, match_id: int = None):
        self.id = match_id
        self.winner = winner
        self.loser = loser
        self.date = date
