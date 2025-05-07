from db.database_connection import get_database_connection
from entities.user import User


def get_user_by_row(row):
    """
    Retrieves a User object from a database row.

    Args:
        row (dict): A dictionary representing a database row with keys "name", "id",
                    and "elo_rating".

    Returns:
        User: An instance of the User class initialized with the values from the row,
        or None if the row is None.
    """
    if row:
        return User(row["name"], row["id"], row["elo_rating"])
    return None


class UserRepository:
    """Class handles all user-related database operations"""

    def __init__(self, db):
        """
        Initializes the UserRepository with a database connection.

        Args:
            db: The database connection object to be used for data storage and retrieval.
        """
        self._db = db
        self._cursor = self._db.cursor()

    def find_all_users(self):
        """
        Retrieves all users from the database.

        This method executes a SQL query to fetch all rows from the 'users' table,
        converts each row into a user object using the `get_user_by_row` function,
        and returns a list of user objects.

        Returns:
            list: A list of user objects representing all users in the database.
        """
        self._cursor.execute("SELECT * FROM users")
        rows = self._cursor.fetchall()

        users = []
        for row in rows:
            users.append(User(row["name"], row["id"], row["elo_rating"]))

        return users

    def find_user_by_username(self, name: str):
        """
        Finds a user in the database by their username.

        Args:
            name (str): The username of the user to search for.

        Returns:
            User: An instance of the User object if a matching user is found,
            or None if no user is found.
        """
        self._cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        row = self._cursor.fetchone()

        if not row:
            return None

        return User(row["name"], row["id"], row["elo_rating"])

    def find_user_by_id(self, user_id: int):
        """
        Retrieves a user from the database by their unique ID.

        Args:
            user_id (int): The unique identifier of the user to retrieve.

        Returns:
            User: An instance of the User object if a user with the given ID exists.
            None: If no user with the given ID is found.
        """
        self._cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = self._cursor.fetchone()

        if not row:
            return None

        return User(row["name"], row["id"], row["elo_rating"])

    def create_user(self, user: User):
        """
        Creates a new user in the database.

        Args:
            user (User): An instance of the User class containing the user's name
            and Elo rating.

        Returns:
            User: The created user instance.
        """
        self._cursor.execute(
            "INSERT INTO users (name, elo_rating) VALUES (?, ?)",
            (user.name, user.elo_rating),
        )

        self._db.commit()

        return user

    def update_user_elo(self, user_id, elo):
        """
        Updates the Elo rating of a user in the database.

        Args:
            user_id (int): The unique identifier of the user whose Elo rating is to be updated.
            elo (int): The new Elo rating to be assigned to the user.

        Raises:
            sqlite3.DatabaseError: If there is an issue executing the database query.
        """
        self._cursor.execute(
            "UPDATE users SET elo_rating = ? WHERE id = ?",
            (elo, user_id),
        )
        self._db.commit()


user_repository = UserRepository(get_database_connection())
