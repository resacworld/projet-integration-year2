import sqlite3
import os


class Database:
    """
    A class to manage the SQLite database connection.
    """

    _instance = None

    def __init__(self):
        self.conn = sqlite3.connect('database.db')

    def __new__(cls, *args, **kwargs):
        """
        Ensure that only one instance of the Database class is created (Singleton pattern).
        """
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    @staticmethod
    def getConnection(self):
        """
        Returns the SQLite database connection.
        """

        return sqlite3.connect(os.getenv("SQLITE_URL"))

    @staticmethod
    def getCursor(self):
        """
        Returns a the cursor of the connection.
        """

        return sqlite3.connect(os.getenv("SQLITE_URL")).cursor()
