import sqlite3

class SQLiteConnector:
    def __init__(self, db_name='swanDB.db'):
        self.db_name = db_name
        self.connection = None
        self.cursor = None


    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            self.cursor = self.connection.cursor()
            return self.cursor
            print(f"Connected to {self.db_name} successfully.")
        except sqlite3.Error as e:
            print(f"Error connecting to {self.db_name}: {e}")


    def close_connection(self):
        if self.connection:
            self.connection.close()
