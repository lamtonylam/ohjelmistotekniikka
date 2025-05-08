import os
import sqlite3
import sys
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)


# get database file names from environment variables, with default values
load_dotenv()

DATABASE_FILE_NAME = os.getenv("DATABASE_FILE_NAME", "database.db")
TEST_DATABASE_FILE_NAME = os.getenv("TEST_DATABASE_FILE_NAME", "test_database.db")

# if the program is run in pytest mode, set the database file path to the test database
# otherwise, set it to the production database
if "pytest" in sys.modules:
    DATABASE_FILE_PATH = os.path.join(
        dirname,
        "..",
        "..",
        TEST_DATABASE_FILE_NAME,
    )
else:
    DATABASE_FILE_PATH = os.path.join(
        dirname,
        "..",
        "..",
        DATABASE_FILE_NAME,
    )

connection = sqlite3.connect(DATABASE_FILE_PATH)
connection.row_factory = sqlite3.Row


def get_database_connection():
    """
    Gets the database connection.
    Returns:
        sqlite3.Connection: The database connection.
    """
    return connection
