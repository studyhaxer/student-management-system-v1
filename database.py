from config import DB_NAME
import sqlite3

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    try:
        sqliteConnection = sqlite3.connect(DB_NAME)
        cursor = sqliteConnection.cursor()
        tbl_qry = """
        CREATE TABLE IF NOT EXISTS students( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name TEXT NOT NULL, 
        age INTEGER, 
        course TEXT,
        marks REAL);
        """
        cursor.execute(tbl_qry)
        sqliteConnection.commit()
    except sqlite3.Error as error:
        print('Error occurred -', error)