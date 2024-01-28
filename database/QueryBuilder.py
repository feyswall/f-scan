import sqlite3
from .SQLiteConnector import SQLiteConnector

class QueryBuilder:

    def __init__(self):
        connector = SQLiteConnector()
        connector.connect()
        self.connection = connector.connection
        self.cursor = connector.cursor

        
    def insert_setup(self, name, port, ip):
        insert_query = "INSERT INTO setups (name, port, ip) VALUES (?, ?, ?)"
        try:
            self.cursor.execute(insert_query, (name, port, ip))
            self.connection.commit()
            print("setup inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting setup: {e}")


    def get_all_setups(self):
        select_query = "SELECT * FROM setups"
        try:
            self.cursor.execute(select_query)
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.OperationalError as e:
            print(f"Error fetching setups: {e}")
            return [('error', e)]


    def get_setup(self, sid):
        select_query = "SELECT * FROM setups WHERE id=?"
        try:
            self.cursor.execute(select_query, (sid))
            rows = self.cursor.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"Error fetching setups: {e}")

    
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed.")