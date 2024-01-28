import sqlite3
from .SQLiteConnector import SQLiteConnector

class SQLiteTables:

    def __init__(self):
        self.create_setups_table()
        connector = SQLiteConnector()
        connector.connect()
        self.connection = connector.connection
        self.cursor = connector.cursor
        

    def create_setups_table(self):
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS setups (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                port TEXT NOT NULL,
                ip TEXT NOT NULL
            );
        '''
        print(create_table_query)
        try:
            self.cursor.execute(create_table_query)
            # self.connection.commit()
            print("Table created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")


    def table_exists(self, table_name, table="setups"):
        check_table = ''' 
            SELECT NAME FROM sqlite_master WHERE type="table" AND name=?
        '''
        self.cursor.execute(check_table, (table))
        result = self.cursor.fetchone()
        return result is not None




