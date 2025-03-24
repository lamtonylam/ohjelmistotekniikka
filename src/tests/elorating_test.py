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
        player1 = "Tony"
        player2 = "Tomppa"
        player1_elo = 1400
        player2_elo = 1600
        winner = player2

        game_result = calculate_elo(player1, player2, player1_elo, player2_elo, winner)

        self.assertEqual(game_result, (1392.31, 1607.69))
