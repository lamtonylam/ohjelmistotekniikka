import unittest

from lib.elo_calculator import calculate_elo, round_number_two_decimals
from build import build


class TestEloCalculator(unittest.TestCase):
    def setUp(self):
        build()

    def test_number_rounding(self):
        number = 120.1111111
        rounded_number = round_number_two_decimals(number)

        self.assertEqual(rounded_number, 120.11)

    def test_correct_elo(self):
        winner_elo = 1600
        loser_elo = 1400

        game_result = calculate_elo(winner_elo, loser_elo)

        self.assertEqual(game_result, (1607.69, 1392.31))
