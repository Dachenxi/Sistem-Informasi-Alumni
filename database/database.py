import sqlite3

class Database:
    def __init__(self, db_path: str = 'database.db'):
        self.db_path = db_path

    def _db_connection(self):
        return sqlite3.connect(self.db_path)

    def execute(self, query: str, params: tuple = ()):
        try:
            with self._db_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                return True
        except sqlite3.Error as e:
            return False

    def fetch(self, query: str, params: tuple = (), one: bool = False):
        try:
            with self._db_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(query, params)
                if one:
                    result = cursor.fetchone()
                    return dict(result) if result else None
                else:
                    results = cursor.fetchall()
                    return [dict(row) for row in results]
        except sqlite3.Error as e:
            return None