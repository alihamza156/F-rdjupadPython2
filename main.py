# main.py

import database  # Importerar modulen 'database.py'

def main():
    # Skapa anslutning till databasen
    conn = database.connect_db()

    # Skapa tabellen om den inte finns
    database.create_table(conn)

    # Lägg till testdata
    database.insert_test_data(conn)

    # Hämta och skriv ut all data
    data = database.fetch_all_data(conn)
    for row in data:
        print(row)

    # Stäng anslutningen
    conn.close()

if __name__ == "__main__":
    main()
