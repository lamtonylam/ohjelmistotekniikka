from db.database_connection import get_database_connection

from entities.match import Match


class MatchRepository:
    """
    A class to handle database operations related to matches.
    """

    def __init__(self, db):
        """
        Initializes a new instance of the class.

        Args:
            db: The database connection object to be used for database operations.
        """
        self._db = db
        self._cursor = self._db.cursor()

    def create_match(self, match: Match):
        """
        Inserts a new match record into the matches table in the database.

        Args:
            match (Match): An instance of the Match class containing the details
            of the match to be created, including the winner, loser,
            and date.

        Returns:
            Match: The same Match instance that was passed as an argument.
        """

        self._cursor.execute(
            "INSERT INTO matches (winner, loser, date) VALUES (?, ?, ?)",
            (match.winner, match.loser, match.date),
        )
        self._db.commit()

        return match

    def find_match_by_id(self, match_id):
        """
        Retrieves a match from the database by its ID.

        Args:
            match_id (int): The unique identifier of the match to retrieve.

        Returns:
            Match: An instance of the Match class representing the match with the given ID,
            or None if no match with the specified ID exists in the database.
        """
        self._cursor.execute(
            "SELECT id, winner, loser, date FROM matches WHERE id = ?",
            (match_id,),
        )
        row = self._cursor.fetchone()

        if not row:
            return None

        return Match(row["winner"], row["loser"], row["date"], match_id=row["id"])

    def get_all_matches(self):
        """
        Retrieves all matches from the database.

        Executes a SQL query to fetch all rows from the 'matches' table,
        and constructs a list of Match objects based on the retrieved data.

        Returns:
            list: A list of Match objects, each representing a match with
            its winner, loser, date, and match ID.
        """
        self._cursor.execute("SELECT id, winner, loser, date FROM matches")
        rows = self._cursor.fetchall()

        matches = []
        for row in rows:
            matches.append(Match(row["winner"], row["loser"], row["date"], match_id=row["id"]))

        return matches


match_repository = MatchRepository(get_database_connection())
