from db.database_connection import get_database_connection
from entities.user import User


def get_user_by_row(row):
    if row:
        return User(row["name"], row["id"], row["elo_rating"])
    return None


class UserRepository:
    def __init__(self, db):
        self._db = db

    def find_all_users(self):
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        users = []
        for row in rows:
            user = get_user_by_row(row)
            users.append(user)

        return users

    def find_user_by_username(self, name: str):
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
        row = cursor.fetchone()

        return get_user_by_row(row)

    def find_user_by_id(self, user_id: int):
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create_user(self, user: User):
        cursor = self._db.cursor()
        cursor.execute(
            "INSERT INTO users (name, elo_rating) VALUES (?, ?)",
            (user.name, user.elo_rating),
        )

        self._db.commit()

        return user

    def update_user_elo(self, user_id, elo):
        cursor = self._db.cursor()
        cursor.execute(
            "UPDATE users SET elo_rating = ? WHERE id = ?",
            (elo, user_id),
        )
        self._db.commit()


user_repository = UserRepository(get_database_connection())
