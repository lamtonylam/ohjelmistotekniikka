from entities.user import User

from repositories.user_repository import user_repository as default_user_repository


class UsernameExistsError(Exception):
    pass


class EloService:
    """Service class for managing user operations related to Elo ratings."""

    def __init__(self, user_repostory=default_user_repository):
        """
        Initializes the EloService with a user repository.

        Args:
            user_repostory (UserRepository, optional): The repository used to manage user data.
                Defaults to `default_user_repository`.
        """
        self._user_repository = user_repostory

    def create_user(self, name):
        """
        Creates a new user with the given name.

        Args:
            name (str): The username for the new user.

        Raises:
            UsernameExistsError: If a user with the given username already exists.

        Returns:
            User: The newly created user instance.
        """
        existing_user = self._user_repository.find_user_by_username(name)

        if existing_user:
            raise UsernameExistsError(f"Username {name} already exists")

        user = self._user_repository.create_user(User(name))

        return user

    def get_all_users(self):
        """Retrieve all users from the repository

        Returns:
            list: A list of all User objects
        """
        return self._user_repository.find_all_users()

    def find_user_by_id(self, user_id):
        """
        Retrieves a user by their unique identifier.

        Args:
            user_id (int): The unique identifier of the user to find.

        Returns:
            User: The user object if found, None otherwise.
        """
        return self._user_repository.find_user_by_id(user_id)

    def find_user_by_username(self, username):
        """
        Retrieves a user by their username.

        Args:
            username (str): The username of the user to find.

        Returns:
            User: The user object if found, None otherwise.
        """
        return self._user_repository.find_user_by_username(username)

    def update_user_elo(self, user_id, elo):
        """
        Updates the Elo rating of a user.

        Args:
            user_id (int): The unique identifier of the user to update.
            elo (int): The new Elo rating to set for the user.
        """
        return self._user_repository.update_user_elo(user_id, elo)
