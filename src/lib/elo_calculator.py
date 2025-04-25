def round_number_two_decimals(number):
    """
    Rounds a given number to two decimal places.

    Args:
        number (float): The number to be rounded.

    Returns:
        float: The number rounded to two decimal places.
    """
    return round(number, 2)


def calculate_elo(winner_elo, loser_elo):
    """
    Calculate the new Elo ratings for the winner and loser of a match.

    The Elo rating system is used to calculate the relative skill levels of players
    in two-player games. This function updates the ratings based on the outcome
    of a match, using the standard Elo formula with a K-factor of 32.

    Args:
        winner_elo (float): The current Elo rating of the winner.
        loser_elo (float): The current Elo rating of the loser.

    Returns:
        tuple: A tuple containing the new Elo ratings for the winner and the loser,
        rounded to two decimal places. Note that the order is the same as the input.
    """

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
