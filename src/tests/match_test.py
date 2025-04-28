import unittest

from build import build

from services.match_service import MatchService
from services.elo_service import EloService


class TestMatches(unittest.TestCase):
    def setUp(self):
        build()
        self.match_service = MatchService()
        self.elo_service = EloService()

    def test_match_recording(self):
        self.match_service.create_match("winner1", "loser1")

        winner_id = self.elo_service.find_user_by_username("winner1").id
        loser_id = self.elo_service.find_user_by_username("loser1").id

        created_match = self.match_service.find_match_by_id(1)

        self.assertEqual(created_match.id, 1)
        self.assertEqual(created_match.winner, winner_id)
        self.assertEqual(created_match.loser, loser_id)

    def test_get_al_matches(self):
        self.match_service.create_match("winner1", "loser1")
        self.match_service.create_match("winner1", "loser1")

        matches = self.match_service.get_all_matches()

        self.assertEqual(len(matches), 2)
