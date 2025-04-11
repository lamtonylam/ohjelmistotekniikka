from entities.match import Match

from repositories.match_repository import match_repository as default_match_repository
from datetime import datetime

from lib.elo_calculator import calculate_elo

from .elo_service import EloService


class MatchService:

    def __init__(self, match_repository=default_match_repository):
        self.match_repository = match_repository

    def create_match(self, winner_username, loser_username, date):

        # date that is compatible with sqlite
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        winner = EloService.find_user_by_username(winner_username).id
        loser = EloService.find_user_by_username(loser_username).id

        match = Match(winner, loser, date)
        self.match_repository.create_match(match)

        winner_new_elo, loser_new_elo = calculate_elo(winner, loser)

        EloService.update_user_elo(winner, winner_new_elo)
        EloService.update_user_elo(loser, loser_new_elo)

    def calculate_elo(self, winner_id, loser_id):
        winner_elo = EloService.find_user_by_id(winner_id).elo_rating
        loser_elo = EloService.find_user_by_id(loser_id).elo_rating

        player1_new_elo, player2_new_elo = calculate_elo(
            winner_id=winner_id,
            loser_id=loser_id,
            winner_elo=winner_elo,
            loser_elo=loser_elo,
        )

        result = {
            "player1_new_elo": player1_new_elo,
            "player2_new_elo": player2_new_elo,
        }

        return result
