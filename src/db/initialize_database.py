from db.database_connection import get_database_connection


def drop_tables(connection):
    """
    Drops the 'users' and 'matches' tables from the database if they exist.

    Args:
        connection: A database connection object that provides a cursor for executing SQL commands.
    """
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS matches")

    connection.commit()


def create_tables(connection):
    """
    Creates the necessary tables in the database if they do not already exist.

    This function initializes two tables:
    1. `users`: Stores user information, including an auto-incrementing ID,
        a name, and an Elo rating.
    2. `matches`: Records match results, including an auto-incrementing ID,
        the IDs of the winner and loser (referencing the `users` table),
        and the date of the match.

    Args:
        connection: A SQLite database connection object.

    Raises:
        sqlite3.DatabaseError: If there is an issue executing the SQL commands.
    """

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
    """
    Initializes the database by establishing a connection, dropping existing tables,
    and creating new tables.

    This function ensures that the database is in a clean state by removing any
    existing tables and recreating them.
    """

    connection = get_database_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
