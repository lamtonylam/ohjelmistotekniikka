class User:
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.
        elo_rating (int): The Elo rating of the user, defaults to 1500.
    """

    def __init__(self, name: str, id: int = None):
        self.id = id
        self.name = name
        self.elo_rating = 1500
