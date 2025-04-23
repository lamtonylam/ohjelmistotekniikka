import os
import sqlite3
import sys

dirname = os.path.dirname(__file__)


# if the program is run in pytest mode, set the database file path to the test database
# otherwise, set it to the production database
if "pytest" in sys.modules:
    DATABASE_FILE_PATH = os.path.join(dirname, "..", "..", "test_database.db")
else:
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
