import os
import sys


from db.database_connection import get_database_connection



# Add the parent directory to sys.path to allow relative imports when run directly
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)



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
            player1_id INTEGER NOT NULL,
            player2_id INTEGER NOT NULL,
            winner INTEGER NOT NULL
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
