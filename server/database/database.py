import sqlite3
import os


class Database:
    """
    A class to manage the SQLite database connection.
    """

    _instance = None

    def __init__(self):
        self.conn = sqlite3.connect(os.getenv("SQLITE_URL"))

    def __new__(cls, *args, **kwargs):
        """
        Ensure that only one instance of the Database class is created (Singleton pattern).
        """
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    def getConnection(self) -> sqlite3.Connection:
        """
        Returns the SQLite database connection.
        """

        return self.conn

    def getCursor(self) -> sqlite3.Cursor:
        """
        Returns a the cursor of the connection.
        """

        return self.conn.cursor()
