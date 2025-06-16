import sqlite3
import os

class Database():
    """
    A class to manage the SQLite database connection.
    """

    def __init__(self):
        """
        Intialsation method, not possible here because this is a static class
        """
        raise RuntimeError("Static class, cannot be instantiated.")

    @staticmethod
    def getConnection() -> sqlite3.Connection:
        """
        Returns the SQLite database connection.
        """

        return sqlite3.connect(os.getenv("SQLITE_URL"))
