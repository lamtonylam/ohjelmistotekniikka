from datetime import datetime

from entities.match import Match
from repositories.match_repository import match_repository as default_match_repository
from repositories.user_repository import user_repository as default_user_repository
from lib.elo_calculator import calculate_elo
from .elo_service import EloService


class MatchService:
    """Service for managing matches and updating Elo ratings."""

    def __init__(
        self,
        match_repository=default_match_repository,
        user_repository=default_user_repository,
    ):
        """
        Initialize the MatchService with repositories.

        Args:
            match_repository: Repository for match data.
            user_repository: Repository for user data.
        """
        self.match_repository = match_repository
        self._user_repository = user_repository
        self.elo_service = EloService()

    def create_match(self, winner_username, loser_username):
        """
        Creates a new match record between two users, updates their Elo ratings, 
        and ensures both users exist.

        Args:
            winner_username (str): The username of the match winner.
            loser_username (str): The username of the match loser.

        Returns:
            None
        """

        # if one of the usernames is empty, dont proceed
        if not winner_username or not loser_username:
            return

        found_winner_user = self._user_repository.find_user_by_username(winner_username)
        found_loser_user = self._user_repository.find_user_by_username(loser_username)

        if not found_winner_user:
            self.elo_service.create_user(winner_username)
        if not found_loser_user:
            self.elo_service.create_user(loser_username)

        # date that is compatible with sqlite
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        winner_id = self.elo_service.find_user_by_username(winner_username).id
        loser_id = self.elo_service.find_user_by_username(loser_username).id

        match = Match(winner_id, loser_id, date)
        self.match_repository.create_match(match)

        winner_new_elo, loser_new_elo = self.compute_elo_ratings(winner_id, loser_id)

        # elo ranking should not be less than 100, per us chess federation
        winner_new_elo = max(winner_new_elo, 100)
        loser_new_elo = max(loser_new_elo, 100)

        self.elo_service.update_user_elo(winner_id, winner_new_elo)
        self.elo_service.update_user_elo(loser_id, loser_new_elo)

    def compute_elo_ratings(self, winner_id, loser_id):
        """
        Calculates and returns the new Elo ratings for the winner and loser of a match.

        Args:
            winner_id (int): The unique identifier of the winning user.
            loser_id (int): The unique identifier of the losing user.

        Returns:
            tuple: A tuple containing the new Elo ratings (winner_new_elo, loser_new_elo).
        """
        winner_elo = self.elo_service.find_user_by_id(winner_id).elo_rating
        loser_elo = self.elo_service.find_user_by_id(loser_id).elo_rating

        player1_new_elo, player2_new_elo = calculate_elo(
            winner_elo=winner_elo,
            loser_elo=loser_elo,
        )

        return (player1_new_elo, player2_new_elo)

    def find_match_by_id(self, match_id):
        """
        Retrieve a match object by its unique identifier.

        Args:
            match_id (int): The unique identifier of the match to retrieve.

        Returns:
            Match: The match object corresponding to the given id, or None if not found.
        """
        return self.match_repository.find_match_by_id(match_id)

    def get_all_matches(self):
        """
        Retrieves all match records from the match repository.

        Returns:
            list: A list of all match objects retrieved from the repository.
        """
        return self.match_repository.get_all_matches()
