from db.database_connection import get_database_connection

from entities.match import Match


class MatchRepository:
    def __init__(self, db):
        self._db = db
        self._cursor = self._db.cursor()

    def create_match(self, match: Match):

        self._cursor.execute(
            "INSERT INTO matches (winner, loser, date) VALUES (?, ?, ?)",
            (match.winner, match.loser, match.date),
        )
        self._db.commit()

        return match

    def find_match_by_id(self, id):
        self._cursor.execute(
            "SELECT id, winner, loser, date FROM matches WHERE id = ?",
            (id,),
        )
        row = self._cursor.fetchone()

        if not row:
            return None

        return Match(row["winner"], row["loser"], row["date"], match_id=row["id"])


match_repository = MatchRepository(get_database_connection())
