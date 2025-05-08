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

    def test_match_recording_with_two_same_players_doesnt_record_a_match(self):
        with self.assertRaises(Exception) as e:
            self.match_service.create_match("winner1", "winner1")

        self.assertEqual(str(e.exception), "A player cannot play against themselves")

        all_matches = self.match_service.get_all_matches()
        self.assertEqual(len(all_matches), 0)

    def test_match_recording_with_one_player_having_really_low_elo_doesnt_go_below_100(
        self,
    ):
        self.elo_service.create_user("winner1")
        self.elo_service.create_user("loser1")
        self.elo_service.update_user_elo(1, 1500)
        loser_id = self.elo_service.find_user_by_username("loser1").id
        self.elo_service.update_user_elo(loser_id, 101)

        self.match_service.create_match("winner1", "loser1")

        self.assertGreaterEqual(
            self.elo_service.find_user_by_id(loser_id).elo_rating, 100
        )

    def test_get_al_matches(self):
        self.match_service.create_match("winner1", "loser1")
        self.match_service.create_match("winner1", "loser1")

        matches = self.match_service.get_all_matches()

        self.assertEqual(len(matches), 2)
