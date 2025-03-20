import os
import sqlite3

dirname = os.path.dirname(__file__)

DATABASE_FILE_PATH = os.path.join(dirname, "..", "..", "database.db")

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    """
    Gets the database connection.
    Returns:
        sqlite3.Connection: The database connection.
    """
    return connection
