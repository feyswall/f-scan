import sqlite3
from .SQLiteConnector import SQLiteConnector

class SQLiteTables:
    def __init__(self):
        self.connector = SQLiteConnector()
        self.connector.connect()
        

    def create_setups_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS setups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                port TEXT NOT NULL,
                ip TEXT NOT NULL
            );
        '''
        try:
            self.connector.cursor.execute(create_table_query)
            # self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")

    def create_tables(self):
        self.create_setups_table()





