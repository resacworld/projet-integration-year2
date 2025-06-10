from ..database.database import Database

class robot:
    @staticmethod
    def checkExists(id: str) -> bool:
        """
        Check if a robot with the given ID exists in the database.
        """
        
        return Database.getConnection().cursor().execute(f"SELECT COUNT(*) FROM robot WHERE id = \"${id}\"").fetchone()[0] > 0