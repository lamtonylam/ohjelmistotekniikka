from db.initialize_database import initialize_database


def build():
    """
    Initializes the database by calling the initialize_database function.
    """
    initialize_database()


if __name__ == "__main__":
    build()
