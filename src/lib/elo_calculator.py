def calculate_elo(player1, player2, player1_elo, player2_elo, winner):
    """
    Calculate new Elo ratings for two players after a match.
    K rating factor is set to 32.
    Args:
        player1: player name for the first player.
        player2: player name for the second player.
        player1_elo: Current Elo rating of the first player.
        player2_elo: Current Elo rating of the second player.
        winner: player name of the player who won the match (either player1 or player2).
    Returns:
        A tuple containing the new Elo ratings (new_player1_elo, new_player2_elo).
    """

    K_FACTOR = 32

    expected_score_player1 = 1 / (1 + 10 ** ((player2_elo - player1_elo) / 400))
    expected_score_player2 = 1 / (1 + 10 ** ((player1_elo - player2_elo) / 400))

    if winner == player1:
        actual_score_player1 = 1
        actual_score_player2 = 0
    else:
        actual_score_player1 = 0
        actual_score_player2 = 1

    new_player1_elo = player1_elo + K_FACTOR * (
        actual_score_player1 - expected_score_player1
    )
    new_player2_elo = player2_elo + K_FACTOR * (
        actual_score_player2 - expected_score_player2
    )

    return new_player1_elo, new_player2_elo
