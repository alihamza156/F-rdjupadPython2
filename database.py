# database.py
import sqlite3


# Anslut till databasen (den skapas om den inte finns för att förenkla test av kod).



def create_connection():
    """Skapar och returnerar en anslutning till SQLite-databasen."""
    conn = sqlite3.connect('my_database.db')
    return conn

def create_table():
    """Skapar tabellen 'people' om den inte redan finns."""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        city TEXT
    )
    ''')
    
    conn.commit()
    conn.close()

def insert_data(data):
    """Sätter in data i tabellen 'people'."""
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.executemany("INSERT INTO people (name, age, city) VALUES (?, ?, ?)", data)
    
    conn.commit()
    conn.close()