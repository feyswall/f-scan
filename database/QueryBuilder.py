import sqlite3
from .SQLiteConnector import SQLiteConnector

class QueryBuilder:

    def __init__(self):
        self.connector = SQLiteConnector()

        
    def insert_setup(self, name, port, ip):
        insert_query = "INSERT INTO setups (name, port, ip) VALUES (?, ?, ?)"
        try:
            self.connector.connect()
            self.connector.cursor.execute(insert_query, (name, port, ip))
            self.connector.connection.commit()
            self.connector.close_connection()
            print("setup inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting setup: {e}")


    def get_all_setups(self):
        select_query = "SELECT * FROM setups"
        try:
            self.connector.connect()
            self.connector.cursor.execute(select_query)
            rows = self.connector.cursor.fetchall()
            self.connector.close_connection()
            return rows
        except sqlite3.OperationalError as e:
            print(f"Error fetching setups: {e}")
            return [('error', e)]


    def get_setup(self, sid):
        select_query = "SELECT * FROM setups WHERE id=?"
        try:
            self.connector.connect()
            self.connector.cursor.execute(select_query, (sid))
            rows = self.connector.cursor.fetchone()
            self.connector.close_connection()
            return rows
        except sqlite3.Error as e:
            print(f"Error fetching setups: {e}")
