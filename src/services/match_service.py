from datetime import datetime

from entities.match import Match
from repositories.match_repository import match_repository as default_match_repository
from repositories.user_repository import user_repository as default_user_repository
from lib.elo_calculator import calculate_elo
from .elo_service import EloService


class MatchService:

    def __init__(
        self,
        match_repository=default_match_repository,
        user_repostory=default_user_repository,
    ):
        self.match_repository = match_repository
        self._user_repository = user_repostory
        self.elo_service = EloService()

    def create_match(self, winner_username, loser_username):

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

        self.elo_service.update_user_elo(winner_id, winner_new_elo)
        self.elo_service.update_user_elo(loser_id, loser_new_elo)

    def compute_elo_ratings(self, winner_id, loser_id):
        winner_elo = self.elo_service.find_user_by_id(winner_id).elo_rating
        loser_elo = self.elo_service.find_user_by_id(loser_id).elo_rating

        player1_new_elo, player2_new_elo = calculate_elo(
            winner_elo=winner_elo,
            loser_elo=loser_elo,
        )

        return (player1_new_elo, player2_new_elo)

    def find_match_by_id(self, id):
        return self.match_repository.find_match_by_id(id)
