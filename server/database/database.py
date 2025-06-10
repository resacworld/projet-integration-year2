import sqlite3
import os
from .interfaces.base import BaseRepository

class Database():
    """
    A class to manage the SQLite database connection.
    """

    # conn = sqlite3.connect(os.getenv("SQLITE_URL"))

    def __init__(self):
        raise RuntimeError("Static class, cannot be instantiated.")

    # def __new__(cls, *args, **kwargs):
    #     """
    #     Ensure that only one instance of the Database class is created (Singleton pattern).
    #     """
    #     if not cls._instance:
    #         cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
    #     return cls._instance
    
    # def getCurrentRepository(self) -> BaseRepository:
    #     """
    #     Returns the current repository connection.
    #     """
    #     return self.conn


    @staticmethod
    def getConnection() -> sqlite3.Connection:
        """
        Returns the SQLite database connection.
        """

        return sqlite3.connect(os.getenv("SQLITE_URL"))

    # @staticmethod
    # def getCursor() -> sqlite3.Cursor:
    #     """
    #     Returns a the cursor of the connection.
    #     """

    #     return Database.conn.cursor()
