from db.database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS matches")

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            elo_rating INTEGER NOT NULL
        );
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            winner INTEGER NOT NULL,
            loser INTEGER NOT NULL,
            date TEXT NOT NULL,
            FOREIGN KEY (winner) REFERENCES users (id),
            FOREIGN KEY (loser) REFERENCES users (id)
        );
    """
    )

    connection.commit()


def initialize_database():
    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
