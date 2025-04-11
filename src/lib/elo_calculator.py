def round_number_two_decimals(number):
    return round(number, 2)


def calculate_elo(winner_elo, loser_elo):

    k_factor = 32

    expected_score_winner = 1 / (1 + 10 ** ((loser_elo - winner_elo) / 400))
    expected_score_loser = 1 / (1 + 10 ** ((winner_elo - loser_elo) / 400))

    actual_score_winner = 1
    actual_score_loser = 0

    winner_new_elo = winner_elo + k_factor * (
        actual_score_winner - expected_score_winner
    )
    loser_new_elo = loser_elo + k_factor * (actual_score_loser - expected_score_loser)

    return round_number_two_decimals(winner_new_elo), round_number_two_decimals(
        loser_new_elo
    )
